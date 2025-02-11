const USE_PRODUCTION = false
export const PROD_API_URL = 'http://ec2-54-232-129-81.sa-east-1.compute.amazonaws.com:5000'
export const DEV_API_URL = 'http://localhost:5000'
export const API_URL = USE_PRODUCTION ? PROD_API_URL : DEV_API_URL