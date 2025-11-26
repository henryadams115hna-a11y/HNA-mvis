size_g = int(input("Please input a number to determine the size of graph where your circle will be: "))
size_c = int(input("Please input a number to determine the size of your circle: "))
y_scale = 1.5  # Makes the circle more round due to the character aspect ratio

for y in range(size_g, -size_g - 1, -1):
    for x in range(-2 * size_g,2 * size_g + 1):
        if (x  * 0.5)**2 + y**2*y_scale < size_c**2:
            print("#", end="")
        else:
            print(" ", end="")
    print()