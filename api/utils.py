from sys import exc_info
from traceback import format_exception
from flask import make_response, jsonify , Response
from api.http_status_code import HTTP_201_CREATED , HTTP_200_OK
import datetime

class APIResponse:
    @staticmethod
    def created(data: dict, message="Entity created successfully") -> Response:
        """
        Renvoie une réponse au format standard pour une création d'entité.

        Args:
            data: Les données de l'entité créée.
            message (str): Le message de réussite.

        Returns:
            response: Réponse HTTP au format JSON.
        """
        response = {
            "code": HTTP_201_CREATED,
            "message": message,
            "data": data,
        }
        return make_response(jsonify(response), HTTP_201_CREATED)
    
    @staticmethod
    def response(data: dict) -> Response:
        """
        Renvoie une réponse HTTP au format JSON avec un code 200.

        Args:
            data: Les données à inclure dans la réponse.

        Returns:
            response: Réponse HTTP au format JSON avec un code 200.
        """
        return make_response(jsonify(data), HTTP_200_OK)

class Utils:
    @staticmethod
    def remove_whitespace(string: str) -> str:
        """
        Supprime les espaces d'une chaîne de caractères.

        Args:
            string (str): Chaîne de caractères à traiter.

        Returns:
            str: Chaîne de caractères sans espaces.
        """
        return "".join(string.split())

    @staticmethod
    def get_current_date() -> datetime:
        """
        Renvoie la date et l'heure actuelles.

        Returns:
            datetime: Objet datetime représentant la date et l'heure actuelles.
        """
        return datetime.utcnow()
    
    @staticmethod
    def format_datetime(date: datetime) -> str:
        """
        Formate une date au format 'JJ/MM/AAAA'.

        Args:
            date (datetime): Date à formater.

        Returns:
            str: Date formatée en 'JJ/MM/AAAA'.
        """
        return date.strftime("%d/%m/%Y")
    
    @staticmethod
    def generate_email(firstname: str, lastname: str) -> str:
        """
        Génère une adresse e-mail basée sur le prénom et le nom.

        Args:
            firstname (str): Prénom de l'utilisateur.
            lastname (str): Nom de l'utilisateur.

        Returns:
            str: Adresse e-mail générée.
        """
        # Génère l'e-mail en supprimant les espaces et en ajoutant un domaine fictif
        email = f"{lastname.lower()}.{firstname.lower()}@lamzone.com"
        return Utils.remove_whitespace(email)


    @staticmethod
    def print_exception():
        """
        Affiche les détails d'une exception.

        Cette méthode affiche les informations sur l'exception en cours, y compris le type d'exception, la valeur et la trace.

        Returns:
            None
        """
        etype, value, tb = exc_info()
        info, error = format_exception(etype, value, tb)[-2:]
        print(f'Exception in:\n{info}\n{error}')