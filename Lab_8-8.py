#Lab_8-8

Rows= [['will', 'john', 'clegg', 'max'],
['Ethan', 'Brian', 'Alex', 'Riley'],
['Zaza', 'Brendan', 'Mia', 'Emma']]

for row in Rows:
    for name in row:
        if name [-1] == "s":
            name += "'"
        else:
            name += "'s"
            print (name)