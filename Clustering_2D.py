import math

n = int(input("Enter data size: "))
dataset = []
for i in range(n):
    dataset.append(list(map(int, input(f"Enter datapoint {i+1} : ").split())))
k = int(input("Enter number of clusters: "))
clusters = []
centroids = []
for i in range(k):
    centroids.append(list(map(int, input(f"Enter centroid {i+1} : ").split())))
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
            temp_list.append(math.dist(centroids[j], dataset[i]))
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
        x, y = 0, 0
        for j in new_clusters[i]:
            x += j[0]
            y += j[1]
        centroids[i] = [x/len(new_clusters[i]), y/len(new_clusters[i])]
