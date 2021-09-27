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


class fs_acuserprofiles(db.Model):
    UserId = db.Column(db.Integer, primary_key=True)
    EmployeeId = db.Column(db.Integer, nullable=False)
    FirstName = db.Column(db.String(150))
    LastName = db.Column(db.String(150))
    Email = db.Column(db.String(150), nullable=False, unique=True)
    PasswordHash = db.Column(db.String(150), nullable=False)
    SecurityStamp = db.Column(db.String(150))
    PhoneNumber = db.Column(db.String(150))
    UserName = db.Column(db.String(150), nullable=False, unique=True)
    AccountLockedOut = db.Column(db.Integer)
    CountToLock = db.Column(db.Integer)
    LockoutEnabled = db.Column(db.Integer)
    AccessFailedCount = db.Column(db.Integer)
    NextLoginResetPassword = db.Column(db.Integer)
    LastModifiedBy = db.Column(db.String(150))
    LastModifiedDate = db.Column(
    db.DateTime, default=func.now(), onupdate=func.now())
    CreatedBy = db.Column(db.String(150))
    CreatedDate = db.Column(db.DateTime, default=func.now())
    
    def __init__(self, EmployeeId, FirstName, LastName, Email, PasswordHash,
                 SecurityStamp, PhoneNumber, UserName, AccountLockedOut, CountToLock, LockoutEnabled, AccessFailedCount, NextLoginResetPassword, LastModifiedBy, LastModifiedDate, CreatedBy, CreatedDate):
       EmployeeId.username = EmployeeId
       self.FirstName = FirstName
       self.LastName = LastName
       self.Email = Email
       self.PasswordHash = PasswordHash
       self.SecurityStamp = SecurityStamp
       self.PhoneNumber = PhoneNumber
       self.AccountLockedOut = AccountLockedOut
       self.UserName = UserName
       self.CountToLock = CountToLock
       self.LockoutEnabled = LockoutEnabled
       self.AccessFailedCount = AccessFailedCount
       self.NextLoginResetPassword = NextLoginResetPassword
       self.LastModifiedBy = LastModifiedBy
       self.LastModifiedDate = LastModifiedDate
       self.CreatedBy = CreatedBy
       self.CreatedDate = CreatedDate       

