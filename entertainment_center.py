import fresh_tomatoes
import media

""" Create instances of class Movie with the arguments:
movie_title, poster_image_url, trailer_youtube_url """
minions = media.Movie("Minions", "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg", "https://www.youtube.com/watch?v=dVDk7PXNXB8")  # noqa

ice_age = media.Movie("Ice Age", "https://upload.wikimedia.org/wikipedia/en/3/3c/Ice_Age_%282002_film%29_poster.jpg", "https://www.youtube.com/watch?v=N9pq-87oCxA")  # noqa

frozen = media.Movie("Frozen", "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg", "https://www.youtube.com/watch?v=TbQm5doF_Uc")  # noqa

home_alone = media.Movie("Home Alone", "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg", "https://www.youtube.com/watch?v=jEDaVHmw7r4")  # noqa

jumanji = media.Movie("Jumanji : Welcome to the jungle", "https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png", "https://www.youtube.com/watch?v=v_TJKwJwN0E")  # noqa

wonder = media.Movie("Wonder", "https://upload.wikimedia.org/wikipedia/en/6/67/Wonder_%28film%29.png", "https://www.youtube.com/watch?v=ngiK1gQKgK8")   # noqa

""" store the movies in array """
movies_list = [minions, ice_age, frozen, home_alone, jumanji, wonder]

""" call open_movies_page function in fresh_tomatoes that takes an array """
fresh_tomatoes.open_movies_page(movies_list)
