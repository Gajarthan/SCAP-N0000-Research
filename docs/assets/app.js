(function () {
"use strict";
const CFG=window.SCAP_CONFIG;
if(!CFG || !document.getElementById("main-content")) return;
const TOPICS=CFG.topics,UI=CFG.ui,RAW=CFG.raw,REPO=CFG.repo;
const MAIN=document.getElementById("main-content");
const SELECT=document.getElementById("languageSelect");
const SIDEBAR=document.getElementById("sideNav");
const TOAST=document.getElementById("toast");
const TOPIC_STATUS={};
let sourceRecords=[],filter="all",query="",state,mermaidLoader=null;

function esc(v){return String(v==null?"":v).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]});}
function langOf(p){return p.startsWith("ta/")?"ta":p.startsWith("si/")?"si":"en";}
function labels(){return UI[state.lang];}
function title(t,l){return t[l==="ta"?2:l==="si"?3:1];}
function desc(t,l){return t[l==="ta"?5:l==="si"?6:4];}
function folder(t,l){return (l==="en"?"":l+"/")+t[0]+"/";}
function url(view,lang,doc){const p=new URLSearchParams();p.set("view",view);if(lang&&lang!=="en")p.set("lang",lang);if(doc)p.set("doc",doc);return "?"+p.toString();}
function pathIsSafe(p){return typeof p==="string"&&p.length<256&&!p.includes("..")&&/^[a-zA-Z0-9/_\-.]+\.md$/.test(p)&&(p.startsWith("sources/")||p.startsWith("01-")||p.startsWith("02-")||p.startsWith("ta/")||p.startsWith("si/")||["README.md","RESEARCH-QUEUE.md","SOURCES.md","RESEARCH-LOG.md"].includes(p));}
function parseRoute(){const q=new URLSearchParams(location.search);const d=q.get("doc")||"";const doc=pathIsSafe(d)?d:"";const view=["overview","research","financials","sources","report"].includes(q.get("view"))?q.get("view"):"overview";const l=q.get("lang");return {view:doc?"report":view,doc:doc,lang:doc&&langOf(doc)!=="en"?langOf(doc):["en","ta","si"].includes(l)?l:"en"};}
function status(t){return TOPIC_STATUS[t[0]]||(TOPICS.indexOf(t)<2?"PARTIAL":"TEMPLATE");}
function inProgress(){return TOPICS.filter(function(t){return status(t)!=="TEMPLATE"}).length;}
function sourceCount(){return sourceRecords.length||11;}
function pill(t){return status(t)==="FILLED"?'<span class="pill mint">● SOURCE-FILLED</span>':status(t)==="PARTIAL"?'<span class="pill gold">◕ PARTIAL</span>':'<span class="pill">○ FRAMEWORK</span>';}
function linkButton(text,view,doc,klass){return '<a class="btn '+(klass||"")+'" href="'+url(view,state.lang,doc)+'">'+esc(text)+'</a>';}
function githubDoc(doc){return REPO+"blob/main/"+doc.split("/").map(encodeURIComponent).join("/");}
function rawDoc(doc){return RAW+doc.split("/").map(encodeURIComponent).join("/");}
function section(title,subtitle,linkLabel,linkUrl){return '<div class="section-head"><div><h2>'+esc(title)+'</h2><p>'+esc(subtitle)+'</p></div>'+(linkLabel?'<a class="section-link" href="'+linkUrl+'">'+esc(linkLabel)+' ↗</a>':"")+'</div>';}
function crumbs(label){return '<div class="breadcrumbs"><a href="'+url("overview",state.lang)+'">'+esc(labels().home)+'</a><span>›</span><span>'+esc(label)+'</span></div>';}
function closeMobile(){SIDEBAR.classList.remove("is-open");document.getElementById("mobileMenu").setAttribute("aria-expanded","false");}
function sidebar(){
 const l=state.lang,x=labels();
 let s='<div class="nav-group"><div class="nav-group-title">'+esc(x.home)+'</div>';
 [["overview","◫",x.home],["research","▦",x.research],["financials","▥",x.financials],["sources","◎",x.sources]].forEach(function(item){
 s+='<a class="nav-item '+(state.view===item[0]?"active":"")+'" href="'+url(item[0],l)+'"><span class="num">'+item[1]+'</span><span class="label">'+esc(item[2])+'</span></a>';
 });
 s+="</div>";
 [0,15].forEach(function(i){
 const a=TOPICS.slice(i,i===0?15:20);
 s+='<div class="nav-group"><div class="nav-group-title"><span>'+esc(i===0?x.fund:x.tech)+'</span><span>'+a.length+'</span></div>';
 a.forEach(function(t,j){
 const path=folder(t,l)+"README.md";
 const active=state.doc===path||state.doc.startsWith(folder(t,l));
 s+='<a class="nav-item '+(active?"active":"")+'" href="'+url("report",l,path)+'"><span class="num">'+String(j+1).padStart(2,"0")+'</span><span class="label">'+esc(title(t,l))+'</span>'+(status(t)!=="TEMPLATE"?'<span class="tiny-dot"></span>':"")+'</a>';
 });
 s+="</div>";
 });
 s+='<div class="nav-group"><div class="nav-group-title">'+esc(x.sourceRegister)+'</div><a class="nav-item" href="'+url("report",l,"sources/SOURCE-REGISTER.md")+'"><span class="num">◇</span><span class="label">'+esc(x.sourceRegister)+'</span></a><a class="nav-item" href="'+url("report",l,(l==="en"?"":l+"/")+"RESEARCH-QUEUE.md")+'"><span class="num">◷</span><span class="label">'+esc(x.queue)+'</span></a></div>';
 document.getElementById("sideTopics").innerHTML=s;
 document.getElementById("sidebarCaption").textContent=x.research.toUpperCase();
 document.getElementById("sidebarStatus").textContent=inProgress()+" / 20 "+x.researchStatus;
 document.getElementById("sidebarUpdated").textContent="GitHub Markdown · 3 languages";
}
function topicCard(t){
const l=state.lang;
return '<a class="panel topic-card" href="'+url("report",l,folder(t,l)+"README.md")+'"><span class="topic-icon">'+esc(t[7])+'</span><h3>'+esc(title(t,l))+'</h3><p>'+esc(desc(t,l))+'</p><div class="topic-bottom">'+pill(t)+'<span class="topic-open" aria-hidden="true">↗</span></div></a>';
}
function bar(name,value,max,variant,number){
 const width=Math.min(100,Math.max(2,Math.abs(value)/max*100)).toFixed(1);
 return '<div class="bar-row"><span class="bar-name">'+esc(name)+'</span><div class="bar-track" role="img" aria-label="'+esc(name)+" "+esc(number)+'"><span class="bar-fill '+(variant||"")+'" style="width:'+width+'%"></span></div><strong class="bar-value">'+esc(number)+'</strong></div>';
}
function home(){
const x=labels(),l=state.lang,p=inProgress(),bf=(l==="en"?"":l+"/")+"01-Fundamental-Analysis/02-Financial-Statements/README.md";
let s='<section class="hero"><div><div class="page-kicker"><span class="kicker-line"></span>'+esc(x.eyebrow)+'</div><h1>'+esc(x.heroA)+'<br><em>'+esc(x.heroB)+'</em></h1><p>'+esc(x.heroP)+'</p><div class="hero-actions">'+linkButton(x.browse+" →","research",null,"btn-primary")+linkButton(x.viewFinancials,"financials")+'</div></div><div class="hero-orbit" aria-hidden="true"><div class="orbit-ring"></div><div class="orbit-ring two"></div><div class="orbit-core">SCAP<span class="mint">.</span></div><div class="orbit-blip one"></div><div class="orbit-blip two"></div><div class="orbit-blip three"></div></div></section><div class="section-rule"></div>';
const stats=[[x.topics,"20","15 fundamental · 5 technical"],[x.languages,"03","English · தமிழ் · සිංහල"],[x.records,String(sourceCount()),"Markdown source cards"],[x.progress,String(p)+"/20","Source research in progress"]];
s+='<section class="metric-grid" aria-label="Research summary">';
stats.forEach(function(a,i){s+='<div class="panel metric-card"><span class="metric-label">'+esc(a[0])+'</span><div class="metric-value">'+esc(a[1])+'</div><div class="metric-note"><span class="pill '+(i===3?"gold":"mint")+'">'+(i===3?"◔":"●")+'</span>'+esc(a[2])+'</div></div>';});
s+='</section>';
s+=section(x.pulse,x.pulseDesc,x.financials,url("financials",l));
s+='<section class="dash-grid"><div class="panel dash-panel"><div class="panel-title"><h3>'+esc(x.income)+'</h3><small>LKR BN</small></div><p class="panel-sub">'+esc(x.notes)+'</p><div class="viz">'+bar(x.period25,42.38372,55,"purple","42.38")+bar(x.period26,51.31049,55,"","51.31")+'</div><div class="panel-foot">FY2025: issuer audited · FY2026: 27 May 2026 interim, subject to audit · <a class="accent" href="'+url("report",l,bf)+'">Source ↗</a></div></div>';
s+='<div class="panel dash-panel"><div class="panel-title"><h3>'+esc(x.insight)+'</h3><small>FY2026 · INTERIM</small></div><p class="panel-sub">'+esc(x.insightP)+'</p><div class="attribution-numbers"><div><strong class="mint">0.97 bn</strong><small>'+esc(x.groupOwners)+'</small></div><div><strong style="color:var(--purple)">2.40 bn</strong><small>'+esc(x.minority)+'</small></div></div><div class="stackbar" role="img" aria-label="28.9% SCAP owners, 71.1% non-controlling interests"><span style="width:28.9%"></span><span style="width:71.1%"></span></div><div class="legend"><span><i style="background:var(--accent)"></i>28.9% '+esc(x.groupOwners)+'</span><span><i style="background:var(--purple)"></i>71.1% '+esc(x.minority)+'</span></div><div class="panel-foot">'+esc(x.notDividend)+' · FY2026 interim.</div></div></section>';
s+='<div class="insight"><span class="insight-icon">⌁</span><div><strong>'+esc(x.notes)+'</strong><p>'+esc(x.sourceNotice)+'</p></div></div>';
s+=section(x.libraryTitle,x.libraryDesc,x.more,url("research",l));
s+='<section class="research-grid">'+TOPICS.slice(0,6).map(topicCard).join("")+'</section>';
s+=section(x.sources,x.sourceDesc,x.sourceRegister,url("report",l,"sources/SOURCE-REGISTER.md"));
s+='<div class="source-strip"><a class="panel" href="'+url("report",l,"sources/SOURCE-REGISTER.md")+'"><span class="s-icon">▤</span><span>'+esc(x.sourceRegister)+'<small>'+sourceCount()+' '+esc(x.records)+'</small></span></a><a class="panel" href="'+url("report",l,folder(TOPICS[0],l)+"VISUAL-REPORT.md")+'"><span class="s-icon">⌘</span><span>'+esc(x.libraryTitle)+'<small>16 business visuals</small></span></a><a class="panel" href="'+url("report",l,(l==="en"?"":l+"/")+"RESEARCH-QUEUE.md")+'"><span class="s-icon">◷</span><span>'+esc(x.queue)+'<small>'+p+' / 20</small></span></a></div>';
return s;
}
function library(){
const x=labels();
MAIN.innerHTML=crumbs(x.research)+'<div class="page-kicker"><span class="kicker-line"></span>20 RESEARCH CHAPTERS</div><h1 class="page-title">'+esc(x.research)+'</h1><p class="page-description">'+esc(x.libraryDesc)+'</p><div class="controls"><input id="topicSearch" class="searchbox" type="search" placeholder="'+esc(x.search)+'" aria-label="'+esc(x.search)+'" value="'+esc(query)+'"><div class="chip-group" id="topicFilters"><button class="chip '+(filter==="all"?"active":"")+'" data-filter="all">'+esc(x.all)+' · 20</button><button class="chip '+(filter==="fund"?"active":"")+'" data-filter="fund">'+esc(x.fund)+' · 15</button><button class="chip '+(filter==="tech"?"active":"")+'" data-filter="tech">'+esc(x.tech)+' · 5</button></div></div><div class="research-grid" id="topicGrid"></div>';
document.getElementById("topicSearch").addEventListener("input",function(){query=this.value;filterGrid();});
document.getElementById("topicFilters").addEventListener("click",function(e){const button=e.target.closest("button[data-filter]");if(!button)return;filter=button.dataset.filter;this.querySelectorAll("button").forEach(function(b){b.classList.toggle("active",b===button);});filterGrid();});
filterGrid();
}
function filterGrid(){
const q=query.trim().toLocaleLowerCase(),x=labels();
const list=TOPICS.filter(function(item){return (filter==="all"||(filter==="fund"?item[0].startsWith("01-"):item[0].startsWith("02-"))) && (!q||item.slice(1,7).join(" ").toLocaleLowerCase().includes(q));});
const node=document.getElementById("topicGrid");
if(node)node.innerHTML=list.length?list.map(topicCard).join(""):'<div class="notice">'+esc(x.noresults)+'</div>';
}
function figures(){
const x=labels();
const rows=[["income","42,383.72","51,310.49"],["profit","+1,694.15","+3,371.26"],["owner","−280.42","+973.77"],["cfo","+427.54","−851.24"],["debt","14,797.33","17,324.26"],["cash","27.89","32.07"]];
let h='<div class="panel table-scroll"><table class="financial-table"><thead><tr><th>'+esc(x.metric)+' · LKR mn</th><th>'+esc(x.period25)+'</th><th>'+esc(x.period26)+'</th></tr></thead><tbody>';
rows.forEach(function(r){h+='<tr><td>'+esc(x[r[0]])+'</td>'+r.slice(1).map(function(v){return '<td class="'+(v.includes("−")?"neg":v.includes("+")?"pos":"")+'">'+esc(v)+'</td>';}).join("")+'</tr>';});
return h+'</tbody></table></div>';
}
function financials(){
const x=labels(),l=state.lang,path=(l==="en"?"":l+"/")+"01-Fundamental-Analysis/02-Financial-Statements/";
let h=crumbs(x.financials)+'<div class="page-kicker"><span class="kicker-line"></span>FINANCIAL EVIDENCE · SCAP.N0000</div><h1 class="page-title">'+esc(x.snapshot)+'</h1><p class="page-description">'+esc(x.notes)+'</p><div class="badge-row"><span class="pill mint">'+esc(x.period25)+'</span><span class="pill gold">'+esc(x.period26)+'</span></div>';
h+=section(x.snapshot,"LKR million · SCAP Group unless parent labelled",x.visual,url("report",l,path+"VISUAL-REPORT.md"));
h+=figures()+'<div class="insight"><span class="insight-icon">!</span><div><strong>'+esc(x.sourceNotice)+'</strong><p>'+esc(x.notes)+'</p></div></div>';
h+=section(x.explainer,x.insightP)+'<div class="method-steps">';
x.explain.forEach(function(a,i){h+='<div class="panel step"><span class="step-n">0'+(i+1)+'</span><h3>'+esc(a)+'</h3><p>'+esc(x.explainP[i])+'</p></div>';});
h+='</div><div class="quick-actions" style="margin-top:23px">'+linkButton(x.financials,"report",path+"README.md","btn-primary")+linkButton(x.visual,"report",path+"VISUAL-REPORT.md")+linkButton(x.sources,"sources")+'</div>';
return h;
}
function sources(){
const x=labels(),l=state.lang;
let h=crumbs(x.sources)+'<div class="page-kicker"><span class="kicker-line"></span>PROVENANCE · CSE / ISSUER SOURCES</div><h1 class="page-title">'+esc(x.sources)+'</h1><p class="page-description">'+esc(x.sourceDesc)+'</p><div class="notice"><strong>'+esc(x.sourceNotice)+'</strong><br>'+esc(x.notes)+'</div>';
h+=section(x.records,x.sourceDesc,x.sourceRegister,url("report",l,"sources/SOURCE-REGISTER.md"));
h+='<div class="source-list">';
if(sourceRecords.length)sourceRecords.forEach(function(r){h+='<a class="panel source-card" href="'+url("report",l,r.path)+'"><span class="s-icon">◫</span><span><strong>'+esc(r.title)+'</strong><small>'+esc(r.id)+' · '+esc(x.records)+' ↗</small></span></a>';});
else h+='<a class="panel source-card" href="'+url("report",l,"sources/SOURCE-REGISTER.md")+'">'+esc(x.sourceRegister)+' ↗</a>';
h+='</div><div class="quick-actions" style="margin-top:22px">'+linkButton(x.queue,"report",(l==="en"?"":l+"/")+"RESEARCH-QUEUE.md")+linkButton(x.research,"research")+'</div>';
return h;
}
function reportHeading(doc){
const item=TOPICS.find(function(t){return doc.includes(t[0]+"/");});
if(item)return title(item,state.lang)+(doc.endsWith("VISUAL-REPORT.md")?" / Visual report":doc.endsWith("SWOT-ANALYSIS.md")?" / SWOT":"");
return doc.split("/").pop().replace(/\.md$/,"").replace(/-/g," ");
}
function translatePath(doc,lang){
if(doc.startsWith("sources/"))return doc;
const core=doc.replace(/^(ta|si)\//,"");
if(core.startsWith("01-")||core.startsWith("02-")||["README.md","RESEARCH-QUEUE.md","RESEARCH-LOG.md","SOURCES.md"].includes(core))return (lang==="en"?"":lang+"/")+core;
return doc;
}
function rewriteLinks(element,doc){
element.querySelectorAll("a[href]").forEach(function(a){
const href=a.getAttribute("href");if(!href||href.startsWith("#")||href.startsWith("mailto:"))return;
let dest="";
if(href.startsWith(REPO+"blob/main/"))dest=decodeURIComponent(href.split("/blob/main/")[1].split("#")[0]);
else if(!/^[a-z]+:\/\//i.test(href)){
 try{dest=decodeURIComponent(new URL(href,rawDoc(doc)).pathname.split("/main/")[1]||"");}catch(e){dest="";}
}
if(pathIsSafe(dest)){
const hash=href.includes("#")?"#"+href.split("#").slice(1).join("#"):"";
a.href=url("report",langOf(dest),dest)+hash;
a.removeAttribute("target");
}else if(/^https?:\/\//.test(href)){a.target="_blank";a.rel="noopener noreferrer";}
});
element.querySelectorAll("h1,h2,h3,h4").forEach(function(h){
if(h.id)return;
const slug=h.textContent.trim().toLowerCase().replace(/[^\p{L}\p{N}\s-]/gu,"").replace(/\s+/g,"-").replace(/-+/g,"-");
if(slug)h.id=slug;
});
}
async function renderMermaid(body){
const diagrams=[];
body.querySelectorAll("pre code.language-mermaid").forEach(function(code){
const div=document.createElement("div");
div.className="mermaid";div.textContent=code.textContent;
div.setAttribute("role","img");div.setAttribute("aria-label","Research diagram");
code.closest("pre").replaceWith(div);diagrams.push(div);
});
if(!diagrams.length)return;
try{
if(!mermaidLoader)mermaidLoader=import("https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs");
const mod=await mermaidLoader,mermaid=mod.default;
mermaid.initialize({startOnLoad:false,securityLevel:"strict",theme:document.documentElement.dataset.theme==="light"?"default":"dark",flowchart:{useMaxWidth:true,htmlLabels:true}});
await mermaid.run({nodes:diagrams});
}catch(e){
console.warn("Diagram display not available",e);
diagrams.forEach(function(node){if(node.querySelector("svg"))return;const pre=document.createElement("pre");pre.textContent=node.textContent;node.replaceWith(pre);});
}
}
async function report(doc){
const x=labels(),heading=reportHeading(doc);
MAIN.innerHTML=crumbs(x.research)+'<div class="reader-header"><div><div class="page-kicker"><span class="kicker-line"></span>'+esc(x.viewer)+'</div><h1 class="page-title">'+esc(heading)+'</h1><div class="research-meta">◉ GitHub main · '+esc(state.lang.toUpperCase())+'</div></div><div class="reader-tools"><a class="btn" target="_blank" rel="noopener noreferrer" href="'+githubDoc(doc)+'">'+esc(x.openGitHub)+'</a></div></div><div class="reader-panel"><article class="report-body" id="reportBody"><div class="loading-placeholder"><span class="spinner"></span>'+esc(x.load)+'</div></article></div><div class="doc-footer"><span>'+esc(x.notes)+'</span><a class="section-link" target="_blank" rel="noopener noreferrer" href="'+githubDoc(doc)+'">'+esc(x.openGitHub)+'</a></div>';
const area=document.getElementById("reportBody");
try{
 const response=await fetch(rawDoc(doc),{cache:"no-store"});
 if(!response.ok)throw new Error("HTTP "+response.status);
 const markdown=await response.text();
 if(!state||state.doc!==doc)return;
 if(!window.marked||!window.DOMPurify)throw new Error("Markdown reader library unavailable");
 area.innerHTML=window.DOMPurify.sanitize(window.marked.parse(markdown,{gfm:true}),{USE_PROFILES:{html:true}});
 rewriteLinks(area,doc);
 await renderMermaid(area);
 if(location.hash){const anchor=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(anchor)anchor.scrollIntoView();}
}catch(e){
area.innerHTML='<div class="error-block"><strong>'+esc(x.fail)+'</strong><p>'+esc(e.message)+'</p><a class="btn btn-primary" target="_blank" rel="noopener noreferrer" href="'+githubDoc(doc)+'">'+esc(x.openGitHub)+'</a></div>';
}
}
function render(){
state=parseRoute();
SELECT.value=state.lang;
document.documentElement.lang=state.lang==="ta"?"ta-LK":state.lang==="si"?"si-LK":"en";
sidebar();
document.querySelectorAll(".top-nav a[data-nav]").forEach(function(a){a.classList.toggle("active",a.dataset.nav===(state.view==="report"?"research":state.view));});
if(state.view==="overview")MAIN.innerHTML=home();
if(state.view==="research")library();
if(state.view==="financials")MAIN.innerHTML=financials();
if(state.view==="sources")MAIN.innerHTML=sources();
if(state.view==="report")report(state.doc);
document.title=(state.view==="report"?reportHeading(state.doc):state.view==="overview"?"SCAP Research":state.view==="financials"?labels().financials:state.view==="sources"?labels().sources:labels().research)+" · Softlogic Capital";
closeMobile();
}
function navigate(href){
const next=new URL(href,location.href);
if(next.origin!==location.origin||next.pathname!==location.pathname){location.href=href;return;}
history.pushState({}, "",next.pathname+next.search+next.hash);
window.scrollTo(0,0);render();
}
function parseSourceList(md){
const list=[];
md.split("\n").forEach(function(row){
const id=row.match(/^\|\s*\x60([^\x60]+)\x60\s*\|/);
const path=row.match(/\[View evidence\]\((records\/[^)]+)\)/);
if(!id||!path)return;
const m=row.match(/\|\s*\x60[^\x60]+\x60\s*\|\s*\[([^\]]+)\]\(/);
list.push({id:id[1],title:m?m[1]:id[1],path:"sources/"+path[1]});
});
return list;
}
async function sync(){
try{
 const fetched=await Promise.all([fetch(rawDoc("RESEARCH-QUEUE.md"),{cache:"no-store"}),fetch(rawDoc("sources/SOURCE-REGISTER.md"),{cache:"no-store"})]);
 if(fetched[0].ok){
  const data=await fetched[0].text();
  data.split("\n").forEach(function(line){
   const m=line.match(/^\|\s*\[[^\]]+\]\(([^)]+)\/README\.md\)\s*\|\s*\*\*(PARTIAL|TEMPLATE|FILLED)/);
   if(m)TOPIC_STATUS[m[1]]=m[2];
  });
 }
 if(fetched[1].ok)sourceRecords=parseSourceList(await fetched[1].text());
 render();
}catch(e){console.info("Research sync unavailable; showing cached overview",e);}
}
SELECT.addEventListener("change",function(){const l=SELECT.value;if(state.view==="report"&&state.doc)navigate(url("report",l,translatePath(state.doc,l)));else navigate(url(state.view,l));});
document.getElementById("mobileMenu").addEventListener("click",function(){const v=SIDEBAR.classList.toggle("is-open");this.setAttribute("aria-expanded",v?"true":"false");});
document.getElementById("themeToggle").addEventListener("click",function(){
const theme=document.documentElement.dataset.theme==="dark"?"light":"dark";
document.documentElement.dataset.theme=theme;
try{localStorage.setItem("scap-theme",theme);}catch(e){}
if(state.view==="report"&&MAIN.querySelector(".mermaid"))report(state.doc);
});
document.addEventListener("click",function(event){
const a=event.target.closest("a[href]");
if(!a||event.button!==0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey||a.target==="_blank")return;
const ref=a.getAttribute("href");
if(ref&&ref.startsWith("?view=")){event.preventDefault();navigate(ref);}
});
window.addEventListener("popstate",render);
try{const saved=localStorage.getItem("scap-theme");if(saved==="light"||saved==="dark")document.documentElement.dataset.theme=saved;}catch(e){}
render();
sync();
})();