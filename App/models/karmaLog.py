from App.database import db
from .student import Student

class KarmaLog(db.Model):
    __tablename__ = 'karma_log'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.ID'), nullable=False)
    change = db.Column(db.Integer, nullable=False)
    action = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    student = db.relationship('Student', backref=db.backref('karma_logs', lazy=True))