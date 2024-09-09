import random

n = int(input("Enter data size: "))
dataset = list(map(int, input("Enter data : ").split(maxsplit=n-1)))
k = int(input("Enter number of clusters: "))
print()
clusters = []
centroids = random.sample(dataset, k=k)
centroids.sort()
status = False
counter = 0
while not status:
    counter += 1
    print("Interation ", counter)
    print("Centroids : ", centroids)
    differences = []
    for i in range(n):
        temp_list = []
        for j in range(k):
            temp_list.append(abs(dataset[i] - centroids[j]))
        differences.append(temp_list)
    min_index = []
    for i in range(n):
        min_index.append(differences[i].index(min(differences[i])))
    print("New clusters:")
    new_clusters = []
    for i in range(k):
        temp_list = []
        for j in range(n):
            if min_index[j] == i:
                temp_list.append(dataset[j])
        new_clusters.append(temp_list)
        print("K", i+1, " = ", temp_list)
    print()
    if counter != 1 and new_clusters == clusters:
        status = True
    clusters = new_clusters
    for i in range(k):
        centroids[i] = sum(new_clusters[i])/len(new_clusters[i])
