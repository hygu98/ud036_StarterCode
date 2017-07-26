# coding=utf-8

"""
Module to display movie object, attributes and instances
"""

import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        """
        Initialize instance of class Movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Initialize instance for playing the youtube.com/
        movie trailer on the website
        """
        webbrowser.open(self.trailer_youtube_url)
