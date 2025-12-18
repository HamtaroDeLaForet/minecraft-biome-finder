from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from api import get_biomes_mock
from utils import find_nearest_biome

app = FastAPI(title="Minecraft Bedrock Biome Finder")

# Autoriser le frontend React en dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/nearest-biome")
def nearest_biome(
    seed: int = Query(..., description="Seed de la map Bedrock"),
    x: int = Query(..., description="Coordonnée X du joueur"),
    z: int = Query(..., description="Coordonnée Z du joueur"),
    biome: str = Query(..., description="Nom du biome recherché")
):
    # Pour l'instant, on utilise le mock
    biomes = get_biomes_mock(seed)
    nearest, dist = find_nearest_biome(x, z, biome.upper(), biomes)

    if nearest is None:
        return {"error": f"Biome {biome} non trouvé."}

    return {
        "biome": nearest["name"],
        "coords": {"x": nearest["x"], "z": nearest["z"]},
        "distance": dist
    }
