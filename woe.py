# Recommendation Software

# data needed: 
# Movies: top 100 movies according to IMDB
#     Title
#     Synopsis
#     Runtime
#     Rating (probably just IMDB rating, but could also do RT/MC if I want to add more)
#     MPA rating (G, PG, etc.)
#     Genre1/Genre2
#     Cast (top 3)

# Functions of program:
#   receive recommendations for movies based on the following criteria:
#       Keywords in title/synopsis
#       Runtime
#       MPA rating
#       Critic rating
#       Genre
#       Cast
#    question posed to user: 
#        How would you like to search? Options are 1. Keyword, 2. Runtime, 3. MPA Rating, 4. IMDB Rating, 5. Genre, 6. Cast
#        Maybe eventually add in a function to search for NOT IN, like horror movies NOT starring a certain actor, or mabye only movies with a rating of 9.0 or better, things like that
#    
#    how recommendations are received:
#        Format recommendations to be printed in a specific format (draft):
#            Recommendation 
#               Title
#                   Genre
#                   Cast
#                   Synopsis
#                   Runtime
#                   MPA Rating
#                   Critic Rating

from logo import *
from moviedata import *
from linkedlist import LinkedList

print_logo()

genre_list = []

def insert_movie_genres():
    movie_genre_list = LinkedList()
    if movie_genre_list.get_head_node().value == None:
        movie_genre_list.remove_node(None)
    for movie in movie_list:
        if movie["Genre"].lower() not in genre_list:
            genre_list.append(movie["Genre"].lower())
    for genre in genre_list:
        movie_genre_list.insert_beginning(genre)
    return movie_genre_list

my_genre_list = insert_movie_genres()
# print(genre_list)
# print(my_genre_list.stringify_list())
# print(movie_list[0]["Genre1"])

def insert_movie_data():
    movie_data_list = LinkedList()
    for genre in genre_list:
        genre_sublist = LinkedList()
        for movie in movie_list:
            # print(movie["Title"])
            if movie["Genre"].lower() == genre:
                # print(genre)
                # print(movie)
                # print(True)
                # print(movie["Genre1"], movie["Genre2"])
                genre_sublist.insert_beginning(movie)
                # print(genre_sublist.get_head_node().value)
                # print(genre_sublist.stringify_list())
        movie_data_list.insert_beginning(genre_sublist)
        # print(movie_data_list.get_head_node().value.stringify_list())
    return movie_data_list

# def insert_movie_data_TEST():
#     genre = genre_list[0]
#     movie_data_list = LinkedList()
#     genre_sublist = LinkedList()
#     for movie in movie_list:
#         if movie["Genre1"] == genre or movie["Genre2"] == genre:
#             genre_sublist.insert_beginning(movie)
#     movie_data_list.insert_beginning(genre_sublist)
#     print(movie_data_list.get_head_node().value)



my_movie_list = insert_movie_data()

# print(my_genre_list.stringify_list())
# current_node = my_movie_list.get_head_node()
# while current_node is not None:
#     print(current_node.head_node.value)
#     current_node = current_node.get_next_node()

selected_genre = ""

while len(selected_genre) == 0:
    user_input = str(input("\nWhat movie genre are you interested in watching?\nType the beginning of the genre and press enter to see if it is on the list.\nPress enter to see the list of all available genres.\n")).lower()

    matching_genres = []
    genre_list_head = my_genre_list.get_head_node()
    # print(str(genre_list_head.get_value()))
    # print(genre_list_head.get_value())
    while genre_list_head is not None:
        # print(user_input)
        if str(genre_list_head.get_value()).startswith(user_input) and str(genre_list_head.get_value()) not in matching_genres:
            matching_genres.append(genre_list_head.get_value())
            # print(matching_genres)
        genre_list_head = genre_list_head.get_next_node()
        # print(genre_list_head.get_value())

    for genre in matching_genres:
        print(genre)
    
    if len(matching_genres) == 1:
        select_genre = str(input("\nThe only genre that matches your search is " + matching_genres[0] + ". \nIs this the genre of movie you are looking for? Enter y for yes, or n for no\n")).lower()

        if select_genre == "y":
            selected_genre = matching_genres[0]
            print("You have chosen: " + selected_genre)
            movie_list_head = my_movie_list.get_head_node()
            # print(my_movie_list.get_head_node().get_value().get_head_node().value["Title"])
            while movie_list_head.get_next_node() is not None:
                sublist_head = movie_list_head.get_value().get_head_node()
                if sublist_head.get_value()["Genre"].lower() == selected_genre:
                    while sublist_head.get_next_node() is not None:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Title: " + sublist_head.get_value()["Title"])
                        print("Genre: " + sublist_head.get_value()["Genre"])
                        print("Main Cast: " + sublist_head.get_value()["Cast1"] + ", " + sublist_head.get_value()["Cast2"] + ", and " + sublist_head.get_value()["Cast3"])
                        print("Synopsis: " + sublist_head.get_value()["Synopsis"])
                        print("Runtime: " + sublist_head.get_value()["Runtime"])
                        print("MPA Rating " + sublist_head.get_value()["MPA_Rating"])
                        print("Critic Rating: " + sublist_head.get_value()["Critic_Rating"])
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        sublist_head = sublist_head.get_next_node()
                movie_list_head = movie_list_head.get_next_node()

            repeat_loop = str(input("\nDid you find a movie you are interested in? Enter y for yes, or n for no.\n")).lower()
            if repeat_loop == "n": 
                selected_genre = ""
            else:
                print("Enjoy your movie!")


#TEST STUFF#