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
  }catch(err){
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

function renderObjectTable(obj){
  let rows = "";

  Object.keys(obj).forEach(key => {
    rows += `
      <tr>
        <th>${escapeHtml(key)}</th>
        <td>${formatValue(obj[key])}</td>
      </tr>
    `;
  });

  return `
    <div class="result-card">
      <h3>Record Details</h3>
      <table class="result-table">
        <tbody>${rows}</tbody>
      </table>
    </div>
  `;
}

function renderArrayTable(arr){
  if(!arr.length){
    return `
      <div class="result-card">
        <h3>Results</h3>
        <p class="result-message">No records were returned.</p>
      </div>
    `;
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
        <h3>Results</h3>
        <p class="result-message">${escapeHtml(JSON.stringify(arr))}</p>
      </div>
    `;
  }

  const head = keys.map(key => `<th>${escapeHtml(key)}</th>`).join("");

  const body = arr.map(item => {
    const cells = keys.map(key => `<td>${formatValue(item[key])}</td>`).join("");
    return `<tr>${cells}</tr>`;
  }).join("");

  return `
    <div class="result-card">
      <h3>Results (${arr.length} record${arr.length === 1 ? "" : "s"})</h3>
      <table class="result-table">
        <thead>
          <tr>${head}</tr>
        </thead>
        <tbody>
          ${body}
        </tbody>
      </table>
    </div>
  `;
}

function renderPrettyResponse(payload){
  if(!payload){
    prettyOutputEl.innerHTML = `<div class="empty-state">No results yet.</div>`;
    return;
  }

  if(payload.error){
    prettyOutputEl.innerHTML = `
      <div class="result-card">
        <h3>Request Error</h3>
        <p class="result-message error">${escapeHtml(payload.error)}</p>
        ${payload.detail ? `<p class="result-message">${escapeHtml(payload.detail)}</p>` : ""}
      </div>
    `;
    return;
  }

  const summary = `
    <div class="result-summary">
      <div class="summary-box">
        <div class="label">Method</div>
        <div class="value">${escapeHtml(payload.method || "")}</div>
      </div>
      <div class="summary-box">
        <div class="label">Status</div>
        <div class="value">${escapeHtml(payload.status || "")}</div>
      </div>
      <div class="summary-box">
        <div class="label">Path</div>
        <div class="value">${escapeHtml(payload.path || "")}</div>
      </div>
    </div>
  `;

  let content = summary;
  const data = payload.data;

  if(Array.isArray(data)){
    content += renderArrayTable(data);
  } else if(isPlainObject(data)){
    content += renderObjectTable(data);
  } else {
    content += `
      <div class="result-card">
        <h3>Result</h3>
        <p class="result-message">${formatValue(data)}</p>
      </div>
    `;
  }

  prettyOutputEl.innerHTML = content;
}

async function request(method, path, bodyObj){
  const url = fullUrl(path);

  if(!url){
    const errObj = { error: "Missing Base URL or Path" };
    showRaw(errObj);
    renderPrettyResponse(errObj);
    statusEl.innerHTML = `<span class="error">Missing Base URL or path.</span>`;
    return;
  }

  const options = {
    method,
    headers: {
      "Content-Type": "application/json"
    }
  };

  if(method === "POST" || method === "PUT"){
    options.body = JSON.stringify(bodyObj || {});
  }

  outputEl.textContent = "Loading...";
  prettyOutputEl.innerHTML = `<div class="empty-state">Loading...</div>`;

  try{
    const response = await fetch(url, options);
    const text = await response.text();

    let data = text;
    try{
      data = JSON.parse(text);
    }catch(err){
      // keep text
    }

    const result = {
      ok: response.ok,
      status: response.status,
      path,
      method,
      data
    };

    showRaw(result);
    renderPrettyResponse(result);

    if(response.ok){
      statusEl.innerHTML = `<span class="success">Request successful ✅</span>`;
    } else {
      statusEl.innerHTML = `<span class="error">Request failed, but the server responded.</span>`;
    }
  } catch(err){
    const errObj = {
      error: "Network error",
      detail: String(err)
    };

    showRaw(errObj);
    renderPrettyResponse(errObj);
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
      } catch(err){
        const errObj = {
          error: "Body must be valid JSON",
          detail: String(err)
        };
        showRaw(errObj);
        renderPrettyResponse(errObj);
        statusEl.innerHTML = `<span class="error">Body must be valid JSON.</span>`;
        return;
      }
    }
  }

  await request(method, path, bodyObj);
});

document.querySelectorAll("[data-path]").forEach(button => {
  button.addEventListener("click", async () => {
    const path = button.getAttribute("data-path");
    await request("GET", path);
  });
});