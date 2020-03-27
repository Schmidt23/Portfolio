import os
from imdb import IMDb
import csv
import pandas as pd


filepath = f"imdbtop250\\top2.csv"
ia = IMDb()

def generate_link(search):

    movies = ia.search_movie(search)
    id = movies[0].movieID

    link = f"https://www.imdb.com/title/tt{id}"
    return link

def newest_movie():
    if not os.path.exists(filepath):

        movies = ia.get_top250_movies()
        header = ['rank', 'title', 'year']
        rows = []
        for movie in movies:
            rows.append([movie['top 250 rank'], movie['title'], movie['year']])

        with open(filepath, 'wt') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            for row in rows:
                csv_writer.writerow(row)

    with open(filepath, 'r') as f:
        df = pd.read_csv(f)

    select = ''.join(df.loc[df['year'] < 1990].sample()['title'].values)
    link = generate_link(select)
    return select, link