from config.withCursor import with_cursor


class Repository:
    @staticmethod
    @with_cursor
    def find_user_by_login(cur, login):
        cur.execute("SELECT id, login, password FROM users u WHERE u.login = %s", (login, ))
        return cur.fetchone()
    
    @staticmethod
    @with_cursor
    def find_user_by_id(cur, id):
        cur.execute("SELECT id, login, password FROM users u WHERE u.id = %s", (id, ))
        return cur.fetchone()
    @staticmethod
    @with_cursor
    def get_roles_by_id(cur, id):
        cur.execute("SELECT role FROM user_role r LEFT JOIN users u ON u.id = r.user WHERE u.id = %s", (id, ))
        return [row[0] for row in cur.fetchall()] 