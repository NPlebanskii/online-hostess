from application import db, app_bcrypt, app


class Session(db.Model):
    """This class represents the sessions table."""

    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(255))
    user_type = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, uuid, user_type):
        """initialize with uuid."""
        self.uuid = uuid
        self.user_type = user_type

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Session.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Sessions: {}>".format(self.uuid)


class Establishment(db.Model):
    """This class represents the establishments table."""

    __tablename__ = 'establishments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    description = db.Column(db.Text())
    open_time = db.Column(db.Time())
    end_time = db.Column(db.Time())
    img_url = db.Column(db.String(255))

    def __init__(self, name, location, description, open_time, end_time,
                 img_url):
        self.name = name
        self.location = location
        self.description = description
        self.open_time = open_time
        self.end_time = end_time
        self.img_url = img_url

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Establishment.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Establishments: {}>".format(self.name)


class Table(db.Model):
    """This class represents the tables table."""

    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    establishment_id = db.Column(db.Integer,
                                 db.ForeignKey('establishments.id'))
    status = db.Column(db.String(255))
    user_id = db.Column(db.Integer)
    number = db.Column(db.Integer)
    establishment = db.relationship('Establishment', back_populates='tables')

    def __init__(self, establishment_id, status, user_id, number):
        self.establishment_id = establishment_id
        self.status = status
        self.user_id = user_id
        self.number = number

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Table.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Tables: {}>".format(self.number)


class User(db.Model):
    """This class represents the users table."""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255))
    rating = db.Column(db.Float(precision=1))
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, first_name, email, password, last_name=None,
                 admin=False):
        self.email = email
        self.password = app_bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.admin = admin
        self.first_name = first_name
        self.last_name = last_name
        self.rating = None

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Users: {}>".format(self.email)


Establishment.tables = db.relationship('Table', order_by=Table.id,
                                       back_populates='establishment')
