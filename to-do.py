import sys

if len(sys.argv) == 1:
    print("\n" "\n" "Python Todo application \n" "=======================\n" "Command line arguments:\n" "-l   Lists all the tasks\n" "-a   Adds a new task\n" "-r   Removes an task\n" "-c   Completes an task\n" "\n")
elif sys.argv[1] == "-l":
    fr = open("tasks.txt", "r")
    text = fr.readlines()
    print(text)
