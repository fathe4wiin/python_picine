import sys
import math



def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + 
                     (p2[1] - p1[1])**2 + 
                     (p2[2] - p1[2])**2)


def main():
    if len(sys.argv) < 2:
        print("Error: <InvalidUsage> Usage: python script.py <x,y,z>")
        return
    
    try:
        parts = sys.argv[1].split(',')
        coord = []
        for p in parts:
            coord.append(float(p))
        if len(coord) != 3:
            raise ValueError
        coord = tuple(coord)
    except ValueError:
        print("Error: <InvalidCoords> All Coordinates must be Numbers and in this format: <x,y,z>")
        return

    player = "fathe4wiin"
    current_pos = (0, 0, 0)
    print("Parsed coordinates:", coord)
    print("Current position:", current_pos)
    print(f"teleported {player} to {coord}\nTotal Distance: {distance(current_pos, coord)}")
    
if __name__ == "__main__":
    main()