n=0
total1=0
total2=0
maxV1=0
minV1=0
while True:
    y=input()
    if y=='999':
        break
    
    n+=1
    a=0
    b=0
    maxV2=0
    minV2=0
    while True:
        p=int(input())
        if p==-111:
            break
        else:
            a+=1
            b+=p
            if maxV2<p:
                maxV2=p
            if minV2>p or a==1:
                minV2=p
    print(f"總和: {b}, 平均: {b/a}, 最高分: {maxV2}, 最低分: {minV2}")
    if maxV1<maxV2:
        maxV1=maxV2
    if minV1>minV2 or n==1:
        minV1=minV2
    total1+=a
    total2+=b
print(f"班級: {n}, 平均: {total2/total1}, 最高分: {maxV1}, 最低分: {minV1}")