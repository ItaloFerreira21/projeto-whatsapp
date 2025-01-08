from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.name}>'

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    participants = db.relationship('User', secondary='group_user', backref='groups')
    
    def __repr__(self):
        return f'<Group {self.name}>'

# Tabela de relacionamento entre usuários e grupos
class GroupUser(db.Model):
    __tablename__ = 'group_user'
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
