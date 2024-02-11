from .Article import Article
class Author:
    def __init__(self, name) :
        self._name = name
        
    def __repr__(self) -> str:
        return(f" {self._name}" )
        pass
    def name(self):
        return self._name
    
    def articles(self):
        # return a list of all articles, written by this author
        # get a list of all articles, and filter by author
        allArticles = Article.all_articles  # [ Author One, Tutembee,  A Visit to Lamu,  Author One, Tupike,  Tupike Chakula Kitamu,  Author One, Tupike,  Tupike Chakula Kibaya]
        # print(f"Article.all_articles {allArticles}")
        authorArticles = []
        for article in allArticles:
            if article.author() == self:
                authorArticles.append(article)
        # print(f" authorArticles --> {authorArticles}")
        return [article for article in allArticles if article.author() == self]


    def magazines(self):
        # get a list of all magazines where the author has articles
        # access all articles by this author
        authorArticles = self.articles() # Articles for our Author [ Author One, Tutembee,  A Visit to Lamu,  Author One, Tupike,  Tupike Chakula Kitamu,  Author One, Tupike,  Tupike Chakula Kibaya]
        # find out which magazines the articles belong to
        authorMagazines = []
        for article in authorArticles:  # [ Author One, Tutembee,  A Visit to Lamu,  Author One, Tupike,  Tupike Chakula Kitamu,  Author One, Tupike,  Tupike Chakula Kibaya]
            authorMagazines.append(article.magazine()) if article.magazine() not in authorMagazines else ""
        return authorMagazines  #[Tutembee, Tupike]
    
    def add_article(self,magazine, title):
        #create new article instnace for this author
        new_article = Article(self, magazine, title)

    def topic_areas(self):
        #returns a unique list containing strings
        #this string list has categories of the magazine the author has contributed
        unique_mag_string = self.magazines()

        unique_mag_list = []
        for mag in unique_mag_string:
            unique_mag_list.append(mag.category)

        return unique_mag_list

        



