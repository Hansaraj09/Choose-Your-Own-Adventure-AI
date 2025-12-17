// export const API_BASE_URL = "/api" 
export const API_BASE_URL =
  import.meta.env.VITE_DEBUG === "true"
    ? "/api"
    : `${import.meta.env.VITE_API_URL}/api`;
