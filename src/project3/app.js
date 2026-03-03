function $(id){ return document.getElementById(id); }

const baseUrlEl = $("baseUrl");
const pingBtn = $("pingBtn");
const statusEl = $("status");

const methodEl = $("method");
const pathEl = $("path");
const bodyEl = $("body");
const sendBtn = $("sendBtn");

const outputEl = $("output");

function cleanBaseUrl(){
  return (baseUrlEl.value || "").trim().replace(/\/+$/, "");
}

function fullUrl(path){
  const base = cleanBaseUrl();
  const p = (path || "").trim();
  if(!base) return "";
  if(!p) return base;
  return p.startsWith("/") ? base + p : base + "/" + p;
}

function show(obj){
  try{
    outputEl.textContent = JSON.stringify(obj, null, 2);
  }catch(e){
    outputEl.textContent = String(obj);
  }
}

async function request(method, path, bodyObj){
  const url = fullUrl(path);
  if(!url){
    show({ error: "Missing Base URL or Path" });
    return;
  }

  const opts = { method, headers: { "Content-Type": "application/json" } };

  if(method === "POST" || method === "PUT"){
    opts.body = JSON.stringify(bodyObj || {});
  }

  outputEl.textContent = "Loading...";

  try{
    const res = await fetch(url, opts);
    const text = await res.text();

    let data = text;
    try{ data = JSON.parse(text); } catch(e){}

    show({
      ok: res.ok,
      status: res.status,
      url,
      method,
      data
    });

    statusEl.textContent = res.ok ? "Request success ✅" : "Request failed (but server responded) ⚠️";
  }catch(err){
    show({ error: "Network error", detail: String(err), url });
    statusEl.textContent = "Network error ❌ (is API running? CORS?)";
  }
}

pingBtn.addEventListener("click", async () => {
  // easiest ping is GET /users?limit=1 (since we know it exists)
  await request("GET", "/users?limit=1");
});

sendBtn.addEventListener("click", async () => {
  const method = methodEl.value;
  const path = pathEl.value.trim();

  let bodyObj = {};
  if(method === "POST" || method === "PUT"){
    const raw = bodyEl.value.trim();
    if(raw){
      try{
        bodyObj = JSON.parse(raw);
      }catch(e){
        show({ error: "Body must be valid JSON", detail: String(e) });
        return;
      }
    }
  }

  await request(method, path, bodyObj);
});

// Quick buttons (data-path)
document.querySelectorAll("[data-path]").forEach(btn => {
  btn.addEventListener("click", async () => {
    const path = btn.getAttribute("data-path");
    await request("GET", path);
  });
});