from psycopg_pool import ConnectionPool

pool = ConnectionPool(
    conninfo="postgresql://admin:admin@localhost:5432/appdb",
    min_size=3,
    max_size=15,
    timeout=10,
    open=True,
)