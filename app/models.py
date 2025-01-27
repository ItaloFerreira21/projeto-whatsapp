from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(320), nullable=False)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)  # Adicionando o campo CNPJ
    company_name = db.Column(db.String(255))  # Nome da empresa
    phone_number = db.Column(db.String(20))  # Número de telefone
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<User {self.username}>'

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    action = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    user = db.relationship('User', backref=db.backref('records', lazy=True))

    def __repr__(self):
        return f'<Record {self.action} by User {self.user_id}>'

class Freelancer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Relacionamento com o contratante
    nome_completo = db.Column(db.String(255), nullable=False)
    celular = db.Column(db.String(15), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)  # M, F, O (Masculino, Feminino, Outro)
    email = db.Column(db.String(255), nullable=False)
    rg = db.Column(db.String(20), nullable=False)
    chave_pix = db.Column(db.String(77), nullable=False)  # Agora a chave PIX é obrigatória e aceita até 77 caracteres

    user = db.relationship('User', backref=db.backref('freelancers', lazy=True))

    def __repr__(self):
        return f'<Freelancer {self.nome_completo}>'