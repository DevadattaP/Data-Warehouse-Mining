import efficient_apriori
transactions = [['A', 'B', 'C'],
                ['A', 'C'],
                ['A', 'D'],
                ['B', 'E', 'F']]
item, rule = efficient_apriori.apriori(transactions)
print(item,'\n',rule)