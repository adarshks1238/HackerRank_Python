n = int(input())

student = []

for i in range(n):
    name = input()
    mark = float(input())
    student.append([name,mark])
    
    

marks = sorted(set(s[1] for s in student))

names = [s[0] for s in student if s[1] == marks[1]]

for name in sorted(names):
    print(name)
