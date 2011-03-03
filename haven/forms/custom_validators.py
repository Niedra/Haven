from wtforms.validators import ValidationError
from haven.models.account import Account

def check_name_avail(form, field):
    """ Checks if requested name is not
        already in database """
    user = Account.by_name(field.data)
    if user:
        raise ValidationError(u'Name already taken')
