def length_string(mystring):
	if type(mystring) == int:
		return "Sorry integers dont have length"
	elif type(mystring) == float:
		return "Sorry floats dont have length"
	else:
		return len(mystring)

print(length_string("test"))
print(length_string(10))
print(length_string(10.0))