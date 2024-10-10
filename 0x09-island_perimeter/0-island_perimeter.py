def island_perimeter(grid):
    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    
    perimeter = 0
    
    # Iterate through the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4
                
                # Check if the cell above is also land, subtract 2 (for shared edge)
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                
                # Check if the cell to the left is also land, subtract 2 (for shared edge)
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2
    
    return perimeter

