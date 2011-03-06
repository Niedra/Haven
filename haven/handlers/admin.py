"""Account handler"""
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url
from pyramid_handlers import action

import uuid

from haven.models.account import Account

class AdminHandler(object):
    def __init__(self, request):
        self.request = request

    @action(renderer='admin/activate.mako')
    def activate(self):
        """ Activate accounts. Allows the admin to manually activate accounts
        as an alternative to email verification."""
        if 'id' in self.request.matchdict:
            id = uuid.UUID(self.request.matchdict['id']).bytes
            inactive_account = Account.by_id(id=id)
            inactive_account.activated = True
            Account.add(inactive_account)
            return HTTPFound(location = route_url('admin_activate_list',
                                                  self.request))


        accounts = Account.by_inactivated()
        return {'accounts':accounts}

