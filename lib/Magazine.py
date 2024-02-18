from .Article import Article
class Magazine:
    all_magazines = []
    mag_articles = []
    

    def __init__(self, name, category) :
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)
        
        
    @property
    #Magazine name()
    #Returns the name of this magazine
    def name(self):
        return self._name
    @property
    #Magazine category()
    #Returns the category of this magazine
    def category(self):
        return self._category

    # def __repr__(self) -> str:
    #     return (f"{self._name}" )
        
    @classmethod
    def all(cls):
        return Magazine.all_magazines
    
    def contributors(self):
        allArticles = Article.all_articles
        # get all articles for this magazine
        margArticles = [article for article in allArticles if article.magazine() == self]
        print(f"Checking margArticle details: {margArticles}")
        # find authors for these articles
        magAuthors = [article.author() for article in margArticles]
        return magAuthors

    @classmethod
    def find_by_name(cls, name):
        print(cls)
        for magazine in Magazine.all_magazines:
            if magazine.name == name:
                return magazine
            
    
    def magazine_articles(self):
        #get list of all articles and filters out those belonging to this magazine.
        my_articles = [article for article in Article.all_articles if article.magazine == self]
        print(my_articles)
        Magazine.mag_articles = my_articles
        return my_articles


    @classmethod
    def article_titles(cls):
        return [ article.title() for article in Magazine.mag_articles]
        # pass
        # return [article.title() for article in Article.all_articles if article.magazine() == cls.name]
        
        # for article in Article.all_articles:  [ Author One, Tutembee,  A Visit to Lamu,  Author One, Tupike,  Tupike Chakula Kitamu,  Author One, Tupike,  Tupike Chakula Kibaya]
        #     if article.magazine() == cls:
        #         return article.title
    

    def contributing_authors(self):
        #author_list with more than two articles for the magazine
        # print(f"mag_articles --> {Magazine.mag_articles}")
        author_dict = {}
        for author in self.contributors():
            if author in author_dict:
                author_dict[author] += 1

            else:
                author_dict[author] = 1

        for name, count in author_dict.items():
            if count >= 2:
                return (f"{name}:{count}")
            else:
                ""
