def dataparser(url):
    import requests
    from bs4 import BeautifulSoup
    import WordSortBegin
    from collections import Counter





#Soupify
    result = requests.get(url)

    src = result.content

    soup = BeautifulSoup(src, features="html.parser")

#Get item details
    ItemDetails = soup.find_all("div", class_="item-details")



    Titles = []
    Prices = []
    Sizes = []
    Categories = []
    Brands = []
    Words = {}


    k = 0

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
#get words
                Words = Counter(WordSortBegin.word_count(TitleCondition1[9:])) + Counter(Words)


#Price
            TemporaryPrice = ItemDetails[k].find_all("div", class_ = "price")
            TemporaryPrice1 = 0
            for div_tag in TemporaryPrice:
                i = 1
                while div_tag.get_text("$")[i] != "$" and div_tag.get_text("$")[i] != "\xa0":
                    i += 1
                i -= 1
                j = i
                while i > 0:
                     TemporaryPrice1 = TemporaryPrice1 + int(div_tag.get_text("$")[i]) * (10**(j-i))
                     i -= 1
            Prices.append(TemporaryPrice1)

#Size and Category
            TemporarySize = ItemDetails[k].find_all("li", attrs = "href", class_ = "size")

            for a_tag in TemporarySize:
                if a_tag.find('a') != None:
                    TemporarySize1 = a_tag.find('a').attrs['href']
                    TemporarySize1 = list(TemporarySize1[10:])

                    if '?' in TemporarySize1:
                        index = TemporarySize1.index('?')

                        Category = TemporarySize1[:index+1]
                        Category = ''.join(Category)

                        Size1 = TemporarySize1[index+6:]
                        Size1 = ''.join(Size1)

                        CategorySize = Category + Size1

                        Sizes.append(CategorySize)
                else:
                    Sizes.append('Missing')

#Brand
            for a_tag in TemporaryBrand:
                TemporaryBrand1 = a_tag.find('a').attrs['title']
                Brands.append(TemporaryBrand1)


        k += 1

    return [Titles, Prices, Sizes, Brands, Words]
