check_num = 0
Primenumber = [] #素数算出のための格納される配列
Prime = [] #素数を格納する配列
num = input("数値を入力してください：")
num = int(num)
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
        print(Primenumber[i])
        Prime.append(Primenumber[i])
        check_num += 1

for i in Prime:
    for j in Prime:
        if i * j == num:
            print(i, j)
