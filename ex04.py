counter=0
total=0
maxV=0
minV=0
while True:
    x=int(input('x='))
    if x==999:
        break
    else:
        counter+=1
        total+=x
        if x>maxV:
            maxV=x
        if x<minV or counter==1:
            minV=x
print(f"總和: {total}, 平均: {total/counter}, 最大值: {maxV}, 最小值: {minV}")
        