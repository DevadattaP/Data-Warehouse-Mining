heading = ['Color', 'Legs', 'Height', 'Smelly']
given_data = [['White', 3, 'Short', 'Yes', 'M'],
              ['Green', 2, 'Tall', 'No', 'M'],
              ['Green', 3, 'Short', 'Yes', 'M'],
              ['White', 3, 'Short', 'Yes', 'M'],
              ['Green', 2, 'Short', 'No', 'H'],
              ['White', 2, 'Tall', 'No', 'H'],
              ['White', 2, 'Tall', 'No', 'H'],
              ['White', 2, 'Short', 'Yes', 'H']]


def priorProbability(species):
    count = 0
    for i in given_data:
        if i[4] == species:
            count = count + 1
    return count / len(given_data)


def conditionalProbability(property, value, species):
    count1, count2 = 0, 0
    for i in given_data:
        if i[4] == species:
            count2 = count2 + 1
            if i[heading.index(property)] == value:
                count1 = count1 + 1
    return count1 / count2


def instanceProbability(species, instance):
    probability = priorProbability(species)
    for i in range(len(heading)):
        probability = probability * conditionalProbability(heading[i], instance[i], species)
    return probability


# instance = ['Green', 2, 'Tall', 'No']
print("Enter information of new instance- \n Color(White/Green), Legs(2/3), Height(Short/Tall), Smelly(Yes/No)\n")
instance = []
for i in range(len(heading)):
    newInstance = input(heading[i] + ' = ')
    if i == 1:
        newInstance = int(newInstance)
    instance.append(newInstance)

print("New instance = ", instance)

probability1 = instanceProbability('M', instance)
probability2 = instanceProbability('H', instance)
print("Probability(M/Instance) = ", probability1, "\nProbability(H/Instance) = ", probability2)
if probability1 > probability2:
    print("New instance belongs to species M.")
else:
    print("New instance belongs to species H.")
