import random
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num4 = ''.join(random.sample(num, k=4))
while True:
    a = input()
    if a == num4:
        break
    if len(a) != 4:
        print('input 4 num.')
        continue
    answer = ''
    for i in range(4):
        if num4[i] == a[i]:
            answer += num4[i]
        else:
            answer += 'X'
            print('-> ' + answer)
