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