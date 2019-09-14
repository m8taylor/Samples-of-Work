import csv
import pathlib




#open csv file
path = pathlib.Path('FileName.csv')
if path.exists() == True:

    with open('FileName.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)

        ConcatenatedRow1 = []
        ConcatenatedRow2 = []
        ConcatenatedRow3 = []
        ConcatenatedRow4 = []

        j = 0

        for row in reader:
            if j%8 == 0:
                ConcatenatedRow1 = ConcatenatedRow1 + row

            if j%8 == 2:
                ConcatenatedRow2 = ConcatenatedRow2 + row

            if j%8 == 4:
                ConcatenatedRow3 = ConcatenatedRow3 + row

            if j%8 == 6:
                ConcatenatedRow4 = ConcatenatedRow4 + row

            j += 1




#write to csv file

with open('FileName.csv', mode='w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(ConcatenatedRow1)
    csv_writer.writerow(ConcatenatedRow2)
    csv_writer.writerow(ConcatenatedRow3)
    csv_writer.writerow(ConcatenatedRow4)
