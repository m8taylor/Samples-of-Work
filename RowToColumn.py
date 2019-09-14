import csv
import pathlib

#open csv file
path = pathlib.Path('FileName.csv')
if path.exists() == True:

#initialize row-column array
    with open('FileName.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)

        RowColumn = [[] for row in reader if row != []]

# write to row-column array from csv file
    with open('FileName.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)

        j = 0
        for row in reader:
            if row != []:
                RowColumn[j] = RowColumn[j] + row
                j += 1

#transpose row-column array
RowColumnNew = [[RowColumn[i][j] for i in range(0, len(RowColumn))] for j in range(0, len(RowColumn[0]))]


##### This may need to be separated out because it is only cleaning data.
#switch columns 3 and 4
for i in range(0, len(RowColumnNew)):
    Temp2 = RowColumnNew[i][2]
    RowColumnNew[i][2] = RowColumnNew[i][3]
    RowColumnNew[i][3] = Temp2
#expand Size and Categories
    TempCategorySize = list(RowColumnNew[i][3])
    if '?' in TempCategorySize:
        index = TempCategorySize.index('?')
        RowColumnNew[i][3] = ''.join(TempCategorySize[index+1:])
        Categories = TempCategorySize[:index]
        while '-' in Categories:
            index = Categories.index('-')
            RowColumnNew[i] = RowColumnNew[i] + [''.join(Categories[:index])]
            Categories = Categories[index+1:]
        RowColumnNew[i] = RowColumnNew[i] + [''.join(Categories)]
    else:
        RowColumnNew[i] = RowColumnNew[i] + ['Missing','Missing']
#####end of stuff that may need to be separated out




#write to new csv file.  The rows and columns have been transposed.
with open('FileNameColumns.csv', mode='w') as FileNameColumns:
    csv_writer = csv.writer(FileNameColumns, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['id', 'Url','Sale_Price','Brand','Size','Category','Subcategory'])
    for i in range(0,len(RowColumnNew)):
        csv_writer.writerow([i] + RowColumnNew[i])
