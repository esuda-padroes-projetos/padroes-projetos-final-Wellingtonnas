// frontend/scripts/api.js
const API_BASE = "http://127.0.0.1:8000"; // seu backend

async function apiGet(endpoint) {
  return apiRequest(endpoint, "GET");
}

async function apiPost(endpoint, data) {
  return apiRequest(endpoint, "POST", data);
}

async function apiPut(endpoint, data) {
  return apiRequest(endpoint, "PUT", data);
}

async function apiDelete(endpoint) {
  return apiRequest(endpoint, "DELETE", null);
}
