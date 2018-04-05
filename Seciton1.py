
import time

def fibonacci_recursive(n):
    if(n<2):
        return n
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

fibonacci_recursive(0),fibonacci_recursive(1),fibonacci_recursive(2),fibonacci_recursive(3),fibonacci_recursive(4),fibonacci_recursive(5)


n=40
time_1=int(round(time.time()))
fibonacci_recursive(n)
time_2=int(round(time.time()))
print(n," için geçen süre: ",time_2-time_1, "saniye")  # 40  için geçen süre:  58 saniye


for n in range(40):
    time_1=int(round(time.time()))
    fibonacci_recursive(n)
    time_2=int(round(time.time()))
    print(n," için geçen süre: ",time_2-time_1, "saniye")
    
#29  için geçen süre:  0 saniye
#30  için geçen süre:  1 saniye
#31  için geçen süre:  1 saniye
#32  için geçen süre:  1 saniye
#33  için geçen süre:  2 saniye
#34  için geçen süre:  3 saniye
#35  için geçen süre:  5 saniye
#36  için geçen süre:  9 saniye
#37  için geçen süre:  14 saniye
#38  için geçen süre:  22 saniye
#39  için geçen süre:  36 saniye


def fibonacci_loop(n):
    if(n<2):
        return n
    else:
        a=0
        b=1
        while(n>1):
            c=a+b
            a=b
            b=c
            n=n-1
    return c


fibonacci_loop(0),fibonacci_loop(1),fibonacci_loop(2),fibonacci_loop(3),fibonacci_loop(4),fibonacci_loop(5)


n=40
time_1=int(round(time.time()))
fibonacci_loop(n)
time_2=int(round(time.time()))
print(n," için geçen süre: ",time_2-time_1, "saniye")# 40  için geçen süre:  0 saniye 


for n in range(40):
    time_1=int(round(time.time()))
    fibonacci_loop(n)
    time_2=int(round(time.time()))
    print(n," için geçen süre: ",time_2-time_1, "saniye")
    
# 29  için geçen süre:  0 saniye
# 30  için geçen süre:  0 saniye
# 31  için geçen süre:  0 saniye
# 32  için geçen süre:  0 saniye
# 33  için geçen süre:  0 saniye
# 34  için geçen süre:  0 saniye
# 35  için geçen süre:  0 saniye
# 36  için geçen süre:  0 saniye
# 37  için geçen süre:  0 saniye
# 38  için geçen süre:  0 saniye
# 39  için geçen süre:  0 saniye
