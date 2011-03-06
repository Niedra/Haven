import cryptacular.bcrypt
import transaction
import uuid

from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import Binary
from sqlalchemy import DateTime

from sqlalchemy.ext.hybrid import hybrid_property

from haven.models import Base
from haven.models import DBSession

from datetime import datetime

bcrypt = cryptacular.bcrypt.BCRYPTPasswordManager()

class Account(Base):
    """Account model"""
    __tablename__ = 'accounts'
    import uuid
    id = Column(Binary(16), primary_key=True, default=uuid.uuid4().bytes)
    name = Column(Unicode(255), unique=True)
    email = Column(Unicode(255), unique=True)
    activated = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.now())
    date_updated = Column(DateTime, default=datetime.now())
    is_admin = Column(Boolean, default=True)
    verify_code = Column(Unicode(20))

    _password = Column(Unicode(255))

    def __init__(self, name, password, email, activated, is_admin,
                 date_updated=datetime.now(), verify_code=None):
        self.name = name
        self.password = password
        self.email = email
        self.activated = activated
        self.date_updated = date_updated
        self.is_admin = is_admin
        self.verify_code = verify_code

    @hybrid_property
    def password(self):
        """Return the account's (hashed) password."""
        return self._password

    @password.setter
    def set_password(self, value):
        """Accept a value, hash it and set it as the account password."""
        hashed = bcrypt.encode(value)
        self._password = unicode(hashed)

    @classmethod
    def by_id(cls, id):
        return DBSession.query(cls).filter(cls.id == id).first()

    @classmethod
    def by_name(cls, name):
        return DBSession.query(cls).filter(cls.name == name).first()

    @classmethod
    def by_inactivated(cls):
        return DBSession.query(cls).filter(cls.activated == False).all()

    @classmethod
    def like(cls, name):
        return DBSession.query(cls).filter(cls.name.like('%'+name+'%')).all()

    @classmethod
    def list(cls):
        return DBSession.query(cls)

    @classmethod
    def add(cls, account):
        DBSession.add(account)
        DBSession.flush() # This is required to set the ID.

    def check_password(self, password):
        return bcrypt.check(self.password, password)
