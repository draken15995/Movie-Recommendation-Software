import csv

with open('Top100Movies.csv', newline='') as movies_csv:
    movie_reader = csv.DictReader(movies_csv)
    movie_list = []
    for row in movie_reader:
        movie_list.append(row)
