from app import db
import comm


class Record(db.Model):
    __tablename__ = 'record'
    object_id = db.Column(db.String, primary_key=True, unique=True, default=comm.create_primary_key())
    record_time = db.Column(db.Datetime)
    done_thing = db.Column(db.Text)
