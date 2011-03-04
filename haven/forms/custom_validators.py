from wtforms.validators import ValidationError
from haven.models.account import Account

def username_unique(form, field):
    """ Checks that requested name is not
    already in database.
    """
    # TODO: This should really be a generic isUnique check.
    user = Account.by_name(field.data)
    if user:
        raise ValidationError(u'Name already in use.')
