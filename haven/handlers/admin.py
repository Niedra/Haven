"""Account handler"""
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url
from pyramid_handlers import action

from haven.models.account import Account

class AdminHandler(object):
    def __init__(self, request):
        self.request = request

    @action(renderer='admin/activate.mako')
    def activate(self):
        """ Activate accounts """
        if 'id' in self.request.matchdict:
            id = self.request.matchdict['id']
            account = Account.by_id(id=id)
            account.activated = True
            Account.add(account)
            return HTTPFound(location = route_url('admin_activate_list',
                                                  self.request))


        accounts = Account.by_inactivated()
        return {'accounts':accounts}

