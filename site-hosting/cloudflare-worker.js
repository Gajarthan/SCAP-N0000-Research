// SCAP research public edge-hosting proxy.
// Cloudflare Worker name: scap-public-research
// Public URL: https://scap-public-research.thisanthan02.workers.dev/
// Source of truth: docs/ on main branch in Gajarthan/SCAP-N0000-Research.
// This Worker fetches static files from the GitHub raw public repository. It never
// requires GitHub-hosted Actions, secrets, a backend, or a paid database.
addEventListener('fetch', event => event.respondWith(serve(event.request)));
const ROOT = 'https://raw.githubusercontent.com/Gajarthan/SCAP-N0000-Research/main/docs';
const FILES = new Set(['/index.html','/assets/site.css','/assets/config.js','/assets/app.js','/assets/favicon.svg']);
async function serve(request) {
  if (request.method !== 'GET' && request.method !== 'HEAD')
    return new Response('Method not allowed', {status:405,headers:{Allow:'GET, HEAD'}});
  const target = new URL(request.url);
  const path = target.pathname === '/' ? '/index.html' : target.pathname;
  if (!FILES.has(path)) return new Response('Not found',{status:404,headers:{'Content-Type':'text/plain; charset=utf-8'}});
  const kind = path.endsWith('.html')?'text/html; charset=utf-8':
    path.endsWith('.css')?'text/css; charset=utf-8':
    path.endsWith('.js')?'application/javascript; charset=utf-8':'image/svg+xml';
  try {
    const resp = await fetch(ROOT+path,{cf:{cacheTtl:120,cacheEverything:true},
      headers:{'User-Agent':'SCAP-Research-Public-Site/1.0'}});
    if(!resp.ok) return new Response('Website asset unavailable: '+resp.status,{status:502});
    const headers=new Headers({'Content-Type':kind,
      'Cache-Control':path==='/index.html'?'public,max-age=60':'public,max-age=120',
      'X-Content-Type-Options':'nosniff',
      'Referrer-Policy':'strict-origin-when-cross-origin'});
    return new Response(request.method==='HEAD'?null:resp.body,{status:200,headers});
  } catch(e) {
    return new Response('Unable to load website source',{status:502});
  }
}
