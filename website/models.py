from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class fs_acuserprofiles(db.Model, UserMixin):
    Id = db.Column(db.Integer, primary_key=True)
    EmployeeId = db.Column(db.Integer, nullable=False)
    FirstName = db.Column(db.String(150))
    LastName = db.Column(db.String(150))
    Email = db.Column(db.String(150), nullable=False, unique=True)
    PasswordHash = db.Column(db.String(150), nullable=False)
    SecurityStamp = db.Column(db.String(150),default='monyoncho')
    PhoneNumber = db.Column(db.String(150),default='+254712675612')
    UserName = db.Column(db.String(150), nullable=False, unique=True)
    is_active = db.Column(db.Boolean, nullable=True)
    AccountLockedOut = db.Column(db.Integer,default=0)
    CountToLock = db.Column(db.Integer ,default=3)
    LockoutEnabled = db.Column(db.Integer,default=1)
    AccessFailedCount = db.Column(db.Integer,default=1)
    NextLoginResetPassword = db.Column(db.Integer,default=0)
    LastModifiedBy = db.Column(db.String(150))
    LastModifiedDate = db.Column(
    db.DateTime, default=func.now(), onupdate=func.now())
    CreatedBy = db.Column(db.String(150))
    CreatedDate = db.Column(db.DateTime, default=func.now())    
      
    def get_id(self):
        return(self.Id)
