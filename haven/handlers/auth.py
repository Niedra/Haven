"""Auth handler"""
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url
from pyramid_handlers import action

from webhelpers import paginate

from haven.forms.account import LoginForm
from haven.models.account import Account

class AuthHandler(object):
    def __init__(self, request):
        self.request = request

    @action(renderer='auth/login.mako')
    def login(self):
        """Login view"""
        form = LoginForm(self.request.POST)
        session = self.request.session
        if self.request.method == 'POST' and form.validate():
            account = Account.by_name(name=form.name.data)
            if account and account.check_password(form.password.data):
                authsession = {'id':account.id, 'name': account.name,
                               'is_admin' : account.is_admin}
                session["auth"] = authsession
                session.save()
                return HTTPFound(location = route_url('index', self.request))

        return {'form':form, 'project':'BEAuth'}

    def logout(self):
        """logout view"""
        session = self.request.session
        session["auth"] = None
        session.delete()
        return HTTPFound(location = route_url('index', self.request))
