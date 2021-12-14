with open("input.txt") as file:
    data = file.read().splitlines()
polymer = data[0]
rules = data[2:]
rules_dict = {}

for i, rule in enumerate(rules):
    rules[i] = rule.split(" -> ")
    rules_dict[rules[i][0]] = rules[i][1]

polymer_pairs = {}
for i in range(len(polymer) - 1):
    pair = polymer[i] + polymer[i+1]
    if pair in polymer_pairs:
        polymer_pairs[pair] += 1
    else:
        polymer_pairs[pair] = 1

step = 0

while step < 40:
    step +=1
    polymer_pairs_2 = {}
    for i, key in enumerate(polymer_pairs):
        new_letter = rules_dict[key]

        new_pair = key[0] + new_letter
        new_pair_2 = new_letter + key[1]
        if new_pair in polymer_pairs_2:
            polymer_pairs_2[new_pair] += 1 * polymer_pairs[key]
        else:
            polymer_pairs_2[new_pair] = 1 * polymer_pairs[key]

        if new_pair_2 in polymer_pairs_2:
            polymer_pairs_2[new_pair_2] += 1 * polymer_pairs[key]
        else:
            polymer_pairs_2[new_pair_2] = 1 * polymer_pairs[key]

        if i == len(polymer_pairs) - 1:
            letters_occurrence = {key[1] : 1}
        else:
            letters_occurrence = {}

    polymer_pairs = polymer_pairs_2


for key in polymer_pairs:
    if key[0] in letters_occurrence:
        letters_occurrence[key[0]] += polymer_pairs[key]
    else:
        letters_occurrence[key[0]] = polymer_pairs[key]

maximum = letters_occurrence[list(letters_occurrence.keys())[0]]
minimum = letters_occurrence[list(letters_occurrence.keys())[0]]

for letter in letters_occurrence:
    if letters_occurrence[letter] > maximum :
        maximum = letters_occurrence[letter]
    elif letters_occurrence[letter] < minimum :
        minimum = letters_occurrence[letter]

print(maximum - minimum)