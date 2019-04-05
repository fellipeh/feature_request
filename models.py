from app import db


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class FeatureRequest(db.Model):
    __tablename__ = 'feature_request'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    client = db.Column(db.String())
    client_priority = db.Column(db.Integer())
    target_date = db.Column(db.Date())
    product_area = db.Column(db.String())

    def __init__(self, title, description, client, client_priority, targe_date, product_area):
        self.title = title
        self.description = description
        self.client = client
        self.client_priority = client_priority
        self.targe_date = targe_date
        self.product_area = product_area

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'client': self.client,
            'client_priority': self.client_priority,
            'target_date': dump_datetime(self.target_date),
            'product_area': self.product_area,
        }

    def __repr__(self):
        return '<FeatureRequest {}>'.format(self.id)

    def __str__(self):
        return self.title
