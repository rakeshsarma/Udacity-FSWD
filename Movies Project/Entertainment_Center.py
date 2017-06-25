#import statements
import media  #Class to create movie objects. Holds movie instance variables and instance methods 
import fresh_tomatoes  #Provides a functioning code to display movies 

#Movie 1
#DJ
dj_title = 'Duvvada Jagannatham'
dj_story_line = 'DJ is a traditionally raised Brahmin guy '
'from Vijayawada in India who runs a catering business',
dj_poster = 'http://www.yadtek.com/wp-content/uploads/2017/04/Allu-Arjun-DJ-Movie-Poster-5.jpg'
dj_trailer = 'https://www.youtube.com/watch?v=fy-kooz9se4'

#DJ object creation
dj = media.Movie(dj_title,
                 dj_story_line,
                 dj_poster,
                 dj_trailer)
                 
#Movie 2
#SpiderMan Homecoming
spiderman_homecoming_title = 'Spiderman Homecoming'
spiderman_homecoming_storyline = 'A Spiderman Reboot'
spiderman_homecoming_poster = 'https://cdn.vox-cdn.com/uploads/chorus_asset/file/8571017/spider_man_poster.jpg'
spiderman_homecoming_trailer = 'https://www.youtube.com/watch?v=n9DwoQ7HWvI'

#Spiderman_homecoming object creation
spiderman_homecoming = media.Movie(spiderman_homecoming_title,
                                   spiderman_homecoming_storyline,
                                   spiderman_homecoming_poster,
                                   spiderman_homecoming_trailer)

#Movie 3
#Cars 3
cars3_title = 'Cars 3'
cars3_storyline = 'Third installment of Cars movie'
cars3_poster = 'http://cdn3-www.comingsoon.net/assets/uploads/2016/11/cars3internationalheader.jpg'
cars3_trailer = 'https://www.youtube.com/watch?v=2LeOH9AGJQM'

#Cars 3 object creation
cars3 = media.Movie(cars3_title,cars3_storyline, cars3_poster, cars3_trailer )

#Movie 4 Tiger
Tiger_title = 'Tiger'
Tiger_storyline = 'A Kannada movie'
Tiger_poster = 'http://telugnet.na1381756400.netdna-cdn.com/wp-content/uploads/2015/06/tiger-movie-Review.jpg'
Tiger_trailer = 'https://www.youtube.com/watch?v=7vkWcZ5Hepo'

#Tiger object creation
tiger = media.Movie(Tiger_title,
	                Tiger_storyline,
	                Tiger_poster,
	                Tiger_trailer
)

#Movie 5 Frozen
frozen_title = 'Frozen'
frozen_storyline = 'Story of an Ice Princess'
frozen_poster = 'https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg'
frozen_trailer = 'https://www.youtube.com/watch?v=hb8WDATVB6A'

# Fozen Object creation
frozen = media.Movie(frozen_title,
                     frozen_storyline,
                     frozen_poster,
                     frozen_trailer)

#Movie 6 Lion King
lion_king_title = 'The Lion King'
lion_king_storyline = 'Story of lions in the Jungle'
lion_king_poster = 'http://vignette3.wikia.nocookie.net/disney/images/c/cb/The_Lion_King_Textless_poster_1.jpg/revision/latest?cb=20140810104158'
lion_king_trailer = 'hhttps://www.youtube.com/watch?v=4sj1MT05lAA'

# lion_king Object creation
lion_king = media.Movie(lion_king_title,
                       lion_king_storyline,
                       lion_king_poster,
                       lion_king_trailer)

#Adding movies to a list
movies = [dj,spiderman_homecoming, cars3, tiger,frozen, lion_king]

#calling function to create movies page
fresh_tomatoes.open_movies_page(movies)


