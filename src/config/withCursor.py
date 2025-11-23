from .db import pool

def with_cursor(func):
    def wrapper(*args, **kwargs):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                return func(cur, *args, **kwargs)
    return wrapper