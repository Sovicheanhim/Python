
# s = [int(x) for x in input().split(" ")]
# print(min(s))

# s = [int(x) for x in input().split(" ")]
# if(s[0] > s[1]):
#     print(abs(s[0] + s[1]))
# else:
#     print(abs(s[0]-s[1]))

# s = int(input())
# for x in range(2, s):
#     if (s%x== 0):
#         print(f"{x} {s//x}")
#         break

# z = [int(x) for x in input().split(" ")]
# s = int(input())
# order = 0
# if(s > z[0]):
#     while(s > z[2]):
#         if(s - z[2] >= z[0] or s - z[2] >= z[1]):
#             s -= z[2]
#             order += 1
#         else: break
#     print(order)
# else:
#     print(-1)

# s = [int(x) for x in input().split(" ")]
# n = list(input())
# print(n)
# count = 0
# takeCount = 0
# for x in n:
#     if(count < s[1]):
#         if(x == "R"):
#             count += 1
#     else: break
#     takeCount += 1
# print(takeCount)

s = [int(x) for x in input().split(" ")]
apples = list(input())
pick = 0
count = 0
if (apples.count("R") >= s[1]):
    while (pick < s[1]):
        count += 1
        leftCount = 0
        rightCount = 0
        for x in apples:
            leftCount += 1
            print(leftCount)
            print(apples)
            if (x == "R"):
                break
        for x in reversed(apples):
            rightCount += 1
            print(rightCount)
            print(apples)
            if (x == "R"):
                break
        if (leftCount < rightCount):
            for x in apples:
                if (x == "R"):
                    pick += 1
                    apples.remove(x)
        else:
            for x in reversed(apples):
                if (x == "R"):
                    pick += 1
                    apples.remove(x)
    print(count)
else:
    print(-1)
