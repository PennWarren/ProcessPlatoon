from itertools import islice
import matplotlib.pyplot as plt


def graph_data(graph_step=1, user_title="", user_x_label="", user_y_label=""):
    more_graphs = 'Y'
    while more_graphs == 'Y':
        print("What file would you like to graph?")
        input_name = input()

        with open(input_name, 'r') as i:
            x = []
            y = []
            iterator = 0

            for line in islice(i, None):
                iterator += 1
                data_point = line.split(', ')
                if iterator == 1:
                    x.append(int(data_point[0]))
                    y.append(float(data_point[1]))
                if iterator % graph_step == 0:
                    x.append(int(data_point[0]))
                    y.append(float(data_point[1]))
                else:
                    pass

            plt.plot(x, y, label=input_name)
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
    plt.legend()
    plt.show()


print("What is the title of this graph?")
g_title = input()
print("Which data points would you like to see? Enter 1 for every point, 500 for every 500th point, "
      "and so on.")
step_size = int(input())
graph_data(step_size, g_title, "Epoch", "Success Rate")