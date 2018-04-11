from app import db


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
