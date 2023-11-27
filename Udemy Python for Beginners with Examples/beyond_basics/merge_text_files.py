# This was the way that I did it. Below is the instructor's solution
# from datetime import datetime
# def fileRead(textFile):
#     with open(textFile, "r") as myfile:
#         return myfile.read()

# current = datetime.now()

# num_files = [1, 2, 3]

# with open("%s.txt" % current, "w") as myfile:
#     for i in num_files:
#         myfile.write(fileRead("file%s.txt" % i) + "\n")
    
import glob2
from datetime import datetime
 
filenames = glob2.glob("file*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read() + "\n")
