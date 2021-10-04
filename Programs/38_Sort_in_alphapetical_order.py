Words = [word.lower() for word in input().split(",")]

Words.sort()

for word in Words:
    print(word)