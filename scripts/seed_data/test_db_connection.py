from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

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
