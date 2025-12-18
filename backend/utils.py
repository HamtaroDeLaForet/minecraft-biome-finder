import math

def distance(x1: int, z1: int, x2: int, z2: int) -> float:
    """Calcule la distance euclidienne entre deux points X/Z."""
    return math.sqrt((x2 - x1)**2 + (z2 - z1)**2)

def find_nearest_biome(player_x: int, player_z: int, target_biome: str, biomes: list):
    """
    Trouve le biome le plus proche parmi une liste de biomes.
    biomes = [{"name": "DESERT", "x": 100, "z": -50}, ...]
    """
    nearest = None
    min_dist = float("inf")
    for b in biomes:
        if b["name"] == target_biome:
            d = distance(player_x, player_z, b["x"], b["z"])
            if d < min_dist:
                min_dist = d
                nearest = b
    return nearest, round(min_dist)
