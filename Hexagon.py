# Axial Coordinates

class Hexagon:
    def __init__(self, q, r, color=.5):
        self.q = q
        self.r = r
        self.color = color
        self.neighbors = []

    def __repr__(self):
        return f'({self.q}, {self.r})'

    def add_neighbor(self, key):
        self.neighbors.append(key)

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









