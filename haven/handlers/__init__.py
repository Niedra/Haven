"""Handlers package"""

def add_handlers(config):
    # Root Handler
    config.add_handler('index', '/',
                       '.root:RootHandler', action='index')
    # Root Handler
    config.add_handler('account_list', '/account/list',
                       '.account:AccountHandler', action='list')
    config.add_handler('account_view', '/account/{id}',
                       '.account:AccountHandler', action='view')
