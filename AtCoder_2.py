# print("".join(str(x) for x in ({1, 2, 3} - {int(input()), int(input())})))

# new_str, num, string = "", int(input()), input().split(" ")
# for x in range(0, num):
#     new_str += string[0][x] + string[1][x]
# print(new_str)

# def gcd(a,b):
#     return b if a == 0 else gcd(b % a, a)
#
#
# num = [int(x) for x in input().split(" ")]
# print(int(num[0] * num[1] / gcd(num[0], num[1])))


# def recursion(n):
#     result = 1
#     for i in range(2, n+1, 2):
#         result *= i
#         print(result)
#     return result
#
#
# string = str(recursion(10000000000000000000))
# print(string)
# print(len(string) - len(string.rstrip('0')))

# num, bricks, count, smash = int(input()), [int(x) for x in input().split(" ")], 1, 0
# for x in bricks:
#     if count == x: count += 1
#     else: smash += 1
# print(smash if smash != len(bricks) else 0 if len(bricks) == 1 else -1)


def findTrailingZeros(n):
    count = 0
    i=10
    if (n%2 == 1 ): return count
    while (n/i>=1):
        count += int(n/i)
        i *= 5
    return count

print(findTrailingZeros(input))

n = input()
test = len(n)
n = int(n)
b = 0
if n % 2 == 0:
    for i in range(1,test+11):
        b = b + (n//(5**(i)))//2
print(b)