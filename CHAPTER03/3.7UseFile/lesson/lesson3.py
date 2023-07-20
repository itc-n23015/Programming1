with open('sample.txt','r') as f:
    data = f.readline()
    line = data.strip()


with open('sample.txt', 'r') as f:
    for line in f:
        print(line.strip())


with open('sample.txt', 'r') as f:
    line = list(f)
print(lines)


with open('sample.txt', 'r')as f:
    line = list(f)
print(lines)
