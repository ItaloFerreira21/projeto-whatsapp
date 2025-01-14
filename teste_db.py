from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()

    new_user = User (name= 'italo', phone_number='1234567890')
    db.session.add(new_user)
    db.session.commit()

    user = User.query.first()
    print(user.name)

                    

    