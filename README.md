# Web Scraping and Database Construction

    Datagather.py scrapes a webpage and sends the scraped data to a SQL database.
    
    The database is broken up in to 3 tables: Items, Url Words, and the table connecting Items and Words.  See SalesDataLessBig.csv, Word.csv and Word_Id.csv 
    
# Machine Learning - Price Prediction via Url Keywords
    
    We are going to work with the information in SalesDataLessBig.csv, which contains ~22000 distinct observations.  The column keys are: Id, Url, Sale Price, Brand, Size, Subcategory. The Category is Women for all the items, so I haven't included it.
    
    My initial workflow is: based on the words in the *urls* in SalesDataLessBig.csv, predict the *sales prices* of items to within 30% relative error at least 70% of the time.
    
    Every distinct url word is treated as a separate feature, so we use One_Hot_Encode.py to handle that part of the preprocessing.  The necessary csv files for encoding are: Id, Word, Word_Id, and Prices.
    *WARNING!!!!* one hot encoding with these files will produce a 0.5 GB size file
    
    Cleaning is still ongoing.  Datagather.py is set up to do a little bit, but more needs to be done.
    
    
  

# Share.py and Follow.py can be used to interface with webpages, without utilizing Selenium

    Alarm.py sets off an alarm if something goes wrong.  This helps to catch bugs.
    
    To utilize these files, set your screen resolution to 1366 x 768 and open Firefox.  Make sure your developer console is docked right and has its leftmost edge at x = 850.

# GatherDataOld.py was one of the *main* files I use for html parsing

    DataParserOld.py extracts and returns html data.

    WordSortBegin.py extracts and returns keywords from urls.

# Older Files

    CSVRowReduced.py reduces the number of rows in a csv file.

    RowToColumn.py transposes the rows and columns in a csv file.
    
    RandomSample.csv was too small for my taste.
