# Web Scraping and Database Construction

    Datagather.py scrapes a webpage and sends the scraped data to a SQL database.
    
    The database is broken up in to 3 tables: Items, Url Words, and the table connecting Items and Words.  See
    SalesDataSmaller.csv, Word.csv and Word_Id.csv 
    
# Machine Learning - Price Prediction via Url Keywords
    
    We are going to work with the information in SalesDataSmaller.csv, which contains ~22000 distinct observations
    of clothing that has sold recently. The column keys are: Id, Url, Sale Price, Brand, Size, Subcategory. The
    Category is Women for all the items, so we don't need to include it.
    
    My initial workflow is: based on the words in the urls in SalesDataSmaller.csv, predict the sales prices of items
    to within 30% relative error at least 70% of the time.
    
    Every distinct word in urls is treated as a separate feature, so we use One_Hot_Encode.py to handle that part of
    the preprocessing.  The necessary csv files for encoding are: Id, Word, Word_Id, and Prices.
    !!!!WARNING!!!! one hot encoding with these files will produce a 0.5 GB sized file
    
    Cleaning is an interesting problem because new url words will show up as more samples are collected.  Words get
    misspelled, abbreviated or clumped together.  Also, these url words are not exactly individual units - their
    combinations have meaning.  My next project is focusing on how to properly use / clean these words.
    
    We are going to use Ridge Regression because we have a "medium" number of observations, ~20000, and because we
    are *ASSUMING* that a large number of features are relevant.  This assumptions is reasonable since most of the
    urls contain the clothing brand. 
    
    Ridge_Model.py trains the model.  The coding was done in Jupyter Notebook.  An alpha of about 1 seems to do a
    decent job.  The data is very sparse, so the training took less than 3 minutes.  The raw results are in
    Ridge_Results.csv.  
    
    The next steps are to collect more data and do more cleaning.

# Deep Learning - Automated Data Cleaning

    The "sentences" in SalesDataSmaller.csv have a syntax that's similar to the English language.  The sentence in
    the first entry of SalesDataSmaller.csv is "JCrew Metallic Striped Sweater."
   
    The idea is to generate many correct sentences and randomly insert errors into those sentences.  This gives us
    clean and dirty data to work with.


# Share.py and Follow.py can be used to Interface with Webpages, without Utilizing Selenium

    Alarm.py sets off an alarm if something goes wrong.  This helps to catch bugs.
    
    To utilize these files, set your screen resolution to 1366 x 768 and open Firefox.  Make sure your developer
    console is docked right and has its leftmost edge at x = 850.

# Older Files

    GatherDataOld.py was one of the files I used for html parsing.

    DataParserOld.py extracts and returns html data.

    WordSortBegin.py extracts and returns keywords from urls.

    CSVRowReduced.py reduces the number of rows in a csv file.

    RowToColumn.py transposes the rows and columns in a csv file.
    
    RandomSample.csv was too small.
