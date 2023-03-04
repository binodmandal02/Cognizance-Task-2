# Write a python program that reads the contents from the given file ‘onelinefile.txt’. The file contains a single line which is of the format (int)(string)(float)(string) repeatedly. For e.g.
# 1Aaa3.5Maths2Bbb4.2Physics3Ccc7.62Chemistry

# Your main task is to split the contents of the given file based on their format and write it into a .csv file say ‘Filename2.csv’. For e.g. the above txt file should be converted into a csv file such that the contents look like this:
# 1,Aaa,3.5,Maths
# 2,Bbb,4.2,Physics
# 3,Ccc,7.62,Chemistry
import re

f = open("onelinefile.txt")
data = f.read()
f.close()

exp = re.compile(r'(\d+)([A-Za-z]+)(\d+\.\d+)([A-Za-z]+)')
x = exp.findall(data)

f = open("Filename2.csv", "w")
for i in x:
    f.write(",".join(i) + "\n")
f.close()