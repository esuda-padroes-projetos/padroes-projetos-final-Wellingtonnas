// frontend/scripts/utils.js

// URL base da API FastAPI (valor global)
const API_URL = "http://127.0.0.1:8000";

// Função genérica para requisições (global)
async function apiRequest(endpoint, method = "GET", body = null) {
  const options = {
    method,
    headers: { "Content-Type": "application/json" },
  };

  if (body) options.body = JSON.stringify(body);

  try {
    const response = await fetch(`${API_URL}${endpoint}`, options);

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Erro HTTP ${response.status}: ${errorText}`);
    }

    // Se não houver conteúdo (204), retornar null
    if (response.status === 204) return null;

    return await response.json();
  } catch (error) {
    console.error("❌ Erro na requisição:", error);
    throw error;
  }
}

// Helpers simples
function showMessage(msg) {
  alert(msg);
}
