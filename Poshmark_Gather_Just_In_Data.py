from random import randint
import random

import time
import datetime

import threading
import logging


import requests
from bs4 import BeautifulSoup
from collections import Counter
import re


import os
import csv
import urllib.request
from urllib import request
import pathlib
import wget






##########################################################################


import sqlalchemy

from sqlalchemy import create_engine
# Postgres username, password, and database name
POSTGRES_ADDRESS = '127.0.0.1' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
POSTGRES_PORT = '5432'
POSTGRES_USERNAME = 'postgres' ## CHANGE THIS TO YOUR PANOPLY/POSTGRES USERNAME
POSTGRES_PASSWORD = 'Caboose325' ## CHANGE THIS TO YOUR PANOPLY/POSTGRES PASSWORD
POSTGRES_DBNAME = 'PoshSalesData' ## CHANGE THIS TO YOUR DATABASE NAME
# A long string that contains the necessary Postgres login information
postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(username=POSTGRES_USERNAME, password=POSTGRES_PASSWORD, ipaddress=POSTGRES_ADDRESS, port=POSTGRES_PORT,dbname=POSTGRES_DBNAME))

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import sessionmaker

from sqlalchemy import func

# Create the connection
cnx = create_engine(postgres_str)





##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################


def scrape(ETag):


    url = 'https://poshmark.com/category/Women'

#    print(ETag)

    if ETag == 0:
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-US,en;q=0.5',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Host':'poshmark.com',
            'Referrer': 'https://www.mozilla.org/en-US/',
            'TE':'Trailers',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
        }
    else:
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-US,en;q=0.5',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Host':'poshmark.com',
            'If-None-Match':'{}'.format(ETag),
            'Referrer': 'https://www.mozilla.org/en-US/',
            'TE':'Trailers',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
        }

#    print(headers)

    #Soupify
    result = requests.get(url, headers = headers)

    ETag = result.headers['ETag']

    src = result.content

    soup = BeautifulSoup(src, features="html5lib")


    #Get item details
    ItemDetails = soup.find_all("div", class_="item__details")

    #Get Pictures
    ItemPictures = soup.find_all('div', class_="img__container img__container--square")

    Urls = []
    Titles = []
    Conditions = []
    Sale_Prices = []
    Original_Prices = []
    Sizes = []
    Brands = []
    Super_Categories = []
    Categories = []
    Pictures = []

    m = len(ItemDetails)
    for k in range (0,m):

    #Get Url and Title
        Url_Title = ItemDetails[k].find_all("a", class_ = "tile__title tc--b")
        Url_Title = Url_Title[0]

        Url = Url_Title.attrs['href']
        Url = Url[9:]
        Urls.append(Url)

        Title = Url_Title.get_text()
        Title = Title.strip()
        Titles.append(Title)

    #Get Condition
        Condition = ItemDetails[k].find_all("span", class_ = "condition-tag all-caps tr--uppercase condition-tag--small")

        if Condition != []:
            Condition = Condition[0]
            Condition = Condition.get_text()
            Condition = Condition.strip()
        else:
            Condition = 'Used'

        Conditions.append(Condition)

    #Prices
        Sale_Price = ItemDetails[k].find_all("span", class_ = "p--t--1 fw--bold")
        Sale_Price = Sale_Price[0]
        Original_Price = ItemDetails[k].find_all("span", class_ = "p--l--1 tc--lg td--lt")
        Original_Price = Original_Price[0]

        Sale_Price = Sale_Price.contents
        Sale_Price = Sale_Price[0]
        Sale_Price = Sale_Price.strip()
        Sale_Price = re.sub('[$,]', '', Sale_Price)
        Sale_Price = int(Sale_Price)
        Sale_Prices.append(Sale_Price)

        Original_Price = Original_Price.get_text()
        Original_Price = Original_Price.strip()
        Original_Price = re.sub('[$,]', '', Original_Price)
        Original_Price = int(Original_Price)
        Original_Prices.append(Original_Price)


    #Categories and Size
        Categories_Sizes = ItemDetails[k].find_all(class_ = "tile__details__pipe__size ellipses")
        Categories_Sizes = Categories_Sizes[0]

    #Size
        Size = Categories_Sizes.get_text()
        Size = Size.strip()
        Size = Size[6:]
        Sizes.append(Size)

    #Categories
        if Categories_Sizes.has_attr('href'):
            Full_Category = Categories_Sizes.attrs['href']

            Full_Category = Full_Category.split('?')
            Full_Category = Full_Category[0]
            Full_Category = Full_Category[10:]
            Full_Category = Full_Category.split('-')

            Super_Category = Full_Category[0]
            Category = Full_Category[1]
        else:
            Super_Category = 'Unknown'
            Category = 'Unknown'



        Super_Categories.append(Super_Category)

        Categories.append(Category)



    #Brand
        Brand = ItemDetails[k].find_all(class_ = "tile__details__pipe__brand ellipses")
        if Brand != []:
            Brand = Brand[0]
            Brand = Brand.get_text()
            Brand = Brand.strip()
        else:
            Brand = 'No Brand'

        Brands.append(Brand)



    #Picture
        Item_Picture = ItemPictures[k].find_all('img')
        Item_Picture = Item_Picture[0]
        Picture_Url = Item_Picture.attrs['data-src']
        Picture_Split = Picture_Url.split('_')
        Picture_ID = Picture_Split[1]
        Picture_Date = re.search('[0-9]{4}/[0-9]{2}/[0-9]{2}/',Picture_Split[0])
        Picture_Date = Picture_Date.group(0)
        Picture_Details = Picture_Date + Picture_ID
        Pictures.append(Picture_Details)

    #Date
    DT = datetime.datetime.now()

    DT = DT.strftime("%Y-%m-%d %H:%M")



    Base = declarative_base()



    class User(Base):
        __tablename__ = 'just_in'

        id = Column(Integer, primary_key=True)
        url = Column(String)
        title = Column(String)
        condition = Column(String)
        sale_price = Column(Integer)
        original_price = Column(Integer)
        size = Column(String)
        brand = Column(String)
        super_category = Column(String)
        category = Column(String)
        picture = Column(String)
        date = Column(String)




    global cnx
    Session = sessionmaker(bind=cnx)

    session = Session()

    m = len(Urls)
    for k in range (0,m):
        session.add(User(url = Urls[k], title = Titles[k], condition = Conditions[k], sale_price = Sale_Prices[k], original_price = Original_Prices[k], size = Sizes[k], brand = Brands[k], super_category = Super_Categories[k], category = Categories[k], picture = Pictures[k], date = DT))


    session.commit()

