# IMDB Top 250 Movies data

import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.strong.text for b in soup.select("td.ratingColumn.imdbRating ")]

imdb = []
years_of_release = []
rating_of_movies = []
rt = []

for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    ranking = movie[:len(str(index)) - (len(movie))]
    ratings_pi = ratings[index]

    data = {"Rankings": ranking,
            "Movie_title": movie_title,
            "Year": year,
            "Star_cast": crew[index],
            "Rating": ratings[index]
            }

    imdb.append(data)
    years_of_release.append(year)
    rating_of_movies.append(ratings_pi)
    rt.append(ranking)

df = pd.DataFrame(imdb)
df.to_csv("Top 250 Movies.csv", index=False)

# To print data
print(df)
