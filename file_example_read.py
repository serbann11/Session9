fp = open("text","r")
print(fp.read())
fp.close()    # close is good practice, not needed

with open("text", "r") as fp:
    print(fp.read()) #because there is no code under with, it closed automatically

#read from the same file, line by line
with open('text', 'r') as fp:
    line_number = 1
    for line in fp:
        # print(line, end="") #print adds a new line as the command is repeated, end="" fixes it
        # print(line.rstrip())
        print(f"{line_number}: {line.rstrip()}")
        line_number += 1