###############
    if len(Urls) < 48:
        print(Urls)
###############
    return [ETag,Urls]













##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################






def Query_just_in_description():

    global cnx

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'just_in_description'

        id = Column(Integer, primary_key=True)
        just_in_id = Column(Integer)
        title = Column(String)
        description = Column(String)
        super_category = Column(String)
        category = Column(String)
        sub_category = Column(String)
        condition = Column(String)
        brand = Column(String)
        sale_price = Column(Integer)
        original_price = Column(Integer)
        date = Column(String)


    Session = sessionmaker(bind=cnx)

    session = Session()

    q = session.query(func.max(User.just_in_id))

    return q





##########################################################################
##########################################################################
##########################################################################
##########################################################################

def Query_just_in(ID):

    global cnx

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'just_in'

        id = Column(Integer, primary_key=True)
        url = Column(String)
        title = Column(String)
        condition = Column(String)
        sale_price = Column(Integer)
        original_price = Column(Integer)
        size = Column(String)
        brand = Column(String)
        super_category = Column(String)
        category = Column(String)
        picture = Column(String)
        date = Column(String)

    Session = sessionmaker(bind=cnx)

    session = Session()

    q = session.query(User.id, User.url)

    q = q.filter(User.id > ID)

    return q



##########################################################################
##########################################################################
##########################################################################
##########################################################################

def Write_just_in_description(IDs, Descriptions, Date_Times):

    global cnx

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'just_in_description'

        id = Column(Integer, primary_key=True)
        just_in_id = Column(Integer)
        title = Column(String)
        description = Column(String)
        super_category = Column(String)
        category = Column(String)
        sub_category = Column(String)
        condition = Column(String)
        brand = Column(String)
        sale_price = Column(Integer)
        original_price = Column(Integer)
        date = Column(String)


    Session = sessionmaker(bind=cnx)

    session = Session()

    m = len(IDs)
    for k in range (0,m):
        if Descriptions[k] == None:
            session.add(User(just_in_id = IDs[k], date = Date_Times[k]))
        else:
            session.add(User(just_in_id = IDs[k],
             title = Descriptions[k][0],
             description = Descriptions[k][1],
             super_category = Descriptions[k][2],
             category = Descriptions[k][3],
             sub_category = Descriptions[k][4],
             condition = Descriptions[k][5],
             brand = Descriptions[k][6],
             sale_price = Descriptions[k][7],
             original_price = Descriptions[k][8],
             date = Date_Times[k]))

    session.commit()


##########################################################################
##########################################################################
##########################################################################
##########################################################################

