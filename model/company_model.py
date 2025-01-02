class CompanyModel:
    def __init__(self, id, nombre, mail, telefono, facebook, instagram, twitter):
        self.id = id
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono
        self.facebook = facebook
        self.instagram = instagram
        self.twitter = twitter
    
    def to_dict(self):
        return{
            'id': self.id,
            'nombre': self.nombre,
            'mail': self.mail,
            'telefono': self.telefono,
            'facebook': self.facebook,
            'instagram': self.instagram,
            'twitter': self.twitter,
        }
    def from_dict(data):
        return CompanyModel(
            id = data.get('id'),
            nombre = data.get('nombre'),
            mail = data.get('mail'),
            telefono = data.get('telefono'),
            facebook = data.get('facebook'),
            instagram = data.get('instagram'),
            twitter = data.get('twitter'),
        )
    def getNombre(self):
        return self.nombre
    def getMail(self):
        return self.mail
    def getTelefono(self):
        return self.telefono
    def getFacebook(self):
        return self.facebook
    def getInstagram(self):
        return self.instagram
    def getTwitter(self):
        return self.twitter
    def getId(self):
        return self.id
    def setNombre(self, nombre):
        self.nombre = nombre
    def setMail(self, mail):
        self.mail = mail
    def setTelefonoo(self, telefono):
        self.telefono = telefono
    def setFacebook(self, facebook):
        self.facebook = facebook
    def setInstagram(self, instagram):
        self.instagram = instagram
    def setTwittter(self, twitter):
        self.twitter = twitter