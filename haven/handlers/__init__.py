"""Handlers package"""

def add_handlers(config):
    # Root Handler
    config.add_handler('index', '/',
                       '.root:RootHandler', action='index')
    # Auth Handler
    config.add_handler('login', '/login',
                       '.auth:AuthHandler', action='login')
    config.add_handler('logout', '/logout',
                       '.auth:AuthHandler', action='logout')
    # Account Handler
    config.add_handler('account_list', '/account/list',
                       '.account:AccountHandler', action='list')
    config.add_handler('account_register', '/account/register',
                       '.account:AccountHandler', action='register')
    config.add_handler('account_view', '/account/{id}',
                       '.account:AccountHandler', action='view')
    # Admin Handler
    config.add_handler('admin_activate_list', '/admin/activate',
                       '.admin:AdminHandler', action='activate')
    config.add_handler('admin_activate', '/admin/activate/{id}',
                       '.admin:AdminHandler', action='activate')
