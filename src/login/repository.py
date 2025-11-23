from config.withCursor import with_cursor


class Repository:
    @staticmethod
    @with_cursor
    def find_user_by_login(cur, login):
        cur.execute("SELECT login, password FROM users u WHERE u.login = %s", (login, ))
        return cur.fetchone()