
import webbrowser
class Movie():
    """This class creates a movie object with the initialized variables.
    The initialized variables are title of the movie, 
    storyline of the movie, URL of the poster image, and URL of its YouTube trailer.
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
           trailer_youtube_url):
        self.title = movie_title  #Assigning movie title
        self.storyline = movie_storyline  # Assigning movie storyline
        self.poster_image_url = poster_image  # Assigning poster image URL
        self.trailer_youtube_url = trailer_youtube_url # Assigning trailer video URL
