from itertools import islice


# Function to take in names of files
def get_filenames():
    print("What file would you like to process? Example: \"data.txt\"")
    input_name = input()

    print("Where would you like to output? Example: \"output.txt\"")
    output_name = input()
    return input_name, output_name


# Opens output file given in get_filenames. Use "w+" to write over, or change to "a+" to append (the + creates a new
# file if the file name inputted does not exist).
i, o = get_filenames()
output_file = open(o, "w+")
input_file = open(i)

iterator = 0

# Change the second parameter to "x" to skip the first x lines
for line in islice(input_file, 15, None):
    # Print epoch number and delimit the .csv OR .txt file
    if line.startswith("Epoch"):
        iterator += 1
        output_file.write(str(iterator) + ", ")
    # Print success rate
    if line.startswith("Success"):
        success_rate = line.split(':')
        output_file.write(success_rate[1])
    # Skip all irrelevant lines
    else:
        pass


input_file.close()
output_file.close()
