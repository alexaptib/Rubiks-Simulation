import cube
import random
import time



if __name__ == '__main__':
  rubiksCube = cube.Cube()
  rubiksCube.rotate("W2")
  rubiksCube.rotate("B")
  rubiksCube.rotate("R'")
  rubiksCube.printCube()
