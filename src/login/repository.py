from config.withCursor import with_cursor


class Repository:
    @staticmethod
    @with_cursor
    def find_user_by_login(cur, login):
        cur.execute("SELECT u.id, login, password, c.ativo as c_ativo FROM users u LEFT JOIN company c ON c.id = u.company WHERE u.login = %s", (login, ))
        return cur.fetchone()
    
    @staticmethod
    @with_cursor
    def find_user_by_id(cur, id):
        cur.execute("SELECT u.id, login, password, c.ativo as c_ativo FROM users u LEFT JOIN company c ON c.id = u.company WHERE u.id = %s", (id, ))
        return cur.fetchone()
    @staticmethod
    @with_cursor
    def get_roles_by_id(cur, id):
        cur.execute("SELECT role FROM user_role r LEFT JOIN users u ON u.id = r.user WHERE u.id = %s", (id, ))
        return [row[0] for row in cur.fetchall()]
     
    @staticmethod
    @with_cursor
    def create_user(cur, form, company):
        cur.execute(
            "INSERT INTO users (login, password, email, name, company) VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (form['login'], form['password'], form['email'], form['name'], company),
        )
        row = cur.fetchone()
        return row[0] if row else None
    
    @staticmethod
    @with_cursor
    def set_role(cur, id, role):
        cur.execute(
            'INSERT INTO user_role ("user", role) VALUES (%s, %s) RETURNING id',
            (id, role),
        )
        row = cur.fetchone()
        return row[0] if row else None
    
    @staticmethod
    @with_cursor
    def create_company(cur, name, token):
        cur.execute(
            "INSERT INTO company (name, ativo, token_inicial) VALUES (%s, %s, %s) RETURNING id",
            (name, False, token),
        )
        row = cur.fetchone()
        return row[0] if row else None

    @staticmethod
    @with_cursor
    def find_company_by_token(cur, token):
        cur.execute("SELECT id FROM company c WHERE c.token_inicial = %s", (token, ))
        row = cur.fetchone()
        return row[0] if row else None
    
    
    @staticmethod
    @with_cursor
    def active_company(cur, id):
        cur.execute(
            """
            UPDATE company
            SET ativo = %s,
                token_inicial = NULL
            WHERE id = %s
            """,
            (True, id)
        )


    
            