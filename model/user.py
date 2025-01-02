class User:
    def __init__(self, id, name, email, password, rank):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.rank = rank

    def __str__(self):
        return f"UserDTO(id={self.id}, name={self.name}, email={self.email}, rank={self.rank},'password': {self.password})"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'rank': self.rank,
            'password': self.password
        }
