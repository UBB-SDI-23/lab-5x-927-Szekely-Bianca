const PROD_BACKEND_API_URL = "/app1";
const DEV_BACKEND_API_URL = "http://ec2-16-16-91-55.eu-north-1.compute.amazonaws.com/app1";
export const BACKEND_API_URL =
	process.env.NODE_ENV === "development" ? DEV_BACKEND_API_URL : PROD_BACKEND_API_URL;
// export const BACKEND_API_URL = "http://ec2-16-16-91-55.eu-north-1.compute.amazonaws.com/app1";
