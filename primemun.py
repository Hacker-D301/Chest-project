# input = 29
# prime = True
# i=2
# 
# while prime:
#     if input%i == 0:
#         print(input, " / / ", i, "result:", prime)
#         print(input, "not prime")
#     else:
#             print(input, " / / ", i, "result:", prime)
#             print(input, "is prime")
#     i = i + 1

# input = 1
# 
# prime = True
# 
# if input < 2:
#     print("Not prime")
#     quit()
# 
# for i in range (2,input):
#     if input % i == 0:
#         print("Not prime")
#         quit()
# print("Is prime")

input = 0
prime = True
i = 2

while prime == True and i < input:
    if input % i == 0:
        print("Not prime")
        prime = False
    print (input, " ", i, " ", prime)
    i = i+1

if prime == True:
    print("Is prime")