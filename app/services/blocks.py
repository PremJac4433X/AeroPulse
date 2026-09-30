import random
from typing import Dict, Any, List

# Center coordinates: Ancient Vaigai / Keezhadi Urban Corridor (Madurai region)
BASE_LAT = 9.8625
BASE_LON = 78.1820
BLOCK_SIZE = 0.00035  # ~10 meters in latitude/longitude degrees

def generate_blocks() -> Dict[str, Any]:
    """
    Generates a 10-meter block grid GeoJSON FeatureCollection
    comparing Modern Asymmetric Canyons, Hybrid Retrofits,
    and Keezhadi Cardinal Grids.
    """
    features: List[Dict[str, Any]] = []
    
    rows = 8
    cols = 8
    
    typologies = [
        {
            "type": "Modern Concrete Canyon",
            "hw_range": (2.6, 3.8),
            "cv_range": (0.10, 0.25),
            "pm25_range": (145.0, 220.0),
            "no2_range": (65.0, 98.0),
            "co_range": (2.8, 4.5),
            "note": "Deep asymmetric canyon trapping vehicular exhaust in vortex recirculations."
        },
        {
            "type": "Sangam Cardinal Grid Avenue",
            "hw_range": (0.6, 1.1),
            "cv_range": (0.75, 0.92),
            "pm25_range": (28.0, 52.0),
            "no2_range": (12.0, 24.0),
            "co_range": (0.4, 0.9),
            "note": "Keezhadi orthogonal avenue oriented along SW-NE monsoon vector for continuous laminar purging."
        },
        {
            "type": "Mutram Courtyard Cluster",
            "hw_range": (1.2, 1.8),
            "cv_range": (0.55, 0.72),
            "pm25_range": (42.0, 68.0),
            "no2_range": (18.0, 32.0),
            "co_range": (0.6, 1.2),
            "note": "Central open courtyard stacks generating thermal buoyant chimneys venting warm particulate air."
        },
        {
            "type": "Hybrid Retrofit Breezeway",
            "hw_range": (1.4, 2.0),
            "cv_range": (0.62, 0.80),
            "pm25_range": (45.0, 75.0),
            "no2_range": (20.0, 36.0),
            "co_range": (0.7, 1.4),
            "note": "Modern building with carved ground-floor wind apertures and porous green vertical screens."
        },
        {
            "type": "Arterial Highway Choke",
            "hw_range": (1.8, 2.5),
            "cv_range": (0.18, 0.35),
            "pm25_range": (180.0, 260.0),
            "no2_range": (80.0, 125.0),
            "co_range": (3.2, 5.8),
            "note": "High vehicular throughput with stagnant boundary eddies between commercial billboards."
        }
    ]
    
    # Pre-determined layout pattern for coherent visualization
    for r in range(rows):
        for c in range(cols):
            block_id = f"BLK-{chr(65+r)}{c+1}"
            
            # Select typology based on coordinate regions
            if c in (3, 4):  # Central cardinal spine (Sangam corridor)
                typo = typologies[1]
            elif r in (0, 1) and c < 3:  # Arterial highway
                typo = typologies[4]
            elif r >= 4 and c >= 4:  # Mutram Courtyards
                typo = typologies[2]
            elif (r + c) % 3 == 0:  # Hybrid retrofits
                typo = typologies[3]
            else:  # Modern dense canyons
                typo = typologies[0]
                
            lat_start = BASE_LAT + (r * BLOCK_SIZE)
            lon_start = BASE_LON + (c * BLOCK_SIZE)
            
            # Polygon coordinates: [lon, lat]
            poly_coords = [
                [lon_start, lat_start],
                [lon_start + BLOCK_SIZE * 0.94, lat_start],
                [lon_start + BLOCK_SIZE * 0.94, lat_start + BLOCK_SIZE * 0.94],
                [lon_start, lat_start + BLOCK_SIZE * 0.94],
                [lon_start, lat_start]
            ]
            
            pm25 = round(random.uniform(*typo["pm25_range"]), 1)
            no2 = round(random.uniform(*typo["no2_range"]), 1)
            co = round(random.uniform(*typo["co_range"]), 2)
            pm10 = round(pm25 * random.uniform(1.6, 2.1), 1)
            hw = round(random.uniform(*typo["hw_range"]), 2)
            cv = round(random.uniform(*typo["cv_range"]), 2)
            
            # Compute composite AQI roughly based on PM2.5 standard
            if pm25 <= 30:
                aqi = int(pm25 * (50 / 30))
                risk = "Low"
            elif pm25 <= 60:
                aqi = int(50 + (pm25 - 30) * (50 / 30))
                risk = "Moderate"
            elif pm25 <= 120:
                aqi = int(100 + (pm25 - 60) * (100 / 60))
                risk = "High"
            else:
                aqi = int(200 + (pm25 - 120) * (150 / 130))
                risk = "Severe"
                
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [poly_coords]
                },
                "properties": {
                    "id": block_id,
                    "name": f"{typo['type']} ({block_id})",
                    "typology": typo["type"],
                    "aqi": aqi,
                    "pm25": pm25,
                    "pm10": pm10,
                    "no2": no2,
                    "co": co,
                    "cv_ventilation": cv,
                    "canyon_hw": hw,
                    "stagnation_risk": risk,
                    "archaeological_note": typo["note"],
                    "center": [lat_start + BLOCK_SIZE * 0.47, lon_start + BLOCK_SIZE * 0.47]
                }
            })
            
    return {
        "type": "FeatureCollection",
        "metadata": {
            "center": [BASE_LAT + (rows * BLOCK_SIZE / 2), BASE_LON + (cols * BLOCK_SIZE / 2)],
            "resolution": "10-meter block grid",
            "region": "Vaigai Ancient Corridor & Modern Madurai Sector",
            "total_blocks": len(features)
        },
        "features": features
    }
