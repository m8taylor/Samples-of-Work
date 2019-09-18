import csv
import pathlib



columns = []

with open('Word.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        columns += row

columns = ['item'] + columns[1:]

#print(len(columns))



rows = []


with open('Id.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rows += row

rows = rows[1:]

#print(rows[:5])

#print(rows)
#print(len(rows))


table = [columns] + [[rows[i]] + [0 for j in range (0,len(columns)-1)] for i in range (0,len(rows))]

#print(table[1][1])



rows_cols = []
n = 0

with open('Word_Id.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rows_cols += [row]
#    print(rows_cols)


rows_cols = rows_cols[1:]




#print(rows_cols)
#print(rows_cols[:5])

j = 1
#l = len(rows_cols)
#r = len(rows)

for k in range (0, len(rows_cols) - 1):
    i = 0
    while True:
        if rows[i] == rows_cols[k][1]:
            table[i+1][j] += 1
#            print(table[i+1][j])
            break
        i += 1

    if rows_cols[k][0] != rows_cols[k+1][0]:
        j += 1
#        print(j)


i = 0
while True:
    if rows[i] == rows_cols[len(rows_cols) - 1][1]:
        table[i+1][j] += 1
        break
    i += 1


prices = []
n = 0

with open('Prices.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        prices += [row]
#    print(rows_cols)



for i in range (0,len(table)):
    table[i] += prices[i]



w = csv.writer(open("Sales_Table.csv", 'w'))
for i in range(0,len(table)):
    w.writerow(table[i])
