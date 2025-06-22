import time

my_time = int(input("enter time in sec : "))

for hasan in range(my_time, 0, -1) :
    seconds = hasan % 60 
    minutes = int(hasan / 60) % 60
    hours = hasan // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
    
print("00:00:00")