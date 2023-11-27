numbers = [1,2,3]
myfile = open("num_list.txt", "w")
for num in numbers:
	myfile.write(str(num))
	myfile.write("\n")
myfile.close()