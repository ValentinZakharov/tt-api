from .models import Client, Dictionary, db


class ClientDao:
    @staticmethod
    def get_all():
        """
        Get list of all clients from database including mapping with values from dictionary
        """
        client_list = [c.__dict__ for c in Client.query.all()]

        dictionary = Dictionary.query.all()
        gender_dict = {i.str_id: i.value for i in dictionary if i.category == 'gender'}
        social_dict = {i.int_id: i.value for i in dictionary if i.category == 'social_status_id'}

        for client in client_list:
            client['gender_id'] = client['gender']
            client['gender'] = gender_dict[client['gender']]
            client['social_status'] = social_dict[client['social_status_id']]

        return client_list

    @staticmethod
    def get(client_id):
        """
        Get client by given id from database including mapping with values from dictionary
        """
        client = Client.query.get(client_id)
        if client:
            client = client.__dict__
            gender = Dictionary.query.filter_by(category='gender', str_id=client['gender']).first().value
            social_status = Dictionary.query.filter_by(category='social_status_id',
                                                       int_id=client['social_status_id']).first().value

            client['gender_id'] = client['gender']
            client['gender'] = gender
            client['social_status'] = social_status

        return client

    @staticmethod
    def create(client_data):
        """
        Insert new client into database
        """
        client = Client(**client_data)
        db.session.add(client)
        db.session.commit()
        return client

    @staticmethod
    def delete(client_id):
        """
        Remove client from database by id
        """
        pass

    @staticmethod
    def update(client_id, client_data):
        """
        Update client
        """
        pass
