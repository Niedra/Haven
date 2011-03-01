"""Root handler"""
from pyramid_handlers import action

class RootHandler(object):
    def __init__(self, request):
        self.request = request

    @action(renderer='index.mako')
    def index(self):
        """Index view, currently just session info."""
        session = self.request.session
        return {'session':session}
