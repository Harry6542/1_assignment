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

