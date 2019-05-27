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
        self.neighbors = []
        self.neighbors.append(["B", "R", "G", "O"])
        self.neighbors.append(["B", "O", "G", "R"])
        self.neighbors.append(["W", "O", "Y", "R"])
        self.neighbors.append(["W", "R", "Y", "O"])
        self.neighbors.append(["W", "B", "Y", "G"])
        self.neighbors.append(["W", "G", "Y", "B"])

    def rotate(self, move):
        face = self.order.index(move[0])
        if len(move) == 1:
            self.cube[face].insert(0, self.cube[face][-2])
            self.cube[face].insert(1, self.cube[face][-1])
            del self.cube[face][-1]
            del self.cube[face][-1]
        
        elif move[1] ==  "'":
            self.cube[face].append(self.cube[face][0])
            self.cube[face].append(self.cube[face][1])
            del self.cube[face][0]
            del self.cube[face][0]
        
        elif move[1] == "2":
            self.cube[face].append(self.cube[face][0])
            self.cube[face].append(self.cube[face][1])
            self.cube[face].append(self.cube[face][2])
            self.cube[face].append(self.cube[face][3])
            del self.cube[face][0]
            del self.cube[face][0]
            del self.cube[face][0]
            del self.cube[face][0]
            
        neighborsToSet = []
        if move[0] == "W":
            for neighbor in self.neighbors[face]:
                neighborsToSet.append([self.cube[self.order.index(neighbor)][0], self.cube[self.order.index(neighbor)][1], self.cube[self.order.index(neighbor)][2]])
            print(neighborsToSet)
            if len(move) == 1:
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            elif move[1] == "'":
                neighborsToSet.append(neighborsToSet[0])
                del neighborsToSet[0]

            elif move[1] == "2":
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            print(neighborsToSet)

            for neighbor in self.neighbors[face]:
                self.cube[self.order.index(neighbor)][0] = neighborsToSet[self.neighbors[face].index(neighbor)][0]
                self.cube[self.order.index(neighbor)][1] = neighborsToSet[self.neighbors[face].index(neighbor)][1]
                self.cube[self.order.index(neighbor)][2] = neighborsToSet[self.neighbors[face].index(neighbor)][2]
            

        elif move[0] == "Y":
            for neighbor in self.neighbors[face]:
                neighborsToSet.append([self.cube[self.order.index(neighbor)][6], self.cube[self.order.index(neighbor)][5], self.cube[self.order.index(neighbor)][4]])
            if len(move) == 1:
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            elif move[1] == "'":
                neighborsToSet.append(neighborsToSet[0])
                del neighborsToSet[0]

            elif move[1] == "2":
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            for neighbor in self.neighbors[face]:
                self.cube[self.order.index(neighbor)][6] = neighborsToSet[self.neighbors[face].index(neighbor)][0]
                self.cube[self.order.index(neighbor)][5] = neighborsToSet[self.neighbors[face].index(neighbor)][1]
                self.cube[self.order.index(neighbor)][4] = neighborsToSet[self.neighbors[face].index(neighbor)][2]

        elif move[0] == "B":
            for neighbor in self.neighbors[face]:
                if neighbor == "W":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][2], self.cube[self.order.index(neighbor)][1], self.cube[self.order.index(neighbor)][0]])
                elif neighbor == "Y":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][6], self.cube[self.order.index(neighbor)][5], self.cube[self.order.index(neighbor)][4]])
                elif neighbor == "R":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][4], self.cube[self.order.index(neighbor)][3], self.cube[self.order.index(neighbor)][2]])
                elif neighbor == "O":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][0], self.cube[self.order.index(neighbor)][7], self.cube[self.order.index(neighbor)][6]])
            if len(move) == 1:
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            elif move[1] == "'":
                neighborsToSet.append(neighborsToSet[0])
                del neighborsToSet[0]

            elif move[1] == "2":
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            self.cube[self.order.index(self.neighbors[face][0])][2] = neighborsToSet[0][0]
            self.cube[self.order.index(self.neighbors[face][0])][1] = neighborsToSet[0][1]
            self.cube[self.order.index(self.neighbors[face][0])][0] = neighborsToSet[0][2]

            self.cube[self.order.index(self.neighbors[face][1])][0] = neighborsToSet[1][0]
            self.cube[self.order.index(self.neighbors[face][1])][7] = neighborsToSet[1][1]
            self.cube[self.order.index(self.neighbors[face][1])][6] = neighborsToSet[1][2]

            self.cube[self.order.index(self.neighbors[face][2])][6] = neighborsToSet[2][0]
            self.cube[self.order.index(self.neighbors[face][2])][5] = neighborsToSet[2][1]
            self.cube[self.order.index(self.neighbors[face][2])][4] = neighborsToSet[2][2]

            self.cube[self.order.index(self.neighbors[face][3])][4] = neighborsToSet[3][0]
            self.cube[self.order.index(self.neighbors[face][3])][3] = neighborsToSet[3][1]
            self.cube[self.order.index(self.neighbors[face][3])][2] = neighborsToSet[3][2]
            
        elif move[0] == "G":
            for neighbor in self.neighbors[face]:
                if neighbor == "W":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][6], self.cube[self.order.index(neighbor)][5], self.cube[self.order.index(neighbor)][4]])
                elif neighbor == "Y":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][2], self.cube[self.order.index(neighbor)][1], self.cube[self.order.index(neighbor)][0]])
                elif neighbor == "R":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][0], self.cube[self.order.index(neighbor)][7], self.cube[self.order.index(neighbor)][6]])
                elif neighbor == "O":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][4], self.cube[self.order.index(neighbor)][3], self.cube[self.order.index(neighbor)][2]])
            if len(move) == 1:
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            elif move[1] == "'":
                neighborsToSet.append(neighborsToSet[0])
                del neighborsToSet[0]

            elif move[1] == "2":
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            self.cube[self.order.index(self.neighbors[face][0])][6] = neighborsToSet[0][0]
            self.cube[self.order.index(self.neighbors[face][0])][5] = neighborsToSet[0][1]
            self.cube[self.order.index(self.neighbors[face][0])][4] = neighborsToSet[0][2]

            self.cube[self.order.index(self.neighbors[face][1])][0] = neighborsToSet[1][0]
            self.cube[self.order.index(self.neighbors[face][1])][7] = neighborsToSet[1][1]
            self.cube[self.order.index(self.neighbors[face][1])][6] = neighborsToSet[1][2]

            self.cube[self.order.index(self.neighbors[face][2])][2] = neighborsToSet[2][0]
            self.cube[self.order.index(self.neighbors[face][2])][1] = neighborsToSet[2][1]
            self.cube[self.order.index(self.neighbors[face][2])][0] = neighborsToSet[2][2]

            self.cube[self.order.index(self.neighbors[face][3])][4] = neighborsToSet[3][0]
            self.cube[self.order.index(self.neighbors[face][3])][3] = neighborsToSet[3][1]
            self.cube[self.order.index(self.neighbors[face][3])][2] = neighborsToSet[3][2]

        elif move[0] == "R":
            for neighbor in self.neighbors[face]:
                if neighbor == "W":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][4], self.cube[self.order.index(neighbor)][3], self.cube[self.order.index(neighbor)][2]])
                elif neighbor == "Y":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][4], self.cube[self.order.index(neighbor)][3], self.cube[self.order.index(neighbor)][2]])
                elif neighbor == "B":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][0], self.cube[self.order.index(neighbor)][7], self.cube[self.order.index(neighbor)][6]])
                elif neighbor == "G":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][4], self.cube[self.order.index(neighbor)][3], self.cube[self.order.index(neighbor)][2]])
            if len(move) == 1:
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            elif move[1] == "'":
                neighborsToSet.append(neighborsToSet[0])
                del neighborsToSet[0]

            elif move[1] == "2":
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            self.cube[self.order.index(self.neighbors[face][0])][4] = neighborsToSet[0][0]
            self.cube[self.order.index(self.neighbors[face][0])][3] = neighborsToSet[0][1]
            self.cube[self.order.index(self.neighbors[face][0])][2] = neighborsToSet[0][2]

            self.cube[self.order.index(self.neighbors[face][1])][0] = neighborsToSet[1][0]
            self.cube[self.order.index(self.neighbors[face][1])][7] = neighborsToSet[1][1]
            self.cube[self.order.index(self.neighbors[face][1])][6] = neighborsToSet[1][2]

            self.cube[self.order.index(self.neighbors[face][2])][4] = neighborsToSet[2][0]
            self.cube[self.order.index(self.neighbors[face][2])][3] = neighborsToSet[2][1]
            self.cube[self.order.index(self.neighbors[face][2])][2] = neighborsToSet[2][2]

            self.cube[self.order.index(self.neighbors[face][3])][4] = neighborsToSet[3][0]
            self.cube[self.order.index(self.neighbors[face][3])][3] = neighborsToSet[3][1]
            self.cube[self.order.index(self.neighbors[face][3])][2] = neighborsToSet[3][2]

        elif move[0] == "O":
            for neighbor in self.neighbors[face]:
                if neighbor == "W":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][0], self.cube[self.order.index(neighbor)][7], self.cube[self.order.index(neighbor)][6]])
                elif neighbor == "Y":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][0], self.cube[self.order.index(neighbor)][7], self.cube[self.order.index(neighbor)][6]])
                elif neighbor == "B":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][4], self.cube[self.order.index(neighbor)][3], self.cube[self.order.index(neighbor)][2]])
                elif neighbor == "G":
                    neighborsToSet.append([self.cube[self.order.index(neighbor)][0], self.cube[self.order.index(neighbor)][7], self.cube[self.order.index(neighbor)][6]])
            if len(move) == 1:
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            elif move[1] == "'":
                neighborsToSet.append(neighborsToSet[0])
                del neighborsToSet[0]

            elif move[1] == "2":
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]
                neighborsToSet.insert(0, neighborsToSet[-1])
                del neighborsToSet[-1]

            self.cube[self.order.index(self.neighbors[face][0])][0] = neighborsToSet[0][0]
            self.cube[self.order.index(self.neighbors[face][0])][7] = neighborsToSet[0][1]
            self.cube[self.order.index(self.neighbors[face][0])][6] = neighborsToSet[0][2]

            self.cube[self.order.index(self.neighbors[face][1])][0] = neighborsToSet[1][0]
            self.cube[self.order.index(self.neighbors[face][1])][7] = neighborsToSet[1][1]
            self.cube[self.order.index(self.neighbors[face][1])][6] = neighborsToSet[1][2]

            self.cube[self.order.index(self.neighbors[face][2])][0] = neighborsToSet[2][0]
            self.cube[self.order.index(self.neighbors[face][2])][7] = neighborsToSet[2][1]
            self.cube[self.order.index(self.neighbors[face][2])][6] = neighborsToSet[2][2]

            self.cube[self.order.index(self.neighbors[face][3])][4] = neighborsToSet[3][0]
            self.cube[self.order.index(self.neighbors[face][3])][3] = neighborsToSet[3][1]
            self.cube[self.order.index(self.neighbors[face][3])][2] = neighborsToSet[3][2]


        #elif move[1] == "2":
            
        #elif move[1] == "'":
  

    def printCube(self):
        for face in self.cube:
            line = 0
            while line < 3:
                if line == 0:
                    line0 = face[0] + face[1] + face[2]
                elif line == 1:
                    line1 = face[7] + self.order[self.cube.index(face)] + face[3]
                else:
                    line2 = face[6] + face[5] + face[4]
                line += 1
            print(line0[0] + " | " + line0[1] + " | " + line0[2])
            print("---------")
            print(line1[0] + " | " + line1[1] + " | " + line1[2])
            print("---------")
            print(line2[0] + " | " + line2[1] + " | " + line2[2])
            print()
            print()

        
