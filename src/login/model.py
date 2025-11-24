from flask_login import UserMixin

class UserWrapper(UserMixin):
    def __init__(self, user_row):
        self.user = user_row
        self.id = user_row[0]            
        self.login = user_row[1]
    def get_id(self):
        return str(self.id)
