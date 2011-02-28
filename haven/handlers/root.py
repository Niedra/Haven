"""Root handler"""
from pyramid_handlers import action

class RootHandler(object):
    def __init__(self, request):
        self.request = request

    @action(renderer='root.mako')
    def index(self):
        """Index view, currently just a static page."""
        return {}
