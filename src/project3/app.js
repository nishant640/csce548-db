function $(id){ 
  return document.getElementById(id); 
}

const baseUrlEl = $("baseUrl");
const pingBtn = $("pingBtn");
const statusEl = $("status");

const methodEl = $("method");
const pathEl = $("path");
const bodyEl = $("body");
const sendBtn = $("sendBtn");

const outputEl = $("output");
const prettyOutputEl = $("prettyOutput");

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

function escapeHtml(value){
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function showRaw(obj){
  try{
    outputEl.textContent = JSON.stringify(obj, null, 2);
  }catch(e){
    outputEl.textContent = String(obj);
  }
}

function isPlainObject(value){
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function formatValue(value){
  if(value === null || value === undefined) return "N/A";
  if(typeof value === "object") return escapeHtml(JSON.stringify(value));
  return escapeHtml(value);
}

function renderObjectCard(obj, title = "Record"){
  let rows = "";

  for(const key in obj){
    rows += `
      <tr>
        <th>${escapeHtml(key)}</th>
        <td>${formatValue(obj[key])}</td>
      </tr>
    `;
  }

  return `
    <div class="result-card">
      <h3>${escapeHtml(title)}</h3>
      <table class="result-table">
        <tbody>
          ${rows}
        </tbody>
      </table>
    </div>
  `;
}

function renderArrayTable(arr){
  if(!arr.length){
    return `<div class="result-card"><p>No records found.</p></div>`;
  }

  const keys = Array.from(
    arr.reduce((set, item) => {
      if(isPlainObject(item)){
        Object.keys(item).forEach(key => set.add(key));
      }
      return set;
    }, new Set())
  );

  if(!keys.length){
    return `
      <div class="result-card">
        <p>${escapeHtml(JSON.stringify(arr))}</p>
      </div>
    `;
  }

  const headerHtml = keys.map(key => `<th>${escapeHtml(key)}</th>`).join("");

  const bodyHtml = arr.map(item => {
    const cells = keys.map(key => `<td>${formatValue(item[key])}</td>`).join("");
    return `<tr>${cells}</tr>`;
  }).join("");

  return `
    <div class="result-card">
      <h3>Results (${arr.length} record${arr.length === 1 ? "" : "s"})</h3>
      <table class="result-table">
        <thead>
          <tr>${headerHtml}</tr>
        </thead>
        <tbody>
          ${bodyHtml}
        </tbody>
      </table>
    </div>
  `;
}

function renderPrettyResponse(payload){
  if(!payload){
    prettyOutputEl.innerHTML = `<p>No results yet.</p>`;
    return;
  }

  if(payload.error){
    prettyOutputEl.innerHTML = `
      <div class="result-card">
        <p class="error">Error: ${escapeHtml(payload.error)}</p>
        ${payload.detail ? `<p>${escapeHtml(payload.detail)}</p>` : ""}
      </div>
    `;
    return;
  }

  const data = payload.data;

  let content = `
    <div class="result-card">
      <h3>Request Summary</h3>
      <p><strong>Method:</strong> ${escapeHtml(payload.method || "")}</p>
      <p><strong>Status:</strong> ${escapeHtml(payload.status || "")}</p>
      <p><strong>URL:</strong> ${escapeHtml(payload.url || "")}</p>
    </div>
  `;

  if(Array.isArray(data)){
    content += renderArrayTable(data);
  } else if(isPlainObject(data)){
    content += renderObjectCard(data, "Record Details");
  } else {
    content += `
      <div class="result-card">
        <h3>Result</h3>
        <p>${formatValue(data)}</p>
      </div>
    `;
  }

  prettyOutputEl.innerHTML = content;
}

async function request(method, path, bodyObj){
  const url = fullUrl(path);

  if(!url){
    const errorObj = { error: "Missing Base URL or Path" };
    showRaw(errorObj);
    renderPrettyResponse(errorObj);
    return;
  }

  const opts = {
    method,
    headers: { "Content-Type": "application/json" }
  };

  if(method === "POST" || method === "PUT"){
    opts.body = JSON.stringify(bodyObj || {});
  }

  outputEl.textContent = "Loading...";
  prettyOutputEl.innerHTML = `<p>Loading...</p>`;

  try{
    const res = await fetch(url, opts);
    const text = await res.text();

    let data = text;
    try{
      data = JSON.parse(text);
    }catch(e){
      // leave as text
    }

    const result = {
      ok: res.ok,
      status: res.status,
      url,
      method,
      data
    };

    showRaw(result);
    renderPrettyResponse(result);

    if(res.ok){
      statusEl.innerHTML = `<span class="success">Request success ✅</span>`;
    } else {
      statusEl.innerHTML = `<span class="error">Request failed, but the server responded ⚠️</span>`;
    }
  } catch(err){
    const errorObj = {
      error: "Network error",
      detail: String(err),
      url
    };

    showRaw(errorObj);
    renderPrettyResponse(errorObj);
    statusEl.innerHTML = `<span class="error">Network error ❌ Check whether the API is running and whether CORS is enabled.</span>`;
  }
}

pingBtn.addEventListener("click", async () => {
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
        const errorObj = {
          error: "Body must be valid JSON",
          detail: String(e)
        };
        showRaw(errorObj);
        renderPrettyResponse(errorObj);
        return;
      }
    }
  }

  await request(method, path, bodyObj);
});

document.querySelectorAll("[data-path]").forEach(btn => {
  btn.addEventListener("click", async () => {
    const path = btn.getAttribute("data-path");
    await request("GET", path);
  });
});