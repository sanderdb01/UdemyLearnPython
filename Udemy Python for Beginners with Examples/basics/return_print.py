def converter(original_unit, coefficient=0.3048):
	return original_unit * coefficient

print(converter(10))
print(converter(10, 0.62))

def returning():
	return 10

def printing():
	print(100)

print(type(returning()))
print(type(printing()))