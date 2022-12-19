cnt = int( input() )
word_count = {}
for i in range(cnt):
    x = input()
    word_count[x]=word_count.get(x, 0)+1

print(len(word_count))
for word in word_count:
    print(word_count[word], end=' ')
