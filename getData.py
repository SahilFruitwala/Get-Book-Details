import requests # to request url and get data
from bs4 import BeautifulSoup # to parse through xml data


class GetData():
    """
    This class has given method...
    1. parseData() which returns title, author, published year, rating count,
        total text review count, image url
    """

    API_KEY = ''
    url = 'https://www.goodreads.com/search.xml?key=' + API_KEY + '&q='

    def __init__(self, bookName):
        """
        1. Get book name from user and assigned to variable.
        """
        self.bookName = bookName

    def parsed_data(self):
        """
        1. Request to the url using requests method
        2. Get Content from url using content method
        3. Parse XML data using BeautifulSoup
        4. return title, author, published year, rating count,
           total text review count, image url
        """
        try:
            self.reqs = requests.get(self.url+self.bookName)
            xmlData = self.reqs.content
            # 1. lxml-xml describes the type of parser to use
            # 2. we can use lxml also. which gives same results in this case
            parseData = BeautifulSoup(xmlData, features="lxml-xml")
            book = parseData.find('work') # get the first work data for given book
            title = book.find('best_book').find('title').text
            author = book.find('best_book').find('author').find('name').text
            rating = book.find('average_rating').text
            publishYear = book.find('original_publication_year').text
            ratingCount = book.find('ratings_count').text
            textReviewsCount = book.find('text_reviews_count').text
            imageURL = book.find('best_book').find('image_url').text
            # print(publishYear)
            # print(title)
            # print(author)
            # print(rating)
            # print(ratingCount)
            # print(textReviewsCount)
            # print(imageURL)
            return (title, author, publishYear, ratingCount, textReviewsCount, imageURL)
        except Exception:
            return "There is no data available!"


# name_book = 'think and grow rich'
# get = GetData(name_book)
# print(get.parsed_data())
