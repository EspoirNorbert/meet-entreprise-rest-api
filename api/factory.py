from api.models import Participant , Room , Meet
from werkzeug.security import generate_password_hash

class ObjectFactory:
    @staticmethod
    def create_participant(data, email):
        """
        Crée un objet Participant à partir des données fournies.

        Args:
            data: Données du participant.
            email: Adresse e-mail du participant.

        Returns:
            Participant: Objet Participant créé.
        """
        firstname = data['firstname']
        lastname = data['lastname']
        gender = data['gender']
        password = "user"
        hashed_password = generate_password_hash(password)
        return Participant(firstname=firstname, lastname=lastname, gender=gender, email=email, password=hashed_password)

    @staticmethod
    def create_room(data):
        """
        Crée un objet Room à partir des données fournies.

        Args:
            data: Données de la salle.

        Returns:
            Room: Objet Room créé.
        """
        name = data['name']
        capacity = data['capacity']
        return Room(name=name, capacity=capacity, state=0)

    @staticmethod
    def create_meet(data, room):
        """
        Crée un objet Meet à partir des données fournies.

        Args:
            data: Données de la réunion.
            room: Objet Room associé à la réunion.

        Returns:
            Meet: Objet Meet créé.
        """
        subject = data['subject']
        hour = data['hour']
        return Meet(subject=subject, hour=hour, room=room)
