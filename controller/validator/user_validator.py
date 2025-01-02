import re
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
class UserValidator:

    @staticmethod
    def validate_create_user_data(name, email, password, rank):
        # Validar que todos los campos sean proporcionados
        if not name or not email or not password or not rank:
            raise ValueError("Name, email, password, and rank are required.")

        # Validar que el email tenga un formato válido
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")

        # Validar la longitud de la contraseña (mínimo 8 caracteres, por ejemplo)
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if password and not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit.")
        if password and not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if password and not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter.")
        if password and not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?`~" for char in password):
            raise ValueError("Password must contain at least one special character.")

    @staticmethod
    def validate_update_user_data(name, email, password, rank):
        # Validar que al menos un campo esté presente para la actualización
        if not name and not email and not password and not rank:
            raise ValueError("At least one field (name, email, password, or rank) must be provided to update the user.")

        # Validar el formato del email si se proporciona uno nuevo
        if email:
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_regex, email):
                raise ValueError("Invalid email format.")

        # Validar la longitud de la contraseña si se proporciona una nueva
        if password:
            if len(password) < 8:
                raise ValueError("Password must be at least 8 characters long.")
            if not any(char.isdigit() for char in password):
                raise ValueError("Password must contain at least one digit.")
            if not any(char.isupper() for char in password):
                raise ValueError("Password must contain at least one uppercase letter.")
            if not any(char.islower() for char in password):
                raise ValueError("Password must contain at least one lowercase letter.")
            if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?`~" for char in password):
                raise ValueError("Password must contain at least one special character.")

        # Validar el rango si se proporciona uno nuevo
        if rank:
            valid_ranks = ["Usuario", "Administrador", "Moderator"]
            if rank not in valid_ranks:
                raise ValueError(f"Invalid rank. Allowed values are: {', '.join(valid_ranks)}.")