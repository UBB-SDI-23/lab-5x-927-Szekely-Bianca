const PROD_BACKEND_API_URL = "/app1";
const DEV_BACKEND_API_URL = "http://ec2-13-50-13-122.eu-north-1.compute.amazonaws.com/app1";
export const BACKEND_API_URL =
	process.env.NODE_ENV === "development" ? DEV_BACKEND_API_URL : PROD_BACKEND_API_URL;
 //export const BACKEND_API_URL = "http://ec2-13-53-45-100.eu-north-1.compute.amazonaws.com/app1";
///app1/* http://ec2-16-16-91-55.eu-north-1.compute.amazonaws.com/:splat 200!