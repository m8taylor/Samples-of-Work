import DataParser
import time
import random
import csv
from collections import Counter
import pathlib


url = 'https://your-url.com/parameters'

Data = DataParser.dataparser(url)


#Get relevant sales data from the html pasrsing
Title = Data[0]
Price = Data[1]
Size = Data[2]
Brand = Data[3]
Words =  Data[4]


#write sales data to file
with open('FileName.csv', mode='a') as FileName:
    csv_writer = csv.writer(FileName, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(Title)
    csv_writer.writerow(Price)
    csv_writer.writerow(Size)
    csv_writer.writerow(Brand)



#check to see if the keyword file exists
path = pathlib.Path('FileNameWords.csv')
if path.exists() == True:

#if the keywords file exists, get the data from it
    with open('FileNameWords.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        wordFreqDic = {}
        for row in reader:
            if row != []:
                wordFreqDic.update( {row[0] : int(row[1])})


#combine the keywords from the csv file with the ones extracted from the html
    Words =  Counter(Words) + Counter(wordFreqDic)

#write to keyword csv file

csv_writer = csv.writer(open("FileNameWords.csv", 'w'))
for key, val in Words.items():
    csv_writer.writerow([key, val])
