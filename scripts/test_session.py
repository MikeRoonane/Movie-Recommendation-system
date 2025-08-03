from core.schema_models import Movie
from core.schema_models import Rating
from core.db_functions import get_session


with get_session() as session:
    res = session.query(Rating).filter(Rating.rating == 5.0).first()
    result = session.query(Movie).filter(Movie.movieId == res.movieId).first()
    print(result.title)