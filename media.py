import webbrowser


# definition of class Movie which has the following instance variables
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # NOQA
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# function used to show the trailer of the movies
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
