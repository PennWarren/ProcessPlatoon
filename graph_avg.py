from itertools import islice
import matplotlib.pyplot as plt
import numpy as np


def graph_average(user_title="", user_x_label="", user_y_label=""):
    more_graphs = 'Y'
    while more_graphs == 'Y':
        print("What file would you like to graph?")
        input_name = input()

        with open(input_name, 'r') as i:
            x = []
            y = []
            mean = []
            sd = []

            for line in islice(i, None):
                # Add data to list
                data_point = line.split(', ')
                x.append(int(data_point[0]))
                y.append(float(data_point[1]))

                # Mean
                mean_point = np.mean(y)
                mean.append(mean_point)

                # Standard Deviation
                sd_point = np.std(y, axis=0)
                sd.append(sd_point)

            # Create numpy arrays for subtraction and addition operations
            np_mean = np.array(mean)
            np_sd = np.array(sd)

            # Plot moving average
            # Plot shaded standard error
            # Alpha controls the opacity of the shading
            plt.plot(x, np_mean, label=input_name)
            plt.fill_between(x, np_mean - np_sd, np_mean + np_sd, alpha=0.25)
            i.close()

        # Plot multiple files
        print("Would you like to plot another file? (Y/N)")
        more_graphs = input()
        # Only accept 'Y' or 'N' to ensure that user-input is consistent
        while True:
            if more_graphs == 'Y' or more_graphs == 'N':
                break
            print("Please enter either 'Y' or 'N'")
            more_graphs = input()

    # Label the graph
    plt.xlabel(user_x_label)
    plt.ylabel(user_y_label)
    plt.title(user_title)
    plt.legend(loc=4)
    plt.show()


print("What is the title of this graph?")
g_title = input()
graph_average(g_title, "Episode", "Mean Success Rate")
