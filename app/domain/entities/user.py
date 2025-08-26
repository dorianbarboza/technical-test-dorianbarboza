class User:
    def __init__(self, email: str, hashed_password: str, is_admin: bool = False):
        self.email = email
        self.hashed_password = hashed_password 
        self.is_admin = is_admin

    def promote_to_admin(self):
        """Convierte a un usuario en administrador"""
        self.is_admin = True

    def demote_to_user(self):
        """Revoca privilegios de administrador"""
        self.is_admin = False