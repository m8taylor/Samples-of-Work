import requests
from bs4 import BeautifulSoup
from collections import Counter

url = 'Your_Url'


#Soupify
result = requests.get(url)

src = result.content

soup = BeautifulSoup(src, features="html.parser")


#Get all item details
ItemDetails = soup.find_all("div", class_="item-details")



Titles = []
Prices = []
Sizes = []
Categories = []
SubCategories = []
Brands = []


k = 0

#There are up to 48 usable items on the page that was scraped above

while k < 48:

#Gather title details
    TitleCondition = ItemDetails[k].find_all("div", class_ = "title-condition-con d-fl ai-fs jc-sb")
#Gather details that may exclude an item
    ExcludeNWT = ItemDetails[k].find_all("div", class_ = "condition dark-grey d-fl ai-c")
    TemporaryBrand = ItemDetails[k].find_all("li", class_ = "brand")


#exclude for word bundle

    for a_tag in TitleCondition:
        Lower = a_tag.get_text().lower()
        if 'bundle' in Lower:
            Bundle = Lower
        else:
            Bundle = []

    if ExcludeNWT == [] and Bundle == [] and TemporaryBrand != []:


#Title Info and web address
        for a_tag in TitleCondition:
            TitleCondition1 = a_tag.find('a').attrs['href']
            Titles.append(TitleCondition1[9:])

#Price
        TemporaryPrice = ItemDetails[k].find_all("div", class_ = "price")
        for div_tag in TemporaryPrice:
        
            i = 1
            TemporaryPrice1 = div_tag.get_text("$")
            while TemporaryPrice1[i] != "$" and TemporaryPrice1[i] != "\xa0":
                i += 1
            if ',' in TemporaryPrice1[1:i]:
                index = TemporaryPrice1.index(',')
                TemporaryPrice1 = int(str(TemporaryPrice1[1:index]) + str(TemporaryPrice1[index+1:i]))
                Prices.append(TemporaryPrice1)
            else:
                Prices.append(int(TemporaryPrice1[1:i]))     
                
            


#Size and Category
        TemporarySize = ItemDetails[k].find_all("li", attrs = "href", class_ = "size")

        for a_tag in TemporarySize:
            if a_tag.find('a') != None:
                TemporarySize1 = a_tag.find('a').attrs['href']
                TemporarySize1 = list(TemporarySize1[10:])

                if '?' in TemporarySize1:
                    index = TemporarySize1.index('?')
                    
                    Size1 = TemporarySize1[index+6:]
                    Size1 = ''.join(Size1)
                    Sizes.append(Size1)

                    Category = TemporarySize1[:index]
                    
                    if '-' in Category:
                        index = Category.index('-')
                        Categories = Categories + [''.join(Category[:index])]
                        SubCategories = SubCategories + [''.join(Category[index+1:])]
                        
                        
            else:
                Sizes.append('Missing')
                Categories.append('Missing')
                SubCategories.append('Missing')
                    
            

#Brand
        for a_tag in TemporaryBrand:
            TemporaryBrand1 = a_tag.find('a').attrs['title']
            Brands.append(TemporaryBrand1)


    k += 1




#Prepare for SQL, PostgreSQL in this case

import sqlalchemy


from sqlalchemy import create_engine
# Postgres username, password, and database name
POSTGRES_ADDRESS = '127.0.0.1' ## Inset DB address, in this case localhost
POSTGRES_PORT = '5432'
POSTGRES_USERNAME = 'postgres' ## Postgres username
POSTGRES_PASSWORD = '*****' ## Postgr password
POSTGRES_DBNAME = 'Database Name' ## Database name
# A long string that contains the necessary Postgres login information
postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(username=POSTGRES_USERNAME, password=POSTGRES_PASSWORD, ipaddress=POSTGRES_ADDRESS, port=POSTGRES_PORT,dbname=POSTGRES_DBNAME))
# Create the connection
cnx = create_engine(postgres_str)


#Creating table to send to SQL server

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    sale_price = Column(Integer)
    brand = Column(String)
    size = Column(String)
    category = Column(String)
    subcategory = Column(String) 





#Inserting scraped datainto the table we just created

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=cnx)

session = Session()

for i in range (0,len(Prices)):
    session.add(User(url = Titles[i], sale_price = Prices[i], brand = Brands[i], size = Sizes[i], category = Categories[i], subcategory = SubCategories[i]))

#Commiting filled table to SQL.  A primary key id is automatically added to each instance that is added.

session.commit()







