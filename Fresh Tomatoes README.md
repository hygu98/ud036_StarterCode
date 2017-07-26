# ud036_StarterCode
Source code for a Movie Trailer website.

## How to use this code
entertainment_center.py is the file that runs this application.  To run the application, copy the below files to the python directory and runt the entertainment_center.py module in IDLE.

* -fresh_tomatoes.py
* -entertainment_center.py
* -media.py

### -entertainment_center.py
This code imports the class **media** and **fresh_tomatoes** additionally, this is where all of the data is stored that we will use to later dynamically generate our movies trailer website.  To add additional movies to the trailer website continue to add movies in the below format:

```
hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",                          "http://www.youtube.com/watch?v=PbA63a7H0bo")
```

### -media.py
-media.py is our class which allows us to call instances of _Movie_ to re-use code in creating additional mvies later.  We pass in to _Movie_ the movie title, movie storyline, poster image, and the youtube trailer.  Additioanlly we define the method _show_trailer_ in -media.py.




