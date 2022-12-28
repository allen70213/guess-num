import random

num = random.randint(1, 100)
count = 0
while True:
    ans = input('請輸入數字:')
    ans = int(ans)
    count = count + 1
    if ans == num:
        print('你猜對了')
        print('總共花了', count, '次')
        break
    else:
        if ans < num:
         print('比答案小')
        else:
         print('比答案大')
    print('這是你猜的第', count, '次')