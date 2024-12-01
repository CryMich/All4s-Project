from App.database import db
from .user import User

class Student(User):
    __tablename__ = 'student'
    ID = db.Column(db.Integer, db.ForeignKey('user.ID'), primary_key=True)
    UniId = db.Column(db.String(10), nullable=False)
    degree = db.Column(db.String(120), nullable=False)
    fullname = db.Column(db.String(255), nullable=True)
    admittedTerm = db.Column(db.String(120), nullable=False)
    gpa = db.Column(db.String(120), nullable=True)
    karma = db.Column(db.Integer, default=0)

    reviews = db.relationship('Review', backref='studentReviews', lazy='joined')
    accomplishments = db.relationship('Accomplishment', backref='studentAccomplishments', lazy='joined')
    incidents = db.relationship('IncidentReport', backref='studentIncidents', lazy='joined')
    grades = db.relationship('Grades', backref='studentGrades', lazy='joined')
    transcripts = db.relationship('Transcript', backref='student', lazy='joined')
    badges = db.relationship('Badges', backref='studentbadge', lazy='joined')

    __mapper_args__ = {"polymorphic_identity": "student"}

    def __init__(self, username, UniId, firstname, lastname, email, password, faculty, admittedTerm, degree, gpa):
        super().__init__(username=username, firstname=firstname, lastname=lastname, email=email, password=password, faculty=faculty)
        self.UniId = UniId
        self.degree = degree
        self.fullname = f"{firstname} {lastname}"
        self.admittedTerm = admittedTerm
        self.gpa = gpa
        self.karma = 0
        self.reviews = []
        self.accomplishments = []
        self.incidents = []
        self.grades = []
        self.transcripts = []
        self.badges = []

    def get_id(self):
        return self.ID

    def to_json(self):
        return {
            "studentID": self.ID,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "gpa": self.gpa,
            "email": self.email,
            "faculty": self.faculty,
            "degree": self.degree,
            "admittedTerm": self.admittedTerm,
            "UniId": self.UniId,
            "accomplishments": [accomplishment.to_json() for accomplishment in self.accomplishments],
            "incidents": [incident.to_json() for incident in self.incidents],
            "grades": [grade.to_json() for grade in self.grades],
            "transcripts": [transcript.to_json() for transcript in self.transcripts],
            "karmaScore": self.karma,
        }
