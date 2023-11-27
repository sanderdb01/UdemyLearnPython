myfile = open("fruits.txt")
fruits = myfile.read()
print(fruits)
fruits_list = fruits.splitlines()
for fruit in fruits_list:
	print(len(fruit))