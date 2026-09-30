# 🍃 AeroPulse (Keeladi Edition)

> **Street-Level Urban Air Quality Intelligence Powered by Ancient Keezhadi Wind-Flow Principles & Google Gemini 2.5 LLM**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Google GenAI SDK](https://img.shields.io/badge/Google_GenAI-Gemini_2.5_Flash-4285F4.svg?logo=google&logoColor=white)](https://ai.google.dev/)
[![Render](https://img.shields.io/badge/Deploy-Render-46E3B7.svg?logo=render&logoColor=white)](https://render.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🏛️ Project Vision & Archaeological Heritage

Traditional air monitoring relies on distant regional weather stations spaced 15–25 km apart. They are blind to the toxic microclimates trapped inside dense urban street canyons at pedestrian breathing level.

**AeroPulse (Keeladi Edition)** maps invisible gases down to a **10-meter block level** and predicts atmospheric stagnation **24 to 48 hours in advance**. The platform takes inspiration from the 2,600-year-old Sangam civilization excavated at **Keezhadi (Keeladi, Tamil Nadu, c. 6th century BCE)**:
* **Cardinal Grid Aerodynamics:** Keezhadi's orthogonal avenues were oriented with cardinal axes to channel prevailing Southwest and Northeast monsoonal wind vectors into laminar cleansing streams.
* **Mutram Stack Buoyancy:** Open residential courtyards generated thermal chimney effects, venting warm particulate-laden air vertically.
* **Contrast with Modern Sprawl:** Deep, asymmetric concrete urban canyons ($H/W > 2.5$) generate skimming-flow vortex traps where vehicular PM2.5 and NO₂ accumulate to hazardous levels.

---

## 🚀 Core Features

1. **Hero Intelligence Section:** Contrasts traditional trapped urban air pollution with ancient architectural wisdom.
2. **Interactive 10-Meter Block Grid Map:** Hyperlocal polygon grid rendering PM2.5, PM10, NO₂, CO, composite AQI, and aerodynamic ventilation coefficients ($C_v$) with real-time inspection.
3. **Keezhadi Sandbox Simulator:** Real-time 2D Canvas physics wind tunnel simulating smoke particle dispersion in **Modern Canyons**, **Keezhadi Cardinal Grids**, and **Hybrid Retrofits** with adjustable wind speed, compass angle, and emission load.
4. **Predictive 24–48h Early Warnings:** Diurnal nocturnal boundary layer inversion modeling (dawn stagnation peaks) and automated executive atmospheric bulletins.
5. **Practical Utilities:**
   - **Citizen View ("BreatheSafe"):** Clean air walking/cycling route calculation showing up to **-58% reduction** in inhaled PM2.5 dosage compared to standard arterial roads.
   - **City Planner View:** Ranked stagnant micro-canyon hotspots with municipal Sangam engineering mitigation playbooks.
6. **Google Gemini 2.5 LLM Integration:**
   - Real-time CFD aerodynamic and architectural critique.
   - 48-Hour Atmospheric Inversion Bulletins.
   - Interactive conversational Copilot trained on Sangam urban layout and street canyon fluid mechanics.

---

## 🛠️ Tech Stack Target

- **Backend:** Python 3.10+ / 3.13, **FastAPI**, **Uvicorn**, **Pydantic**
- **AI / LLM:** Official Google GenAI SDK (`google-genai` 2.0+) using **Gemini 2.5 Flash** (`gemini-2.5-flash`)
- **Frontend:** Responsive Single-Page Application (HTML5, Tailwind CSS, Leaflet.js, Canvas 2D Physics, Chart.js)
- **Deployment:** **Render** (`render.yaml` Blueprint or Dockerfile / Procfile)

---

## 🌐 Local Setup & Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/priyu210824/AeroPulse.git
cd AeroPulse
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. (Optional) Set your Google Gemini API Key
Create a `.env` file in the root folder:
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
PORT=8000
```
*(Note: You can also launch without a key and paste it directly into the web UI settings modal!)*

### 4. Run the server
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Open your browser at **`http://localhost:8000`** to experience AeroPulse!

---

## ☁️ Deploying on Render in 2 Minutes

### Method A: 1-Click Blueprint (Recommended)
1. Fork or push this repository to your GitHub account: `https://github.com/priyu210824/AeroPulse.git`.
2. Log into [Render.com](https://render.com).
3. Click **New +** &rarr; **Blueprint**.
4. Connect the `AeroPulse` repository. Render will automatically read `render.yaml`:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Under Environment Variables, add:
   - `GEMINI_API_KEY`: *(Your Google Gemini API Key)*
6. Click **Apply**. Your live URL (e.g. `https://aeropulse-keeladi.onrender.com`) will be online in under 90 seconds!

### Method B: Manual Web Service on Render
1. Click **New +** &rarr; **Web Service**.
2. Select repository `AeroPulse`.
3. Choose **Python** runtime.
4. Set Build Command: `pip install -r requirements.txt`
5. Set Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add `GEMINI_API_KEY` in Environment Variables and hit **Create Web Service**.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Web application single-page interface |
| `GET` | `/api/status` | System health check and Gemini configuration status |
| `POST` | `/api/set-api-key` | Dynamically update Google Gemini API key in session |
| `GET` | `/api/blocks` | 10-meter block grid GeoJSON with real-time telemetry |
| `GET` | `/api/forecast` | 24-48 hour predictive timeline & early warning alerts |
| `POST` | `/api/route` | BreatheSafe Clean Air Route vs Highway Exposure Path |
| `POST` | `/api/gemini/chat` | Conversational assistant powered by Gemini 2.5 Flash |
| `POST` | `/api/gemini/analyze-simulator` | Aerodynamic CFD critique of the sandbox simulator |
| `POST` | `/api/gemini/forecast-report` | Executive atmospheric early warning bulletin |
| `POST` | `/api/gemini/planner-mitigation` | Municipal engineering interventions for hotspots |

---

## 🏛️ Sangam Heritage References
- Archaeological Survey of India (ASI) Keezhadi Excavation Reports.
- Sangam Literature (*Maduraikkāñci* & *Purananuru* on ancient town layouts along the Vaigai).
- Oke, T. R. (1988). *Street design and urban canopy layer climate*.
