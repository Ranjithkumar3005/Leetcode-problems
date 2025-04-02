# with open("ran_file.txt", "a") as file:
#     file.write("\nGood Morning")

with open("ran_file.txt", "r") as file:
    for line in file:
        with open("new_file", "a") as file:
            file.write(line)
#