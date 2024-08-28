for i in range(2000,2023+1):
    if((i%4==0 and i%100!=0) or i%400==0):
        print(f'{i} is a Leap Year')