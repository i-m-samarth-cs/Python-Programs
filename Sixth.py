def simulate_band(start, moves, size):
    """Simulate the band placement and return a list of occupied cells with their positions."""
    directions = {'u': (0, -1, 0), 'd': (0, 1, 0),
                  'f': (1, 0, 0), 'b': (-1, 0, 0),
                  'r': (0, 0, 1), 'l': (0, 0, -1)}
    cells = []
    x, y, z = start
    cells.append((x, y, z))  # Add the starting position
    for move in moves:
        dx, dy, dz = directions[move]
        x, y, z = x + dx, y + dy, z + dz
        if 0 <= x < size and 0 <= y < size and 0 <= z < size:
            cells.append((x, y, z))
    return cells

def count_overlaps(band1_cells, band2_cells):
    """Count the maximum overlap between Band 1 and Band 2 in terms of vertical stacking."""
    overlap_count = 0
    band2_set = set(band2_cells)
    for x, y, z in band1_cells:
        if (x, y, z) in band2_set:
            return -1  # Interlocked
        if (x, y - 1, z) in band2_set:
            overlap_count += 1
    return overlap_count

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Input parsing
    S = int(data[0])
    band1_start = tuple(map(int, data[1].split()))
    band1_moves = data[2]
    band2_start = tuple(map(int, data[3].split()))
    band2_moves = data[4]
    
    # Simulate bands
    band1_cells = simulate_band(band1_start, band1_moves, S)
    band2_cells = simulate_band(band2_start, band2_moves, S)
    
    # Check overlaps
    overlap_count = count_overlaps(band1_cells, band2_cells)
    if overlap_count == -1:
        print("Impossible")
    else:
        print(overlap_count)

if __name__ == "__main__":
    main()
