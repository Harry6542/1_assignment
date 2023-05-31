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