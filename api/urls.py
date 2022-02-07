from api import api
from . import views

api.add_resource(views.PersonView, '/person/')
api.add_resource(views.PersonEdit, '/person/<int:id>')