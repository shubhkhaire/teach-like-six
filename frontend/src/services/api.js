import axios from "axios";

const BACKEND = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

export async function createExplainer(topic, { include_image = true, include_voice = false } = {}) {
  const payload = { topic, include_image, include_voice };
  const res = await axios.post(`${BACKEND}/explain`, payload, { timeout: 120000 });
  return res.data;
}
