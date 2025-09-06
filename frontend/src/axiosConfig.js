import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000",
  withCredentials: true,
});

const setupCSRF = async () => {
  try {
    const res = await axiosInstance.get("/api/get_csrf_token/");
    axiosInstance.defaults.headers.common["X-CSRFToken"] = res.data.csrfToken;
  } catch (err) {
    console.error("CSRF setup failed", err);
  }
};

setupCSRF(); // run immediately

export default axiosInstance;
