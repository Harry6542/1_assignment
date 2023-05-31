def Initial_state_reading(filename):
    """ Reads a file's contents and returns the starting state as a list of lists.
              Args: filename (str): The name of the file to read.
              Returns: list: A collection of lists representing the initial state. Each row of the initial state is represented by an inner list.
          with open("input_1.txt", 'r') as file:
              lines = file.readlines()
          begining_state = [list(line.strip()) for line in lines]
          return begining_state
          """
    with open("input_1.txt", 'r') as file:
        lines = file.readlines()
    begining_state = [list(line.strip()) for line in lines]
    return begining_state
def neighbours_around_cell(displayed_grid, i, j):
    """ Updates the status of a grid display based on the Game of Life rules.
            Args: displayed_grid (list): A list of lists representing the current state of the grid display.
                                         Each inner list represents a grid display row.
                                         The characters in each row are saved as distinct inner list components.
                                         The grid display can include the characters '*' to denote live cells
                                         and '-' to represent dead cells.

            Returns: list: The updated status of the grid display after applying the Game of Life rules.
        """
    neighbours = []
    rows, cols = len(displayed_grid), len(displayed_grid[0])
    if i > 0:
        neighbours.append(displayed_grid[i - 1][j])
    if i < rows - 1:
        neighbours.append(displayed_grid[i + 1][j])
    if j > 0:
        neighbours.append(displayed_grid[i][j - 1])
    if j < cols - 1:
        neighbours.append(displayed_grid[i][j + 1])
    return neighbours
def New_state(displayed_grid):
    """

      Applies the rules of Conway's Game of Life to the provided grid and returns a new state of the grid.

      Parameters:
      - displayed_grid (list of lists): The current state of the grid, where '*' represents a live cell and '-' represents a dead cell.

      Returns:
      - new_displayed_grid (list of lists): The new state of the grid after applying the rules.

      """
    new_displayed_grid = []
    for i, row in enumerate(displayed_grid):
        new_row = []
        for j, cell in enumerate(row):
            neighbours = neighbours_around_cell(displayed_grid, i, j)
            Neighbours_alive = neighbours.count('*')
            if cell == '*':
                if Neighbours_alive < 2 or Neighbours_alive > 3:
                    new_row.append('-')
                else:
                    new_row.append('*')
            else:
                if Neighbours_alive == 3:
                    new_row.append('*')
                else:
                    new_row.append('-')
        new_displayed_grid.append(new_row)
    return new_displayed_grid
def Conway(input_1):
    """

       Reads the initial state from a text file, applies Conway's Game of Life rules to the grid, and saves the updated state to a new text file.

       Parameters:
       - input_1 (str): The name or path of the text file containing the initial state of the grid.

       Returns:None

       """