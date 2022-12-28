import random

num = random.randint(1, 100)
while True:
    ans = input('請輸入數字:')
    ans = int(ans)
    if ans == num:
        print('你猜對了')
        break
    else:
        if ans < num:
         print('比答案小')
        else:
         print('比答案大')