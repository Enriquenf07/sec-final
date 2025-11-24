from psycopg_pool import ConnectionPool
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv("DATABASE_URL")

pool = ConnectionPool(
    conninfo=database_url,
    min_size=3,
    max_size=15,
    timeout=10,
    open=True,
)