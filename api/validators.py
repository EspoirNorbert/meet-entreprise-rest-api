
class Validator:
    @staticmethod
    def check_hour(hour: str) -> bool:
        """
        Vérifie si l'heure est au format valide (HH:MM).

        Args:
            hour (str): Heure au format HH:MM.

        Returns:
            bool: True si l'heure est valide, sinon False.
        """
        try:
            hour, minutes = map(int, hour.split(':'))
            return 0 <= hour <= 23 and 0 <= minutes <= 59
        except ValueError:
            return False

    @staticmethod
    def check_json_data(data) -> bool:
        """
        Vérifie si les données JSON sont vides.

        Args:
            data: Données JSON.

        Returns:
            bool: True si les données sont vides, sinon False.
        """
        return data is None or data == ''

    @staticmethod
    def check_gender(gender: str) -> bool:
        """
        Vérifie si le genre est valide (F ou M).

        Args:
            gender (str): Genre à vérifier.

        Returns:
            bool: True si le genre est valide, sinon False.
        """

        return gender in {'F', 'M'}

    @staticmethod
    def check_validity_data(data, entity: str) -> str:
        """
        Vérifie la validité des données pour une entité donnée.

        Args:
            data: Données à valider.
            entity (str): Nom de l'entité ('participant', 'room' ou 'meet').

        Returns:
            str: Message d'erreur en cas de données non valides, sinon une chaîne vide.
        """
        if entity == 'participant':
            required_fields = ['firstname', 'lastname', 'gender']
        elif entity == 'room':
            required_fields = ['name', 'capacity']
        elif entity == 'meet':
            required_fields = ['subject', 'hour', 'room', 'participants']
        else:
            return ''

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return ', '.join([f'{field} required' for field in missing_fields])

        return ''
