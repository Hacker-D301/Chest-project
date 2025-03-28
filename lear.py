def data_input(area, data, same):
    for i in range(0, len(data)):
        key = data[i]%10
        if area[key] != "":
            same = True
            return key, area, data, same, i
        area[key-1] = data[i]
    print(area)
    return key, area, data, same

def hashing(key, area):
    j = 0
    n = len(area)
    count = 1
    while j<n:
        if area[key-1] != "":
            count = count + 1
            key = key + 1
            j = j + 1
        else:
            return key

def new_area(key, area, data, i):
    area[key-1] = data[i]
    return key, area, data, i#THIS CODE HAVE TO BEHIND HASHING
    
area:list = [""]*10
data = [11,22,33,44,55,66,81]
same = False
key, area, data, same, i = data_input(area, data, same)

key = hashing(key, area)
key, area, data, i = new_area(key, area, data, i)
print(area)