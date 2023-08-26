# Axial Coordinates
import math

BLACK = (0, 0, 0)
DARK_GREY = (30, 30, 30)
OFF_WHITE = (255, 255, 240)
DARK_BEIGE = (139, 121, 94)
DARK_MAGENTA = (139, 0, 139)
MAROON = (128, 0, 0)
FOREST_GREEN = (34, 139, 34)

class Hexagon:
    def __init__(self, q, r, color=(0, 255, 0)):
        self.q = q
        self.r = r
        self.color = color
        self.neighbors = []

    def __repr__(self):
        return f'({self.q}, {self.r})'

    def add_neighbor(self, key):
        self.neighbors.append(key)
    
    def get_vertices(self, hexagon_size):
        x = hexagon_size * 3/2 * self.q
        y = hexagon_size * (math.sqrt(3) / 2 * self.q + math.sqrt(3) * self.r)
        
        vertices = []
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = math.pi / 180 * angle_deg
            vertex_x = x + hexagon_size * math.cos(angle_rad)
            vertex_y = y + hexagon_size * math.sin(angle_rad)
            vertices.append((vertex_x, vertex_y))
        
        return vertices

class HexagonGrid:
    def __init__(self, radius):
        self.radius = radius
        self.hexagons = self.generate_hexagons() # dict
        
    def generate_hexagons(self):
        radius = self.radius
        hexagons = {}
        hexagons["0,0"] = Hexagon(0, 0)
        
        for r in range(0, -radius, -1):
            for q in range(-r - 1, -radius - r, -1):
                hexagons[f"{q},{r}"] = Hexagon(q, r)

        for r in range(1, radius):
            for q in range(0, -radius, -1):
                hexagons[f"{q},{r}"] = Hexagon(q, r)
                
        for q in range(1, radius):
            for r in range(-q, radius - q):
                hexagons[f"{q},{r}"] = Hexagon(q, r)

        hexagons = self.generate_adjacency_matrix(hexagons)

        return hexagons
    
    def generate_adjacency_matrix(self, hexagons):
        directions = [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]

        for key in hexagons: 
            hexagon = hexagons[key]
            for direction in directions:
                new_key = f"{hexagon.q+direction[0]},{hexagon.r+direction[1]}"
                if new_key in hexagons:
                    hexagons[key].add_neighbor(new_key)

        return hexagons




# Example usage
# grid = HexagonGrid(radius=3)
# for key in grid.hexagons:
#     hex = grid.hexagons[key]
#     neighbors = hex.neighbors
#     print(f"{key}: {neighbors}")









