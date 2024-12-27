class UserModel:
    def __init__(self, id, username, password, email, role):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.role = role

    def to_dict(self):
        return{
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'role': self.role,
        }
    def from_dict(data):
        return UserModel(
            id = data.get('id'),
            username = data.get('username'),
            password = data.get('password'),
            email = data.get('email'),
            role = data.get('role'),
        )
    
    def getName(self):
        return self.username
    def getPassword(self):
        return self.password

    def getEmail(self):
        return self.email

    def getRole(self):
        return self.role

    def getId(self):
        return self.id

    def setName(self, name):
        self.username = name

    def setPassword(self, password):
        self.password = password

    def setEmail(self, email):
        self.email = email

    def setRole(self, role):
        self.role = role

    def setId(self, id):
        self.id = id