# ... Sets ...

# Given a list of integers. Determine how many distinct numbers there are. This task can be solved in one line of code.

print(len(set(input().split())))

# Given two lists of numbers. Count how many unique numbers occur in both of them. This task can be solved in one line of code.

print(len(set(input().split()) & set(input().split())))

# Given two lists of numbers. Find all the numbers that occur in both the first and the second list and print them in ascending order. Even this task can be solved in one line of code.

a = set(input().split()) & set(input().split())
b = []
for i in a:
    b.append(int(i))
b.sort()
print(" ".join(str(i) for i in b))

# Given a sequence of numbers, determine if the next number has already been encountered. For each number, print the word YES (in a separate line) if this number has already been encountered, and print NO, if it has not already been encountered.

numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)

# Alice and Bob like to play with colored cubes. Each child has its own set of cubes and each cube has a distinct color, but they want to know how many unique colors exist if they combine their block sets. To determine this, the kids enumerated each distinct color with a random number from 0 to 108. At this point their enthusiasm dried up, and you are invited to help them finish the task.Given two integers that indicate the number of blocks in Alice's and then Bob's sets N and M. The following N lines contain the numerical color value for each cube in Alice's set. Then the last M rows contain the numberical color value for each cube in Bob's set.
# Find three sets: the numerical colors of cubes in both sets, the numerical colors of cubes only in Alice's set, and the numerical colors of cubes only in Bob's set. For each set, print the number of elements in the set, followed by the numerical color elements, sorted in ascending order.

def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])
N, M = [int(s) for s in input().split()]
A_colors, B_colors = set(), set()
for i in range(N):
    A_colors.add(int(input()))
for i in range(M):
    B_colors.add(int(input()))
print_set(A_colors & B_colors)
print_set(A_colors - B_colors)
print_set(B_colors - A_colors)

# Given a number n, followed by n lines of text, print the number of distinct words that appear in the text. For this, we define a word to be a sequence of non-whitespace characters, seperated by one or more whitespace or newline characters. Punctuation marks are part of a word, in this definition.

words = set()
for _ in range(int(input())):
    words.update(input().split())
print(len(words))

# Augustus and Beatrice play the following game. Augustus thinks of a secret integer number from 1 to n. Beatrice tries to guess the number by providing a set of integers. Augustus answers YES if his secret number exists in the provided set, or NO, if his number does not exist in the provided numbers. Then after a few questions Beatrice, totally confused, asks you to help her determine Augustus's secret number. Given the value of n in the first line, followed by the a sequence Beatrice's guesses, series of numbers seperated by spaces and Agustus's responses, or Beatrice's plea for HELP. When Beatrice calls for help, provide a list of all the remaining possible secret numbers, in ascending order, separated by a space.

n = int(input())
a = [i for i in range(1,n+1)]
s = set(a)
while True:
    guess = input()
    if guess == 'HELP':
        break
    answer = input()
    if answer == 'NO':
        s -= set(guess.split())
    elif answer == 'YES':
        s &= set(guess.split())
print(' '.join([str(i) for i in list(s)]))

# Each student at a certain school speaks a number of languages. We need to determine which languges are spoken by all the students, which languages are spoken by at least one student. Given, the number of students, and then for each student given the number of languages they speak followed by the name of each language spoken, find and print the number of languages spoken by all the students, followed by a list the languages by name, then print the number of languages spoken by at least one student, followed by the list of the languages by name. Print the languages in alphabetical order.

n = int(input())
num = [0] * n
langs = []
for i in range(n):
    num[i] = int(input())
    lang = set()
    for j in range(num[i]):
        lang.add(input())
    langs.append(lang)
uni = set.union(*langs)
inter = set.intersection(*langs)
print(len(inter))
print("\n".join(sorted(inter)))
print(len(uni))
print("\n".join(sorted(uni)))

