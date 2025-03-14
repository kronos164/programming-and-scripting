import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
    directory = "../programming-and-scripting/pands-weekly-tasks/"
    print(file)
    file = directory + str(file)
    print(file)
    with open(file, "r") as f:
        count = 0
        for line in f:
            for char in line:
                if char == "e":
                    count += 1
        print(count)
else:
    print("Error: No file argument provided.")