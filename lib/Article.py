class Article:
    all_articles = []
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)
        pass

    # def __repr__(self) -> str:
    #     return(f"{self._author}, {self._magazine},  {self._title}" )
        pass
    def title(self):
        return self._title

    def all(self):
        return Article.all_articles
    
    def author(self):
        return self._author
    
    def magazine(self):
        return self._magazine
    