from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class SetApiKeyRequest(BaseModel):
    api_key: str = Field(..., description="Google Gemini API key")

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = Field(default_factory=list)

class SimulatorCritiqueRequest(BaseModel):
    scenario: str
    wind_speed: float
    wind_direction_deg: float
    emission_rate: float
    evacuation_rate: float
    stagnation_index: float

class MitigationRequest(BaseModel):
    block_id: str
    canyon_hw: float
    aqi: int
    dominant_pollutant: str
    cv_ventilation: float

class RouteRequest(BaseModel):
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    transport_mode: Optional[str] = "walking"
