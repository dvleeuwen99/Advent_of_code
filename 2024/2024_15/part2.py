with open('test1.txt', 'r') as file:
    input = file.read().split( "\n\n" )

grid = { ( x * 2, y ): c.replace( 'O', '[' )
      for y, r in enumerate( input[0].splitlines() )
      for x, c in enumerate( r.strip( '\n' ) ) }
grid.update( { ( x + 1, y ): c.replace( '[', ']' ).replace( '@', '.' )
            for ( x, y ), c in grid.items() } )

def collect_boxes(grid, start_x, start_y, dx, dy):
    """Iteratively collect all boxes connected to the starting point."""
    to_process = [(start_x, start_y)]  
    boxes = {}  
    
    while to_process:
        x, y = to_process.pop()
        if (x, y) in boxes:
            continue
        
        boxes[(x, y)] = grid[(x, y)]
        
        if grid[(x, y)] == '[' and (x + 1, y) not in boxes:
            to_process.append((x + 1, y))
        if grid[(x, y)] == ']' and (x - 1, y) not in boxes:
            to_process.append((x - 1, y))
        
        if grid.get((x + dx, y + dy)) in "[]" and (x + dx, y + dy) not in boxes:
            to_process.append((x + dx, y + dy))
    
    return boxes

rx, ry = min( k for k, v in grid.items() if v == '@' )
for m in "".join( input[1].split() ):
    dx, dy = { '^': ( 0, -1 ), '>': ( 1, 0 ), 'v': ( 0, 1 ), '<': ( -1, 0 ) }[ m ]
    s = collect_boxes(grid, rx, ry, dx, dy)

    if all( grid[ ( x + dx, y + dy ) ] != '#' for x, y in s ):
        grid.update( { ( x, y ): '.' for x, y in s } )
        grid.update( { ( x + dx, y + dy ): c for ( x, y ), c in s.items() } )
        rx, ry = rx + dx, ry + dy

print( sum( 100 * y + x for x, y in grid if grid[ ( x, y ) ] == '[' ) )

