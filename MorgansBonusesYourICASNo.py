
number_grid = [
    [5.00, 9.00, 16.00, 22.00, 30.00],
    [10.00, 12.00, 18.00, 24.00, 36.00],
	[20.00, 25.00, 32.00, 42.00, 53.00],
    [32.00, 38.00, 45.00, 55.00, 68.00],
	[46.00, 54.00, 65.00, 77.00, 90.00],
	[60.00, 72.00, 84.00, 96.00, 120.00],
	[85.00, 100.00, 120.00, 140.00, 175.00]
]

weeks = int(input("Enter the number of weeks worked: "))
reviews = int(input("Enter the number of positive reviews received: "))


while (weeks != 999 or reviews != 999):
	if reviews >= 4:
		print("Bonus: " + "$" + str(number_grid[weeks][4]))
		#(number_grid[weeks][4])
	else:
		print("Bonus: " + "$" + str(number_grid[weeks][reviews]))
		#print(number_grid[weeks][reviews])

	weeks = int(input("Enter the number of weeks worked: \n"))
	reviews = int(input("Enter the number of positive reviews received: \n"))
  
