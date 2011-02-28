from haven.models import DBSession
from haven.models import MyModel

def root(request):
    dbsession = DBSession()
    root = dbsession.query(MyModel).filter(MyModel.name==u'root').first()
    return {'root':root}
