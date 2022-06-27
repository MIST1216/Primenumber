Primenumber = [] #素数算出のための格納される配列
Prime = [] #素数を格納する配列
num = int(input("数値を入力してください："))
if num > 100000000:
    num = 0
    print('大きすぎるため計算できません')
num += 1
if num >= 100:
    num_10 = int(num/10)
else :
    num_10 = num
for i in range(num):
    Primenumber.append(i)
for i in range(4,num,2):
    Primenumber[i] = 0
for i in range(3,num_10):
    if Primenumber[i] == 0:
        continue
    for j in range(3*i,num,2*i):
        Primenumber[j] = 0
for i in range(2,num):
    if Primenumber[i] != 0:
        Prime.append(Primenumber[i])
num -= 1
for i in Prime:
    if num%i == 0:
        print(i, end = '')
        num /= i
        count = 1
        while num%i == 0:
            count += 1
            num /= i
        if count > 1:
            print('^', count, sep = '', end = '')
        if i > num:
            break
        else:
            print(end = '×')
