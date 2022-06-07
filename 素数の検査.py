f = open('素数.txt', 'r')
Check_Prime = f.readlines() #10000までの素数の格納
f.close()
check_num = 0
Primenumber = [] #素数の格納される配列
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
        if Primenumber[i] == int(Check_Prime[check_num]):
            print(Primenumber[i])
            check_num += 1
        else:   #エラー処理用
            print("素数以外が入っています(または素数が抜けてる)")
            break
    
