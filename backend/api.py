# Mock des positions de biomes (à remplacer par une vraie API plus tard)
def get_biomes_mock(seed: int):
    """
    Retourne une liste de biomes avec coordonnées fictives.
    """
    return [
        {"name": "DESERT", "x": 120, "z": -300},
        {"name": "PLAINS", "x": 50, "z": 75},
        {"name": "FOREST", "x": -200, "z": 100},
        {"name": "JUNGLE", "x": 400, "z": -150},
    ]
