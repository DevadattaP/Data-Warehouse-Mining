def get_powerset(lst):
    if len(lst) == 0:
        return [[]]
    subset = []
    for partial_subset in get_powerset(lst[1:]):
        subset.append(partial_subset)
        subset.append(partial_subset[:] + [lst[0]])
    return subset


transactions = [['A', 'B', 'C'],
                ['A', 'C'],
                ['A', 'D'],
                ['B', 'E', 'F']]
min_support = 0.5
min_confidence = 0.5
total_transactions = len(transactions)
min_support_count = min_support * total_transactions
item_sets = []
for i in transactions:
    for j in range(len(i)):
        if i[j] not in item_sets:
            item_sets.append(i[j])
# print(item_sets)
k = 1

# for k = 1
p1 = get_powerset(item_sets)
# print(p1)
out = []
for i in p1:
    if len(i) == 1:
        out.append(i)
print(out)


temp = [j for i in transactions for j in i]
# print(temp)
freq = []
l = []
for i in item_sets:
    count = 0
    for item in temp:
        if item == i:
            count += 1
    freq.append(count)
    print(i, count)
    # applying min support count, find L
    if count >= min_support_count:
        l.append(i)
print(l)

# for k = 2
powerset = get_powerset(l)
for i in powerset:
    i.reverse()
# print(powerset)
out = []
for i in powerset:
    if len(i) == 2:
        out.append(i)
print(out)
new_item_set = []
for i in out:
    for j in transactions:
        if (all(x in j for x in i)):
            print(i)
            new_item_set.append(i)

print(new_item_set)
temp = []
for i in new_item_set:
    if i not in temp:
        temp.append(i)
print(temp)
new_freq = []
for i in temp:
    count = 0
    for j in new_item_set:
        if j == i:
            count += 1
    new_freq.append(count)
    if count >= min_support_count:
        print(i,count)
print(temp, new_freq)