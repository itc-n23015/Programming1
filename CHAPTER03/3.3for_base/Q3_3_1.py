for i in range(10):
    if i % 2 ==0:
        continue
    print(i)

    #奇数のみが出力される

for i in range(10):
    if i % 2 == 0:
        break
    print(i)
    
    #continueをbreakにかえると何も出力しない
