import media
import fresh_tomatoes

# object of class Movie
american_sniper = media.Movie("American Sniper",
                              "A story of american soldier",
                              "http://is2.mzstatic.com/image/thumb/Video60/v4/7d/ca/88/7dca8825-8dbf-9653-afdb-fe3753f7d91e/source/1200x630bb.jpg",
                              "https://www.youtube.com/watch?v=99k3u9ay1gs")

#print(american_sniper.storyline)

# object of class Movie
interstellar = media.Movie("Interstellar",
                           "A story of astronaut in Mars",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

#interstellar.show_trailer()

# object of class Movie
dunkirk = media.Movie("Dunkirk",
                      "A story of soldiers",
                      "http://www.geekgirlauthority.com/wp-content/uploads/2016/12/d3a8343cb1c0bbe8-600x400.jpg",
                      "https://www.youtube.com/watch?v=T7O7BtBnsG4")

# object of class Movie
martian = media.Movie("Martian",
                      "A story of an astronaut who is abandoned from the rest of his crew on Mars",
                      "http://www.xfdrmag.net/wp-content/uploads/2015/10/the-martian-poster.jpg",
                      "https://www.youtube.com/watch?v=XQnYm5MG1x0")

# object of class Movie
lion = media.Movie("Lion",
                   "A story of an Indian kid who is lost and adopted by an Australian couple",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcTVuFTo4qf9v0c91rhTcSn25dsQygPhIRdivLe8Z1HdZNiPCj2F",
                   "https://www.youtube.com/watch?v=CoIy9Xq8tYs")

# object of class Movie
batman = media.Movie("Batman",
                     "A story of a guy who saves the city of Gothan from evil minds",
                     "http://www.followingthenerd.com/site/wp-content/uploads/TheDarkKnightRises_TeaserPoster.jpg",
                     "https://www.youtube.com/watch?v=ay-Xg1oTeAs")


# array that stores the movies to be displayed on the website
movies = [american_sniper, interstellar, dunkirk, martian, lion, batman]
fresh_tomatoes.open_movies_page(movies)
