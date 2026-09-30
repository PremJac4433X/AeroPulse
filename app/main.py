import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from app.services.models import (
    SetApiKeyRequest,
    ChatRequest,
    SimulatorCritiqueRequest,
    MitigationRequest,
    RouteRequest
)
from app.services.blocks import generate_blocks
from app.services.forecast import get_forecast_48h
from app.services.routes import calculate_breathe_safe_route
from app.services.gemini import (
    get_effective_api_key,
    set_effective_api_key,
    is_gemini_ready,
    generate_chat_response,
    analyze_simulator_cfd,
    generate_forecast_bulletin,
    generate_mitigation_plan
)

app = FastAPI(
    title="AeroPulse (Keeladi Edition)",
    description="Street-Level Urban Air Quality Intelligence Powered by Ancient Keezhadi Wind-Flow Principles & Google Gemini 2.5 LLM",
    version="1.0.0"
)

# Static and Templates
static_dir = os.path.join(os.path.dirname(__file__), "static")
templates_dir = os.path.join(os.path.dirname(__file__), "templates")

if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "gemini_ready": is_gemini_ready(),
            "model_name": "gemini-2.5-flash"
        }
    )

@app.get("/api/status")
async def get_system_status():
    return {
        "status": "online",
        "app_name": "AeroPulse (Keeladi Edition)",
        "version": "1.0.0",
        "gemini_configured": is_gemini_ready(),
        "model": "gemini-2.5-flash",
        "archaeological_site": "Keezhadi (Sivaganga District, Tamil Nadu)",
        "aerodynamic_basis": "Oke (1988) Street Canyon Microclimates & Cardinal Monsoonal Cleansing"
    }

@app.post("/api/set-api-key")
async def set_gemini_api_key(req: SetApiKeyRequest):
    if not req.api_key or len(req.api_key.strip()) < 8:
        return JSONResponse(status_code=400, content={"error": "Invalid API key format"})
    set_effective_api_key(req.api_key.strip())
    return {
        "success": True,
        "message": "Google Gemini API key successfully registered for this session",
        "gemini_configured": True,
        "model": "gemini-2.5-flash"
    }

@app.get("/api/blocks")
async def get_blocks():
    return generate_blocks()

@app.get("/api/forecast")
async def get_forecast():
    return get_forecast_48h()

@app.post("/api/route")
async def calculate_route(req: RouteRequest):
    return calculate_breathe_safe_route(
        start_lat=req.start_lat,
        start_lon=req.start_lon,
        end_lat=req.end_lat,
        end_lon=req.end_lon,
        mode=req.transport_mode or "walking"
    )

@app.post("/api/gemini/chat")
async def gemini_chat(req: ChatRequest):
    reply = await generate_chat_response(req.message, req.history)
    return {"reply": reply, "model": "gemini-2.5-flash"}

@app.post("/api/gemini/analyze-simulator")
async def gemini_simulator_critique(req: SimulatorCritiqueRequest):
    analysis = await analyze_simulator_cfd(req.model_dump())
    return {"critique": analysis, "model": "gemini-2.5-flash"}

@app.post("/api/gemini/forecast-report")
async def gemini_forecast_report():
    forecast_data = get_forecast_48h()
    bulletin = await generate_forecast_bulletin(forecast_data)
    return {"bulletin": bulletin, "model": "gemini-2.5-flash"}

@app.post("/api/gemini/planner-mitigation")
async def gemini_planner_mitigation(req: MitigationRequest):
    playbook = await generate_mitigation_plan(req.model_dump())
    return {"playbook": playbook, "model": "gemini-2.5-flash"}
