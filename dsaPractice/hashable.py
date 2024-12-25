from collections import Counter, defaultdict


string = "aaaaaaaaaabbbbbbbbbbbccccccccdddddddddddddeeeeeeeeeeee"
count = Counter(string)
print(count.values())

dictionary = defaultdict(int)
dictionary[1]
dictionary[2]
dictionary[9]
dictionary[3]

print(dictionary)
print(9 in dictionary)