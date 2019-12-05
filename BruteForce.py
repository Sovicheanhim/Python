import enchant
d = enchant.Dict("en_US")
letters = " abcdefghijklmnopqrstuvwxyz"
plainText = [""] * 26
cipherText = input("Please enter cipher text: ")
answer, count = "", 0
for x in range(25):
    count, check, answer = 0, "", ""
    for y in cipherText:
        plainText[x] += letters[(letters.index(y)+x) % 26]
    for z in reversed(plainText[x]):
        check = z + check
        if check.isalpha() and len(check) == 1:
            continue
        elif d.check(check):
            answer = check + " " + answer
            check = ""
            continue
    checkAnswer = answer.strip().split(" ")
    for a in checkAnswer:
        if not a or not d.check(a): break
        else: count += 1
    if count == len(checkAnswer):
        print(answer)
