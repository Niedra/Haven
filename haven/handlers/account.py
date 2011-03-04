"""Account handler"""
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url
from pyramid_handlers import action

from webhelpers import paginate

from haven.forms.account import RegistrationForm
from haven.forms.account import LoginForm
from haven.lib.paginate import list_users_url_generator
from haven.models.account import Account

class AccountHandler(object):
    def __init__(self, request):
        self.request = request

    @action(renderer='account/view.mako')
    def view(self):
        """View a user's account page."""
        id = self.request.matchdict['id']
        account = Account.by_id(id=id)
        return {'account':account}

    @action(renderer='account/register.mako')
    def register(self):
        account = Account(name=None, password='', email=None, activated=False,
                          is_admin = False)
        form = RegistrationForm(self.request.POST)
        if self.request.method == 'POST' and form.validate():
            account.name = form.name.data
            account.password = form.password.data
            account.email = form.email.data
            Account.add(account)
            return HTTPFound(location = route_url('account_view',
                                                  self.request,
                                                  id=account.id))
        return {'form':form}

    @action(renderer='account/list.mako')
    def list(self):
        page_number = self.request.GET.get('page', '1')
        query = self.request.GET.get('query', '')
        # TODO: Remove DBSession and move query to model.
        accounts = Account.list()
        currentPage = paginate.Page(accounts, page=page_number,
                                    items_per_page=10,
                                    url=list_users_url_generator)
        return {'currentPage':currentPage, 'accounts':currentPage.items}
