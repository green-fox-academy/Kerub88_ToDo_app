import sys

if len(sys.argv) == 1:
    print("\n" "\n" "Python Todo application \n" "=======================\n" "Command line arguments:\n" "-l   Lists all the tasks\n" "-a   Adds a new task\n" "-r   Removes an task\n" "-c   Completes an task\n" "\n")

elif sys.argv[1] == "-l":
    fr = open("tasks.txt", "r")
    text = fr.readlines()
    print(text)
    fr.close()

elif sys.argv[1] == "-a":
    fr = open("tasks.txt", "a")
    fr.writelines("\n" + str(sys.argv[2]))
    fr.close()

class Text:

    def __init__(self):
        fr = open("tasks.txt", "r")
        text = fr.readlines()
        for element in text:
            if element[0] ==
