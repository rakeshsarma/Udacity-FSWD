import media
import fresh_tomatoes
#Movie 1 : DJ Movie
dj = media.Movie('Duvvada Jagannatham',
                 'DJ is a traditionally raised Brahmin guy from Vijayawada who runs a catering business',
                 'http://www.yadtek.com/wp-content/uploads/2017/04/Allu-Arjun-DJ-Movie-Poster-5.jpg',                
                 'https://www.youtube.com/watch?v=fy-kooz9se4')
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
cars3_storyline = 'Third installment of Cars Movie'
cars3_poster = 'http://cdn3-www.comingsoon.net/assets/uploads/2016/11/cars3internationalheader.jpg'
cars3_trailer = 'https://www.youtube.com/watch?v=2LeOH9AGJQM'

#Cars 3 object creation
cars3 = media.Movie(cars3_title,cars3_storyline, cars3_poster, cars3_trailer )

#Movie 4 Tiger
Tiger_title = 'Tiger'
Tiger_storyline = 'A Kannada Movie'
Tiger_poster = 'http://telugnet.na1381756400.netdna-cdn.com/wp-content/uploads/2015/06/tiger-movie-Review.jpg'
Tiger_trailer = 'https://www.youtube.com/watch?v=7vkWcZ5Hepo'

#Tiger object creation
tiger = media.Movie(Tiger_title,
Tiger_storyline,
Tiger_poster,
Tiger_trailer,
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
LionKing_title = 'The Lion King'
LionKing_storyline = 'Story of lions in the Jungle'
LionKing_poster = 'http://vignette3.wikia.nocookie.net/disney/images/c/cb/The_Lion_King_Textless_poster_1.jpg/revision/latest?cb=20140810104158'
LionKing_trailer = 'hhttps://www.youtube.com/watch?v=4sj1MT05lAA'

# LionKing Object creation
LionKing = media.Movie(LionKing_title,
LionKing_storyline,
LionKing_poster,
LionKing_trailer)

movies = [dj,spiderman_homecoming, cars3, tiger,frozen, LionKing]
fresh_tomatoes.open_movies_page(movies)


