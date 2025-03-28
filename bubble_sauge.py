queue = [9,8,7,6,1,2,3,4]
n = len(queue)

for j in range(0, n-1):
    for i in range(0, n-1-j):
        if queue[i] > queue[i+1]:
            # 交换元素
            queue[i], queue[i+1] = queue[i+1], queue[i]
    print(queue)

print("Final result:", queue)