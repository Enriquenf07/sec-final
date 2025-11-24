from flask_login import current_user

menu_items = [
        {"name": "Home", "href": "home.home", "roles": None},
        {"name": "Usuários", "href": "home.home", "roles": ["admin", "suporte"]},
        {"name": "Configurações", "href": "home.home", "roles": None},
        {"name": "Logout", "href": "login.logout", "roles": None}
    ]

class Service:
    @staticmethod
    def generate_menu():
        from login import Service as Login_service
        if(not current_user):
            return None
        roles = Login_service.get_roles(current_user.id)
        menu = [menu for menu in menu_items if menu["roles"] == None or any(r in roles for r in menu["roles"])]
        return menu
    @staticmethod
    def get_default_ctx():
        ctx = {
            "menu": Service.generate_menu()
        }
        return ctx