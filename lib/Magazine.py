from Article import Article

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def contributors(self):
        return list(set(article.author for article in self._articles))

    @classmethod
    def all(cls):
        return cls._all_magazines

    def add_article(self, author, title):
        new_article = Article(author, self, title)
        self._articles.append(new_article)
        return new_article

    @classmethod
    def find_by_name(cls, name):
        return next((magazine for magazine in cls._all_magazines if magazine.name == name), None)

    @classmethod
    def article_titles(cls):
        return [article.title for magazine in cls._all_magazines for article in magazine._articles]

    @classmethod
    def contributing_authors(cls):
        return [author for magazine in cls._all_magazines for author in magazine.contributors if len(author.articles) > 2]
