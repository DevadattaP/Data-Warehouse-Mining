# matrix representation of given graph
adj = [[0, 1, 1, 0],
       [0, 0, 0, 1],
       [1, 1, 0, 1],
       [0, 0, 1, 0]]
n = len(adj)    # total number of nodes
count = 0
ranks = []
incoming_edges = []
outgoing_edges = []
# finding incoming edges for each node
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(adj[j][i])
    incoming_edges.append(temp)
# finding number of outgoing edges from each node
for i in adj:
    total = 0
    for j in i:
        if j == 1:
            total += 1
    outgoing_edges.append(total)
# run algorithm n-1 times
while count < n-1:
    count += 1
    # for very first iteration, rank = 1/n for each node
    if count == 1:
        for i in range(n):
            ranks.append(1 / n)
    # from 2nd iteration onwards,
    # use ranks from previous iterations to calculate the new ones
    else:
        new_page_ranks = []
        # PR(X) = sum |  rank of node Y which is incident to X  |
        #             | --------------------------------------- |
        #             |     no. of outgoing edges from Y        |
        for i in incoming_edges:
            page_rank = 0
            for j in range(n):
                # for every inbound node of a node,
                # add ratio of rank/edges to get final rank
                if i[j] == 1:
                    page_rank += ranks[j]/outgoing_edges[j]
            new_page_ranks.append(page_rank)
        ranks = new_page_ranks
    print(f'Ranks in iteration {count}: ', ranks)
print()
# assign ranks according to the ascending order of page ranks
assigned_ranks = sorted(range(n), key=lambda index: ranks[index])
for i in range(n):
    print(f'Node {chr(i + 65)} - Rank {assigned_ranks[i] + 1} : ({round(ranks[i], 4)})')
