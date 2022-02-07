
from flask_restful import Resource, abort,marshal_with,fields,marshal,reqparse
from .models import PersonModel
from api import db
person_args = reqparse.RequestParser()
person_args.add_argument('name',type=str,help="name is required",required=True)
person_args.add_argument('Address',type=str,help="Address is required",required=True)
person_args.add_argument('Phone',type=str,help="Phone is required",required=True)

person_update_args = reqparse.RequestParser()
person_update_args.add_argument('name',type=str,help="name is required")
person_update_args.add_argument('Address',type=str,help="Address is required")
person_update_args.add_argument('Phone',type=str,help="Phone is required")

resource_fields = {
    'id':fields.Integer,
    'name':fields.String,
    'Address':fields.String,
    'Phone':fields.String,
    'created':fields.DateTime
}
class PersonView(Resource):
    def get(self):
        data = PersonModel.query.all()
        data = [marshal(d,resource_fields) for d in data]
        return data
    @marshal_with(resource_fields)
    def post(self):
        args = person_args.parse_args()
        ob = PersonModel(**args)
        db.session.add(ob)
        db.session.commit()
        return ob
class PersonEdit(Resource):
    @marshal_with(resource_fields)
    def get(self,id):
        ob = PersonModel.query.filter_by(id=id).first()
        if not ob:
            abort(404,message="data not found")
        return ob
    def delete(self,id):
        ob = PersonModel.query.filter_by(id=id).first()
        if not ob:
            abort(404,message="data not found")
        db.session.delete(ob)
        db.session.commit()
        return {'status':'ok',"message":"data deleted"}
    @marshal_with(resource_fields)
    def put(self,id):
        args = person_update_args.parse_args()
        newargs = {}
        for data in args:
            if args[data] is not None:
                newargs[data] = args[data]
        print(newargs)
        ob = PersonModel.query.filter_by(id=id)
        if not ob.first():
            abort(404,message="data not found")
        ob.update(newargs)
        # db.session.add(ob) 
        db.session.commit()
        return ob.first()