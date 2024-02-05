#!/usr/bin/env python3
import sys
sys.path.append('lib')  # Assuming 'lib' is one level above 'tools'

import ipdb

from Author import Author
from Magazine import Magazine
from Article import Article

if __name__ == '__main__':
    #  WRITE YOUR TEST CODE HERE ###
    author1 = Author("John Thabuks")
    author2 = Author("Alex Mutinda")

    magazine1 = Magazine("Hope FM", "The word")
    magazine2 = Magazine("Radio Jambo", "Patanisho")

    article1 = author1.add_article(magazine1, "Space x")
    article2 = author2.add_article(magazine1, "What journey would you take to the future")
    article3 = author1.add_article(magazine2, "Stock market")

    # Test code
    print("Authors:")
    for author in Author.all():
        print(author.name)

    print("\nMagazines:")
    for magazine in Magazine.all():
        print(f"{magazine.name} - {magazine.category}")

    print("\nArticles:")
    for article in Article.all():
        print(f"{article.title} by {article.author.name} in {article.magazine.name}")

    # DO NOT REMOVE THIS
    ipdb.set_trace()
