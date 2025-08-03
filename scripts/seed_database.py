from sqlalchemy import create_engine
from sqlalchemy import text
from core.schema_models import Base
from dotenv import load_dotenv
import os
import pandas as pd

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
        print("Database connection successful!")
except Exception as e:
    print(f"Failed to connect to the database: {e}")

def create_tables():
    try: 
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully!")
    except Exception as e:
        print(f"Failed to create tables: {e}")

def seeding_database():
    try:
        movies_df = pd.read_csv('/workspace/data/processed/movies.csv')
        movies_df.to_sql('movies',engine, if_exists='replace', index=False)
        print("Movies table seeded successfully!")

        ratings_df = pd.read_csv('/workspace/data/processed/ratings.csv')
        ratings_df.to_sql('ratings', engine, if_exists='replace', index=False)
        print("Ratings table seeded successfully!")
        
    except Exception as e:
        print(f"Failed to seed database: {e}")
        
if __name__ == "__main__":
    create_tables()
    seeding_database()
    