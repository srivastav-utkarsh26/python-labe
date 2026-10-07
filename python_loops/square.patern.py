size = int(input("Enter the size of the square: "))

for row in range(size):
	for column in range(size):
		if row in (0, size - 1) or column in (0, size - 1):
			print("*", end=" ")
		else:
			print(" ", end=" ")
	print()
