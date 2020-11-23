import os
import sys

# reads a file and writes it to a file the given number of times
def duplicate(times):
    dataPath = os.environ.get('TASK2_PATH')
    file = open(os.path.join(dataPath, "output_data"), "r")
    fileContents = file.read()

    result = open("duplicate_data", "a")
    for iter in range(int(times)):
        result.write(str(iter) + ": " + fileContents + "\n")

    result.close()
    file.close()

duplicate(int(sys.argv[1]))