def Write_just_in_color(IDs, Colors):

    global cnx

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'just_in_color'

        id = Column(Integer, primary_key=True)
        just_in_id = Column(Integer)
        color = Column(String)


    Session = sessionmaker(bind=cnx)

    session = Session()

    m = len(IDs)
    for k in range (0,m):
        if Colors[k] != None:
            for color_ in Colors[k]:
                session.add(User(just_in_id = IDs[k],
                 color = color_))


    session.commit()


##########################################################################
##########################################################################
##########################################################################
##########################################################################

def Write_just_in_picture(IDs, Pictures):

    global cnx

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'just_in_picture'

        id = Column(Integer, primary_key=True)
        just_in_id = Column(Integer)
        picture = Column(String)


    Session = sessionmaker(bind=cnx)

    session = Session()

    m = len(IDs)
    for k in range (0,m):
        if Pictures[k] != None:
            for picture_ in Pictures[k]:
                session.add(User(just_in_id = IDs[k],
                 picture = picture_))


    session.commit()


##########################################################################
##########################################################################
##########################################################################
##########################################################################

def Write_just_in_size(IDs, Sizes):

    global cnx

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'just_in_size'

        id = Column(Integer, primary_key=True)
        just_in_id = Column(Integer)
        size = Column(String)


    Session = sessionmaker(bind=cnx)

    session = Session()

    m = len(IDs)
    for k in range (0,m):
        if Sizes[k] != None:
            for size_ in Sizes[k]:
                session.add(User(just_in_id = IDs[k],
                 size = size_))


    session.commit()








##########################################################################
##########################################################################
##########################################################################
##########################################################################

def Parse(Url, Headers):

#Soupify
    result = requests.get(Url, headers = Headers)

    src = result.content

    soup = BeautifulSoup(src, features="html5lib")


###################
#Get Sold Out, Title and Prices
    Title_Price = soup.find_all("h1")

    if Title_Price == []:
        return None

    if len(Title_Price) > 2:

        Title_Price = Title_Price[1:]


    Sale_Price = Title_Price[1].contents[0]
    Sale_Price = Sale_Price.strip()
    Sale_Price = re.sub('[$,]', '', Sale_Price)
    Sale_Price = int(Sale_Price)

    Original_Price = Title_Price[1].contents[1]
    Original_Price = Original_Price.get_text().strip()
    Original_Price = re.sub('[$,]', '', Original_Price)
    Original_Price = int(Original_Price)


    Title = Title_Price[0].contents[0]
    Title = Title.strip()



###################
#Get Pictures
    Pictures = []

    Image_Url_Tags = soup.find_all("img", class_="")


    for tag in Image_Url_Tags:
        Picture_Url = tag.attrs['data-src']
        Picture_Split = Picture_Url.split('_')
        Picture_ID = Picture_Split[1]
        Picture_Date = re.search('[0-9]{4}/[0-9]{2}/[0-9]{2}/',Picture_Split[0])
        Picture_Date = Picture_Date.group(0)
        Picture_Details = Picture_Date + Picture_ID
        Pictures.append(Picture_Details)

    Pictures = list(dict.fromkeys(Pictures))


###################
#Get Description
    Description = soup.find_all("div", class_="listing__description fw--light")[0].contents[0]
    Description = Description.strip()



###################
#Get Categories and Colors
    Categories_Colors = soup.find_all("div", class_="m--t--3 m--r--7")


    Categories = Categories_Colors[0].findChildren("a" , recursive=False)

    Super_Category = Categories[0].contents[0]
    Super_Category = Super_Category.strip()

    Category = Categories[1].contents[0]
    Category = Category.strip()

    if len(Categories) == 3:
        Sub_Category = Categories[2].contents[0]
        Sub_Category = Sub_Category.strip()
    else:
        Sub_Category = ''

    Colors = []
    if len(Categories_Colors) == 2:
        Color_Tags = Categories_Colors[1].findChildren("a" , recursive=False)
        for tag in Color_Tags:
            Color = tag.contents[1]
            Color = Color.strip()
            Colors.append(Color)

###################
#Get Condition

    Condition = soup.find_all("span", class_="condition-tag all-caps tr--uppercase")
    if Condition != []:
        Condition = Condition[0].contents[0]
        Condition = Condition.strip()
    else:
        Condition = 'Used'



###################
#Get Brand

    Brand = soup.find_all("a", class_="listing__brand listing__ipad-centered d--fl m--t--2")
    if Brand != []:
        Brand = Brand[0].get_text().strip()

    else:
        Brand = ''





