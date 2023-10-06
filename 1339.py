n = int(input())
aph = {}
data = []

for _ in range(n):
    word = input()
    data.append(word)
    d = len(word)
    for i in range(d, 0, -1):
        if word[-i] not in aph.keys():
            aph[word[-i]] = 10**(i-1)
            
        else:
            aph[word[-i]] = aph[word[-i]] + 10**(i-1)
            
dictionary = dict(sorted(aph.items(), key=lambda item: -item[1]))

tmp = 0
for al in dictionary.keys():
    dictionary[al] = dictionary[al] * (9 - tmp)
    tmp+=1

res = 0
for al in dictionary.values():
    res+= al
print(res)
