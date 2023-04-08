const PROD_BACKEND_API_URL = "https://shopping_center_app.strangled.net/app1/";
const DEV_BACKEND_API_URL = "http://127.0.0.1:8000/app1/";

export const BACKEND_API_URL =
	process.env.NODE_ENV === "development" ? DEV_BACKEND_API_URL : PROD_BACKEND_API_URL;