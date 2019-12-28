# a = [int(x) for x in input().split(" ")]
# print("bust") if sum(a) >= 22 else print("win")

# s = input()
# count = 0
# first_half, second_half = s[:len(s)//2], s[(len(s)+1)//2:]
# if first_half == reversed(second_half):
#     print(count)
# else:
#     for x in range(len(first_half)):
#         if first_half[x] != second_half[len(second_half)-x-1]:
#             count += 1
#     print(count)

# num = int(input())
# a, s, people = [], [], []
# for x in range(num):
#     a[x] = int(input())
#     for y in range(a[x]):
#         s[y] = input().split(" ")


num = int(input())
s = input().split(" ")
num_list = [int(x) for x in s]
taken_list, count = [x for x in num_list], 0
for x in num_list:
    taken_list.remove(taken_list[0])
    for y in taken_list:
        count += bin(x) ^ bin(y)
print(count % (pow(10, 9)+7))
