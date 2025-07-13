def split_and_join(line):
    s = line.split(" ")
    j = "-".join(s)
    return j
    
line = input()
result = split_and_join(line)
print(result)