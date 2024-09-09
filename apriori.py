adj = [[1, 1, 1, 0, 0, 0],
       [1, 0, 1, 0, 0, 0],
       [1, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 1, 1]]
total_transactions = len(adj)
min_support = 0.5 * total_transactions
min_confidence = 0.5
frequency_count = []
valid_count = []
valid_index = []
for i in range(len(adj[0])):
    count = 0
    for j in range(len(adj)):
        if adj[j][i] == 1:
            count += 1
    if count >= min_support:
        valid_count.append(1)
        valid_index.append(i)
    else:
        valid_count.append(0)
    frequency_count.append(count)
print(frequency_count)
print(valid_count)
print(valid_index)


def get_powerset(lst):
    if len(lst) == 0:
        return [[]]
    subset = []
    for partial_subset in get_powerset(lst[1:]):
        subset.append(partial_subset)
        subset.append(partial_subset[:] + [lst[0]])
    return subset


powerset = get_powerset(valid_index)
for i in powerset:
    i.reverse()
print(powerset)
iteration_2 = [i for i in powerset if len(i)==2]
print(iteration_2)
i2_freq_count = []
i2_valid_count = []
for i in iteration_2:
    count = 0
    for j in range(len(adj)):
        if adj[j][i[0]] == 1 and adj[j][i[1]]:
            count += 1
    if count >= min_support:
        i2_valid_count.append(1)
    else:
        valid_count.append(0)
    i2_freq_count.append(count)

print(i2_freq_count)
print(i2_valid_count)
final_list = iteration_2[valid_count[0]]
print(final_list)
rule_list = [final_list,[final_list[1], final_list[0]]]
print(rule_list)
