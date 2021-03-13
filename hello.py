for i in range(3):
    a,b=map(int,input().replace(":",'').split())
    count=0
    while 1:
        if a%3==0:
            count+=1
        if a==b:
            break
        a+=1
        if a%100==60:
            a+=40
        if a%10000==6000:
            a+=4000
        if a==240000:
            a=0
    print(count)