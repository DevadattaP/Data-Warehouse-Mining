# define transaction set
# transactions = {'T100': {'I1', 'I2', 'I5'},
#                 'T200': {'I2', 'I4'},
#                 'T300': {'I2', 'I3'},
#                 'T400': {'I1', 'I2', 'I4'},
#                 'T500': {'I1', 'I3'},
#                 'T600': {'I2', 'I3'},
#                 'T700': {'I1', 'I3'},
#                 'T800': {'I1', 'I2', 'I3', 'I5'},
#                 'T900': {'I1', 'I2', 'I3'}
#                 }
#transactions = {'T1': {'A', 'B', 'C'},
  #              'T2': {'A', 'C'},
    #            'T3': {'A', 'D'},
      #          'T4': {'B', 'E', 'F'}}
transactions = {'T1':{'Bread', 'Jelly', 'Butter'},
                'T2':{'Bread', 'Butter'},
                'T3':{'Bread', 'Milk', 'Butter'},
                'T4':{'Coke','Bread'},
                'T5':{'Coke','Milk'}}
# define minimum support = 50%
min_support = 0.3
# define minimum confidence = 50%
min_confidence = 0.8
# find total number of transactions
total_transactions = len(transactions)
# find minimum support count
min_support_count = min_support * total_transactions
# min_support_count = 2
# find distinct items from transactions
item_sets = {}
for i in transactions:
    for j in transactions[i]:
        if j not in item_sets:
            item_sets[j] = 0
        item_sets[j] += 1
print('k = 1')
# apply minimum support count and keep only items of interest
l = {k: v for k, v in item_sets.items() if v >= min_support_count}
distinct = sorted(list(l.keys()))
item_freq = []
t = []
t.append(list(l.keys()))
t.append(list(l.values()))
item_freq.append(t)
print('L1 ==> Item sets \t Frequency')

for i in range(len(item_freq[0][0])):
    print('\t\t', item_freq[0][0][i], '\t\t', item_freq[0][1][i])
k = 2


def combinations(lst):
    # lst = the list from which we want to generate combinations
    # Initialize a list with an empty subset, representing the start of our combinations
    combination = [[]]
    # This loop structure is similar to the "combinations def powerset" concept, iterating through each element
    for element in lst:
        # For each existing combination, create a new combination that includes the current element
        for sub_set in combination.copy():
            new_sub_set = sub_set + [element]
            # Append the new combination to our list of combinations
            combination.append(new_sub_set)
    # take only combinations with length = k
    new_set = [set(com) for com in combination if len(com) == k]
    new_lst = []
    for i in new_set:
        for j in transactions.values():
            if i.issubset(j):
                new_lst.append(i)
    # print(new_lst)
    temp = []
    for i in new_lst:
        if i not in temp:
            temp.append(i)
    # print(temp)
    new_freq = []
    for i in temp:
        count = 0
        for j in new_lst:
            if j == i:
                count += 1
        new_freq.append(count)
    # print(new_freq)
    final_item = [temp[i] for i, item in enumerate(new_freq) if item >= min_support_count]
    final_freq = [x for x in new_freq if x >= min_support_count]
    # print(final_item, final_freq)
    # return new_set
    return [final_item, final_freq]


frequent_item_set = []
while len(distinct) >= k:
    new_item_set = combinations(distinct)
    item_set = new_item_set[0]
    frequency = new_item_set[1]
    print('k =', k)
    print(f'L{k} ==>  Item sets \t\t frequency')
    k += 1
    if item_set:
        item_freq.append(new_item_set)
        frequent_item_set = new_item_set
        for i in range(len(item_set)):
            print('\t\t', item_set[i], '\t:', frequency[i])
        distinct = []
        for i in item_set:
            for j in i:
                if j not in distinct:
                    distinct.append(j)
        # print(sorted(distinct))
    else:
        print('\t\tEmpty set\t\t----')
        break
items = frequent_item_set[0]
freq = frequent_item_set[1]
rules = []
print('Final Item Sets :\t Frequency')
for i in range(len(items)):
    print(items[i], '\t\t', freq[i])


def permutations(lst):
    # lst = the list from which we want to generate combinations
    # Initialize a list with an empty subset, representing the start of our combinations
    combination = [[]]
    # This loop structure is similar to the "combinations def powerset" concept, iterating through each element
    for element in lst:
        # For each existing combination, create a new combination that includes the current element
        for sub_set in combination.copy():
            new_sub_set = sub_set + [element]
            # Append the new combination to our list of combinations
            combination.append(new_sub_set)
    return combination


for i in range(len(items)):
    temp = permutations(items[i])[1:-1]
    support = freq[i] / len(transactions)
    print('Case', i + 1, ':')
    for j in range(len(temp)):
        left = set(temp[j])
        right = items[i] - set(temp[j])
        n = len(left)
        f = 0
        for m in range(len(item_freq[n-1][0])):
            if n == 1:
                if item_freq[n - 1][0][m] in left:
                    f = item_freq[n - 1][1][m]
            else:
                if item_freq[n-1][0][m] == left:
                    f = item_freq[n - 1][1][m]
        confidence = freq[i]/f
        print('Rule', j + 1, ':', left, '-->', right,
              f'\tSupport = {freq[i]}/{len(transactions)} = {round(support * 100, 2)} %',
              f'\tConfidence = {freq[i]}/{f} = {round(confidence * 100, 2)} %', end='')
        if confidence >= min_confidence:
            print('\tValid rule')
            rules.append([left, '-->', right])
        else:
            print()

print('\nAnswer:-')
print('Frequent Item Sets :\t Frequency')
for i in range(len(items)):
    print(items[i], '\t\t', freq[i])
print('\nStrong Association Rules:')
for i in rules:
    for j in i:
        print(j, end='')
    print()