###################
#Get Sizes

    Size_Tags = soup.find_all("button", class_="size-selector__size-option btn btn--tertiary")


    Sizes = []
    for tag in Size_Tags:
        tag = tag.get_text()
        Sizes.append(tag.strip())


    Sold_Out_Tags = soup.find_all("span", class_="td--st")

    Sold_Out_Sizes = []
    for tag in Sold_Out_Tags:
        tag = tag.get_text()
        Sold_Out_Sizes.append(tag.strip())

    Sold_Out_Sizes = list(dict.fromkeys(Sold_Out_Sizes))


    Available_Sizes = ['a_' + x for x in Sizes if x not in Sold_Out_Sizes]
    Available_Sizes = list(dict.fromkeys(Available_Sizes))

    #add the s_ tag to sold out sizes
    Sold_Out_Sizes = ['s_' + x for x in Sold_Out_Sizes]


    Sizes = Available_Sizes + Sold_Out_Sizes


    return [[Title, Description, Super_Category, Category, Sub_Category, Condition, Brand, Sale_Price, Original_Price], Colors, Pictures, Sizes]









##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################
##########################################################################




Just_In_Priority = 0
Listing_Priority = 0



def Scrape_Just_In():

    global Just_In_Priority
    global Listing_Priority

    New_Urls = []
    ETag = 0
    delay = 50



    while True:

        Just_In_Priority = 1

        time.sleep(0.5)

        if Listing_Priority == 1:
            Just_In_Priority = 0

            while Listing_Priority == 1:
                time.sleep(1)

            Just_In_Priority = 1

        logging.info("Scraping just in listings")


    #    print(ETag)
        Old_Urls = New_Urls
        [ETag,New_Urls] = scrape(ETag)

        time.sleep(10)

        Just_In_Priority = 0


        Different_Urls = [x for x in New_Urls if x not in Old_Urls]

        t = 47.9 - len(Different_Urls)
        if t > 1:
            t = 1

        delay += t
        if delay < 50:
            delay = 50
        if delay > 120:
            delay = 120


        a = random.gauss(delay, 5)
        if a < 5:
            a = 5
        if a > 140:
            a = 140
#        print(ETag,t,a)
        time.sleep(a)




##########################################################################
##########################################################################
##########################################################################
##########################################################################


def Scrape_Listing():


    global Just_In_Priority
    global Listing_Priority

    ##########################################################################


    Headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-US,en;q=0.5',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'poshmark.com',
        'Referrer': 'https://www.mozilla.org/en-US/',
        'TE':'Trailers',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
    }


    ID = Query_just_in_description()[0][0]
    if ID == None:
        ID = 0

    IDs_Urls = Query_just_in(ID).all()


    i = 0
    IDs = []
    Descriptions = []
    Colors = []
    Pictures = []
    Sizes = []
    Date_Times = []

    for id_url in IDs_Urls:

        IDs.append(id_url[0])

        Listing_Priority = 1

        while Just_In_Priority == 1:
            time.sleep(1)

        logging.info("Scraping individual listing")


        Url = 'https://poshmark.com/listing/' + id_url[1]

        data = Parse(Url, Headers)

        time.sleep(8)

        Listing_Priority = 0

        if data == None:
            Descriptions.append(None)
            Colors.append(None)
            Pictures.append(None)
            Sizes.append(None)
        else:
            Descriptions.append(data[0])
            Colors.append(data[1])
            Pictures.append(data[2])
            Sizes.append(data[3])

        #Date
        date_time = datetime.datetime.now()
        date_time = date_time.strftime("%Y-%m-%d %H:%M")

        Date_Times.append(date_time)



        i += 1
        if i == 10:
            logging.info("Committing data")
            #commit to database
            Write_just_in_description(IDs, Descriptions, Date_Times)
            Write_just_in_color(IDs, Colors)
            Write_just_in_picture(IDs, Pictures)
            Write_just_in_size(IDs, Sizes)

            i = 0
            IDs = []
            Descriptions = []
            Colors = []
            Pictures = []
            Sizes = []
            Date_Times = []


        a = random.gauss(8, 3)
        if a < 0:
            a = 0
        if a > 16:
            a = 16
#        print(a)
        time.sleep(a)








##########################################################################
##########################################################################
##########################################################################
##########################################################################

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    y = threading.Thread(target=Scrape_Listing, args=())
    y.start()

    time.sleep(randint(13,19))

    x = threading.Thread(target=Scrape_Just_In, args=())
    x.start()

##########################################################################
##########################################################################
##########################################################################
##########################################################################



if __name__ == '__main__':
    main()
