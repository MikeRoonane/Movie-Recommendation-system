from core.schema_models import Movie
from core.schema_models import Rating
from core.db_functions import get_session


with get_session() as session:
    result = session.query(Rating).filter(Rating.rating == 5.0).all()
    for res in result:
        movie = session.query(Movie).filter(Movie.movieId == res.movieId).first()
        if not movie:
            print("Error")