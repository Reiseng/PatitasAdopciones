from persistence.userDao import UserPersistence

class UserService:
    def __init__(self, user_repository=None):
        # Usa el repositorio proporcionado o crea uno nuevo por defecto
        self.user_repository = user_repository or UserPersistence()

    def create_user(self, name, email, password, rank):
        # Lógica de negocio para crear un usuario, como validaciones
        if not name or not email or not password:
            raise ValueError("Name, email, and password are required.")
        user = self.user_repository.add_user(name, email, password, rank)
        return user

    def get_user(self, user_id):
        user = self.user_repository.get_user(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        return user

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def update_user(self, user_id, name=None, email=None, password=None, rank=None):
        print(user_id)
        user = self.user_repository.update_user(user_id, name, email, password, rank)
        print(user)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        return user

    def delete_user(self, user_id):
        user = self.user_repository.delete_user(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        return user
