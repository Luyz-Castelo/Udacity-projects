import fresh_tomatoes
import movie

toy_story = movie.Movie(
  movie_title='Toy Story', 
  movie_storyline='A story of a boy and his toys that come to life', 
  poster_image='https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg', 
  trailer_youtube='https://www.youtube.com/watch?v=rNk1Wi8SvNc'
  )

print(toy_story.storyline)

avatar = movie.Movie(
  movie_title='Avatar', 
  movie_storyline='A marine on an alien planet', 
  poster_image='https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amateur-made_Na%27vi.jpg/640px-Amateur-made_Na%27vi.jpg', 
  trailer_youtube='https://www.youtube.com/watch?v=5PSNL1qE6VY'
  )

# avatar.show_trailer()
school_of_rock = movie.Movie(
  movie_title='School of Rock', 
  movie_storyline='Using rock music to learn', 
  poster_image='https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg', 
  trailer_youtube='https://www.youtube.com/watch?v=TExoc0MG4I4'
  )

ratatouille = movie.Movie(
  movie_title='Ratatouille', 
  movie_storyline='A rat chef in Paris', 
  poster_image='https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg', 
  trailer_youtube='https://www.youtube.com/watch?v=-tNqfcZKn6k'
  )

midnight_in_paris = movie.Movie(
  movie_title='Midnight in Paris', 
  movie_storyline='Going back in time to meet the authors', 
  poster_image='https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg', 
  trailer_youtube='https://www.youtube.com/watch?v=FAfR8omt-CY'
  )

hunger_games = movie.Movie(
  movie_title='Hunger Games', 
  movie_storyline='A really real reality show', 
  poster_image='https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg', 
  trailer_youtube='https://www.youtube.com/watch?v=mfmrPu43DF8'
  )

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies=movies)
