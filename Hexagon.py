class Hexagon:
    def __init__(self, q, r, value=0, color='white'):
        self.q = q
        self.r = r
        self.neigbors = []
        self.color = color

    def __repr__(self):
        return f'({self.q}, {self.r})'

class HexagonGrid:
    def __init__(self, radius):
        self.radius = radius
        self.hexagons = self.generate_hexagons() # dict
        self.adjacecny_matrix = self.generate_adjacency_matrix()
        
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

        return hexagons
    
    def generate_adjacency_matrix(self):
        adjacency_matrix = {}
        
        directions = [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]
        for key, value in self.hexagons.items(): 
            neighbors = []
            q = value.q
            r = value.r
            for direction in directions:
                new_key = f"{q+direction[0]},{r+direction[1]}"
                if new_key in self.hexagons:
                    neighbors.append(self.hexagons[new_key])

            adjacency_matrix[key] = neighbors 
        
        return adjacency_matrix

# Example usage
grid = HexagonGrid(radius=3)
print(grid.hexagons)
adjacency_matrix = grid.generate_adjacency_matrix()
print(adjacency_matrix)
