from itertools import islice
import matplotlib.pyplot as plt


def graph_data(graph_step=1, user_x_label="Epoch", user_y_label="Success Rate", user_title="Success Rate"):
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

    plt.plot(x, y, label = "Success Rate")
    plt.xlabel(user_x_label)
    plt.ylabel(user_y_label)
    plt.title(user_title)
    plt.legend()
    plt.show()


print("How many data points would you like to see? Enter 1 for every point, 500 for every 500th point, "
      "and so on.")
step_size = int(input())
graph_data(step_size)
