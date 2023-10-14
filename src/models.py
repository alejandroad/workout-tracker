from . import db
from sqlalchemy import Column, Integer, ForeignKey, String, Enum
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    workouts = db.relationship("Workout", backref="user")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User(name='%s')>" % (self.name)

    def as_dict(self):
        fields = {}

        for c in self.__table__.columns:
            fields[c.name] = getattr(self, c.name)
        return fields

class Exercise(db.Model):
    __tablename__ = 'exercise'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    url = Column(String)
    muscle_worked = Column(String)
    workouts = db.relationship('Workout', secondary='workout_exercise_association', back_populates='exercises')

    def __repr__(self):
        return "<Exercise(name='%s')>" % (self.name)

    def as_dict(self):
        fields = {}

        for c in self.__table__.columns:
            fields[c.name] = getattr(self, c.name)
        return fields

class Workout(db.Model):
    __tablename__ = 'workout'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    exercises = db.relationship('Exercise', secondary='workout_exercise_association', back_populates='workouts')

    def __repr__(self):
        return "<Workout(name='%s')>" % (self.name)

    def as_dict(self):
        fields = {}

        for c in self.__table__.columns:
            fields[c.name] = getattr(self, c.name)
        return fields

class WorkoutExerciseAssociation(db.Model):
    __tablename__ = 'workout_exercise_association'
    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workout.id'))
    exercise_id = Column(Integer, ForeignKey('exercise.id'))
    repetitions = Column(Integer)
    sets = Column(Integer)
    weight = Column(Integer)
    WeightUnit = Enum("kg", "lbs", name="weight_unit")
    unit = Column(WeightUnit)




