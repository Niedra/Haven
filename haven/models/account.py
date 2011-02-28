import cryptacular.bcrypt
import transaction

from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import Unicode

from sqlalchemy.ext.hybrid import hybrid_property

from haven.models import Base
from haven.models import DBSession

bcrypt = cryptacular.bcrypt.BCRYPTPasswordManager()

class Account(Base):
    """Account model"""
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)
    email = Column(Unicode(255), unique=True)
    activated = Column(Boolean, default=False)
    verify_code = Column(Unicode(20))

    _password = Column(Unicode(255))

    def __init__(self, name, password, email, activated, verify_code=None):
        self.name = name
        self.password = password
        self.email = email
        self.activated = activated
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
    def by_name(cls, name):
        return DBSession.query(cls).filter(cls.name == name).first()

    @classmethod
    def like(cls, name):
        return DBSession.query(cls).filter(cls.name.like('%'+name+'%')).all()

    def check_password(self, password):
        return bcrypt.check(self.password, password)
