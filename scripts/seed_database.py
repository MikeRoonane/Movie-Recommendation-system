from sqlalchemy import create_engine
from sqlalchemy import text
from core.schema_models import Base
from dotenv import load_dotenv
import os
import pandas as pd
from core.schema_models import Movie, Rating
from core.db_functions import get_session
load_dotenv()

db_user = os.getenv('DB_USER') 
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

database_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


try:
    engine = create_engine(database_url)
    with engine.connect() as connection:
        connection.execute(text("TRUNCATE TABLE ratings RESTART IDENTITY CASCADE"))
        connection.execute(text("TRUNCATE TABLE movies RESTART IDENTITY CASCADE"))
        print("Database connection successful!")
except Exception as e:
    print(f"Failed to connect to the database: {e}")

def create_tables():
    try: 
        Base.metadata.drop_all(bind=engine)
        print("Dropped all tables")
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully!")
    except Exception as e:
        print(f"Failed to create tables: {e}")

def seeding_database():
    try:
        movies_df = pd.read_csv('/workspace/data/processed/movies.csv')
        ratings_df = pd.read_csv('/workspace/data/processed/ratings.csv')
        movies_df = movies_df.astype({'movieId':'int','title':'str','genres':'str','Year':'int'})
        ratings_df = ratings_df.astype({'userId':'int','movieId':'int','rating':'float','timestamp':'int'})
        movies = [Movie(**row.to_dict()) for _,row in movies_df.iterrows()]
        with get_session() as session:
            session.add_all(movies)
            session.commit()
            existing_movie_id = set( id for (id,) in session.query(Movie.movieId).all())
            valid_ratings = []
            for _,row in ratings_df.iterrows():
                if row['movieId'] in existing_movie_id:
                    valid_ratings.append(
                        Rating(**row.to_dict())
                    )
            session.add_all(valid_ratings)
            session.commit()                
    except Exception as e:
        print(f"Failed to seed database: {e}")
        
if __name__ == "__main__":
    create_tables()
    seeding_database()
    