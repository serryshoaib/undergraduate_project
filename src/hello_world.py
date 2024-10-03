print("The text stored in ../data/hello_world.txt is: ", end="")

print(open("../data/hello_world.txt", "r").read(), end="")
