# ... Dictionaries ...

# The text is given in a single line. For each word of the text count the number of its occurrences before it. A word is a sequence of non-whitespace characters. Two consecutive words are separated by one or more spaces. Punctiation marks are a part of a word, by this definition.

words = input().split()
for i in range(len(words)):
    print(words[:i].count(words[i]), end=' ')

# You are given a dictionary consisting of word pairs. Every word is a synonym the other word in its pair. All the words in the dictionary are different. After the dictionary there's one more word given. Find a synonym for him.

n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])

# As you know, the president of USA is elected not by direct vote, but through a two-step voting. First elections are held in each state and determine the winner of elections in that state. Thereafter, the state election is going: in this election, every state has a certain the number of votes — the number of electors from that state. In practice, all the electors from the state of voted in accordance with the results of the vote within a state. The first line contains the number of records. After that, each entry contains the name of the candidate and the number of votes they got in one of the states. Count the total results of the elections: sum the number of votes for each candidate. Print candidates in the alphabetical order.

n = int(input())
d = {}
for i in range(n):
    key, val = input().split()
    if key in d:
        d[key] += int(val)
    else:
        d[key] = int(val)
for key, val in sorted(d.items()):
   print(key, val)

# Given the text: the first line contains the number of lines, then given the lines of words. Print the word in the text that occurs most often. If there are many such words, print the one that is less in the alphabetical order.

counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))

# The virus attacked the filesystem of the supercomputer and broke the control of access rights to the files. For each file there is a known set of operations which may be applied to it:
# write W,
# read R,
# execute X.
# The first line contains the number N — the number of files contained in the filesystem. The following N lines contain the file names and allowed operations with them, separated by spaces. The next line contains an integer M — the number of operations to the files. In the last M lines specify the operations that are requested for files. One file can be requested many times.
# You need to recover the control over the access rights to the files. For each request your program should return OK if the requested operation is valid or Access denied if the operation is invalid.

permissions = {}
n = int(input())
for _ in range(n):
    s = input().split()
    permissions[s[0]] = set(s[1:])
for _ in range(int(input())):
    perm, file = input().split()
    if perm == 'read':
        perm = 'R'
    if perm == 'write':
        perm = 'W'
    if perm == 'execute':
        perm = 'X'
    if perm in permissions[file]:
        print('OK')
    else:
        print('Access denied')

# Given a list of countries and cities of each country. Then given the names of the cities. For each city specify the country in which it is located.

n = int(input())
cities = {}
for _ in range(n):
    line = input().split()
    for city in line[1:]:
        cities[city] = line[0]
for _ in range(int(input())):
    print(cities[input()])

# Given a number n, followed by n lines of text, print all words encountered in the text, one per line. The words should be sorted in descending order according to their number of occurrences in the text, and all words with the same frequency should be printed in lexicographical order. Hint. After you create a dictionary of the words and their frequencies, you would like to sort it according to the frequencies. This can be achieved if you create a list whose elements are tuples of two elements: the frequency of occurrence of a word and the word itself. For example, [(2, 'hi'), (1, 'what'), (3, 'is')]. Then the standard list sort will sort a list of tuples, with the tuples compared by the first element, and if these are equal, by the second element. This is nearly what is required in the problem.

from collections import Counter
words = []
for _ in range(int(input())):
    words.extend(input().split())
counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))

# One day, going through old books in the attic, a student Bob found English-Latin dictionary. By that time he spoke English fluently, and his dream was to learn Latin. So finding the dictionary was just in time.
# Unfortunately, full-fledged language studying process requires also another type of dictionary: Latin-English. For lack of a better way he decided to make a second dictionary using the first one.
# As you know, the dictionary consists of words, each of which contains multiple translations. For each Latin word that appears anywhere in the dictionary, Bob has to find all its translations (that is, all English words, for which our Latin word is among its translations), and take them and only them as the translations of this Latin word.
# Help him to create a Latin-English.
# The first line contains a single integer N — the number of English words in the dictionary. Followed by N dictionary entries. Each entry is contained on a separate line, which contains first the English word, then a hyphen surrounded by spaces and then comma-separated list with the translations of this English word in Latin. All the words consist only of lowercase English letters. The translations are sorted in lexicographical order. The order of English words in the dictionary is also lexicographic.
# Print the corresponding Latin-English dictionary in the same format. In particular, the first word line should be the lexicographically minimal translation of the Latin word, then second in that order, etc. Inside the line the English words should be sorted also lexicographically.

from collections import defaultdict
lateng = defaultdict(list)
for i in range(int(input())):
    eng_word, lat_trans = input().split(' - ')
    lat_translations = lat_trans.split(', ')
    for lat_word in lat_translations:
        lateng[lat_word].append(eng_word)
print(len(lateng))
for lat_word, eng_translations in sorted(lateng.items()):
    print(lat_word + ' - ' + ', '.join(eng_translations))





