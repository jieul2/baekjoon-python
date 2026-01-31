#인사성 밝은 곰곰이
lst = []
emoteCount = 0
emote = []

for _ in range(int(input())):
    i = input()
    if i == 'ENTER':
        emoteCount += len(list(set(emote)))
        emote = []
        continue
    emote.append(i)
emoteCount += len(list(set(emote)))
print(emoteCount)
