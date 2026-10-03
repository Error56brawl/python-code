documents = [
    {"A", "B", "C"},
    {"B", "D"},
    {"C", "B"}
]

count = {}

for doc in documents:
    for word in doc:
        count[word] = count.get(word, 0) + 1

answer = set()

for word in count:
    if count[word] == 1:
        answer.add(word)

print(answer)
