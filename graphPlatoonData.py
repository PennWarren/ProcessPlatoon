import matplotlib.pyplot as plt
import csv


def graph_data(user_x_label="Epoch", user_y_label="Success Rate", user_title="Success Rate"):
    print("What file would you like to graph?")
    input_name = input()

    x = []
    y = []

    with open(input_name, 'r') as i:
        plots = csv.reader(i, delimiter = ',')
        for row in plots:
            x.append(int(row[0]))
            y.append(float(row[1]))

    plt.plot(x, y)
    plt.xlabel(user_x_label)
    plt.ylabel(user_y_label)
    plt.title(user_title)
    plt.legend()
    plt.show()


graph_data()
