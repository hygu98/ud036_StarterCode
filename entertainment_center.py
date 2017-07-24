import media
import fresh_tomatoes

#this file contains the list of movies to be dynamically generated by fresh_tomatoes.py when run
#to add more movies follow the below formatting and be sure to add the instance to the movies list

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", 
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

office_space = media.Movie("Office Space",
                           "Three company workers who hate their jobs decide to rebel against their greedy boss.",
                           "https://images-na.ssl-images-amazon.com/images/I/51S7MWB56VL.jpg",
                           "https://www.youtube.com/watch?v=dMIrlP61Z9s")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", 
                             "http://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "http://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "http://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "http://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, office_space, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)
