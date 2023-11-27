# This was the way that I did it. Below is the instructor's solution
# temperatures = [10, -20, -289, 100]
# def c_to_f(c):
#     if c < -273.15:
#         return "That temperature doesn't make sense!"
#     else:
#         f = c* 9/5 + 32
#         return f
    
# with open("temperature_list_example.txt", "w") as myfile:
#     for t in temperatures:
#         temp = c_to_f(t)
#         if type(temp) == float:
#             myfile.write("%s\n" % temp)
            
temperatures = [10,-20,-289,100]
def writer(temperatures, filepath):
    with open(filepath, 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c* 9/5 + 32
                file.write(str(f) + "\n")
writer(temperatures, "temps.txt") #Here we're calling the function, otherwise no output will be generated