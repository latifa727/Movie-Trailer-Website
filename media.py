import webbrowser


class Movie(object):
    """docstring for Movie Class
          Arguments :
            title:a string indicate the title of the movie
            poster image:a string that take the url for the movie poster image
            trailer youtube:a string  take the url for movie youtube trailer
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """ inits class Movie """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


def show_trailer(self):
    """ show movie trailer url using open function in webbrowser module """
    webbrowser.open(self.trailer_youtube_url)
