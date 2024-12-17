import sys

shapes = {
    'Q': [['#', '#'],
          ['#', '#']],
    'Z': [['#', '#', '.'],
          ['.', '#', '#']],
    'S': [['.', '#', '#'],
          ['#', '#', '.']],
    'T': [['#', '#', '#'],
          ['.', '#', '.']],
    'I': [['#', '#', '#', '#']],
    'L': [['#', '.'],
          ['#', '.'],
          ['#', '#']],
    'J': [['.', '#'],
          ['.', '#'],
          ['#', '#']]
}

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['.'] * width for _ in range(height)]  # Create an empty grid with '.' cells.

    def drop_and_place(self, piece, start_column):

        # Calculate the last possible row (level) where the piece can be dropped
        last_level = len(self.grid) - len(piece)

        # Find the lowest level where the piece can fit without collision
        for level in range(last_level + 1):
            # We Check if placing the piece at this level causes any collision with existing blocks
            collision = any(
                self.grid[level + i][start_column + j] == '#' and piece[i][j] == '#'
                for i in range(len(piece))
                for j in range(len(piece[0]))
            )
            if collision:
                level -= 1  # Move up one level if there's a collision
                break

        # Place the piece on the determined level by updating the grid with '#' blocks
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                if piece[i][j] == '#':
                    self.grid[level + i][start_column + j] = '#'  # Mark the grid cells with '#' to mention it filled

        # Remove any fully completed lines (rows with no '.' cells)
        self.grid = [line for line in self.grid if '.' in line]

        # Make sure the grid maintains its height by adding empty rows ('.') at the top if needed
        while len(self.grid) < self.height:
            self.grid.insert(0, ['.'] * self.width)  # Add an empty row at the top if the height of the grid isnt sufficient

    def __str__(self):
        return '\n'.join(''.join(line) for line in self.grid)


def tetris_engine(line):
    grid = Grid(10, 5) 
    moves = line.split(',')  # Split the input line into individual moves

    for move in moves:
        shape, start_column = move[0], int(move[1])  
        grid.drop_and_place(shapes[shape], start_column) 

    # Count the number of rows that have at least one block ('#')
    return sum(1 for row in grid.grid if '#' in row)


def main():
    """
    Read input from stdin, process each line using the tetris_engine function,
    and write the output to 'output.txt'.
    """
    output_file_path = 'output.txt'
    with open(output_file_path, 'w') as output_file:
        for line in sys.stdin:
            result = tetris_engine(line.strip()) 
            output_file.write(str(result) + '\n') 
            print(result)

if __name__ == "__main__":
    main()
