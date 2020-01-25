from flask_restplus import Api, Resource, fields, abort
from .dao import ClientDao

api = Api(default='clients', default_label='Operations with clients')


client_post_dto = api.model('Root Type for clientPOST', {
    'last_name': fields.String(),
    'first_name': fields.String(),
    'dob': fields.Date(),
    'social_status_id': fields.Integer(),
    'gender': fields.String()
})

client_dto = api.model('Root Type for client', {
    'id': fields.Integer(),
    'last_name': fields.String(),
    'first_name': fields.String(),
    'dob': fields.Date(),
    'social_status_id': fields.Integer(),
    'social_status': fields.String(),
    'gender_id': fields.String(),
    'gender': fields.String()
})


@api.route('/clients')
class ClientList(Resource):
    """
    Shows a list of all clients and allows to create add client with POST request
    """
    @api.doc('list_clients')
    @api.marshal_list_with(client_dto)
    def get(self):
        """
        returns a list of clients
        """
        return ClientDao.get_all()

    @api.doc('create_client')
    @api.expect(client_post_dto)
    @api.marshal_with(client_dto)
    @api.response(400, 'Some error')
    def post(self):
        """
        adds a new client to db
        """
        return ClientDao.create(api.payload)


@api.route('/clients/<int:client_id>')
class Clients(Resource):
    """
    Show a single client details
    """
    @api.doc('get_todo')
    @api.marshal_with(client_dto)
    @api.response(404, 'Client not found')
    def get(self, client_id):
        """
        return client by id
        """
        client = ClientDao.get(client_id)
        if not client:
            abort(404, 'Client not found')

        return client
