from app import db

class Session(db.Model):
    """This class represents the session table."""

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