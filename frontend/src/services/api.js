import axios from "axios";

const API = axios.create({
  baseURL: "codereviewer-production-9852.up.railway.app",
});

export default API;