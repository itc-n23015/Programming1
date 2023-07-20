with open('test.dat', 'wb') as f:
    f.write(b'012345')

with open('test.dat', 'rb') as f:
    data = f.read(6)
    print(data)


f = open('test.dat', 'rb')
f.tell()  #先頭

f.read(2) #2バイト読み込み

f.tell()

f.seek(4)

f.tell()

f.read(2)

f.close()
