import cube

rubiksCube = cube.Cube()

face = 0
while face < 6:
    line = 0
    while line < 3:
        if line == 0:
            line0 = rubiksCube.cube[face][0] + rubiksCube.cube[face][1] + rubiksCube.cube[face][2]
        elif line == 1:
            line1 = rubiksCube.cube[face][7] + rubiksCube.order[face] + rubiksCube.cube[face][3]
        else:
            line2 = rubiksCube.cube[face][6] + rubiksCube.cube[face][5] + rubiksCube.cube[face][4]
        line += 1
    face += 1
    print(line0)
    print(line1)
    print(line2)
    print()