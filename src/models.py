from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, String

from src import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///powerlifting.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String, unique=True, nullable=False)

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
    #unit = Column(Bool) # or maybe enums to signifiy lbs vs kg




