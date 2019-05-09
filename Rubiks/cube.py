class Cube:

    def __init__(self):
        
        self.cube = []
        self.order = ["W", "Y", "B", "G", "R", "O"]
        face = 0
        while face < 6:
            self.cube.append([])
            square = 0
            while square < 8:
                self.cube[face].append(self.order[face])
                square += 1
            face += 1
        self.neighbors = [[][][][][][]]

        


        