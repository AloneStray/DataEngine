from  .test_klf import testObj
from  .index import indexObj
# from .user import *
# from .loglist import *
#
def init_view(app):
     app.register_blueprint(testObj, url_prefix='/users')#
     #app.register_blueprint(testObj, url_prefix='/data')
     app.register_blueprint(indexObj) #
     #app.register_blueprint(op_admin)
     #app.register_blueprint(op_loglist)
     pass