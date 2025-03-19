import numpy as np
import matplotlib.pyplot as pyplot

def plot_data_from_dat(filename, delimiter = None, skip_header = 0, x_column = 0, y_column = 1):
    
    """
    Plots data from a .dat file.

    Args:
        filename (str): The name of the .dat file.
        delimiter (str, optional): The delimiter used in the file (e.g., ",", " ", "\t"). 
                                  If None, whitespace is used. Defaults to None.
        skip_header (int, optional): Number of header lines to skip. Defaults to 0.
        x_column (int, optional): The column index to use for the x-axis (0-based). Defaults to 0.
        y_column (int, optional): The column index to use for the y-axis (0-based). Defaults to 1.
    """

    data = np.genfromtxt(filename, delimiter = delimiter, skip_header = skip_header)

    if data.size == 0 :  # Check if file is empty or contains only header
        raise ValueError("File is empty or contains only header/comments")

    name_legend = ["$ p $", "$ U_{x} $", "$ U_{y} $", "$ k $", r"$ \varepsilon $"]

    pyplot.figure()
    for col in range(1, len(name_legend) + 1):
        pyplot.plot(data[:, x_column], data[:, col], label = name_legend[col - 1])

    pyplot.xlabel('Iteration Number', fontsize = 13, color = 'black')
    pyplot.title('Residuals', loc = 'center', fontsize = 15, color = 'black', style = 'italic')
    pyplot.yscale('log')
    pyplot.legend(loc = 'best')
    pyplot.grid(True) # Add a grid for better readability
    pyplot.tight_layout() # Adjust layout to prevent labels from overlapping
    pyplot.savefig(fname = 'Residuals', dpi = 300, format = "png")

plot_data_from_dat("postProcessing/residuals/0/residuals.dat", x_column = 0, y_column = 1, skip_header = 4)