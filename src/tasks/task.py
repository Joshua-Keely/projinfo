import logging
import datetime

import tasks.task

LOGGER = logging.getLogger(__name__)


class Task:
    """
    Classe modélisant une tâche.

    Avec :

    * son descriptif (attribut privé __description)
    """

    def __init__(self, description, state=False):
        """Constructeur.

        :param description: Le descriptif à renseigner pour la tâche
        :param state: L'etat de la tâche

        """
        self.__description = description
        self.__state = state
        self.__date = get_today()
        # Configuration de la journalisation pour l'objet
        LOGGER.info(f"Instantiation de la tâche \"{self.__description}\"")

    def __str__(self):
        """Méthode spéciale `__str__`.

        :return: La représentation textuelle de la tâche
        """
        LOGGER.info(f"Dans __str__")
        return f"{self.__description} ({'fait' if self.__state else 'à faire'})"

    @property
    def description(self):
        """Propriété `description`.

        :getter: Getter de `__description`
        :return: La description de la tâche
        """
        LOGGER.info(f"Dans le getter")
        return self.__description

    @property
    def state(self):
        """Propriété `state`.

        :getter: Getter de `state`
        :return:Etat de la tâche
        """
        LOGGER.info(f"State")
        return self.__state

    @description.setter
    def description(self, valeur):
        """Setter de `description`.

        La description ne peut être modifiée que si la tâche n'est pas faite.
        Sinon, renvoie une erreur de type :py:class:`AttributeError`.

        :param valeur: La nouvelle valeur de la `description`
        :return: :py:obj:`None`
        :raises: :py:class:`AttributeError` : `description` non modifiable pour une tâche faite
        """
        LOGGER.info(f"Dans setter de description")
        if not self.__state:
            self.__description = valeur
        else:
            raise AttributeError("La description ne peut être modifiée pour une tâche faite")

    def change_state(self):
        """Propriété `change_state`.
        fait passer l’état de la tâche a 'fait' si la tâche était 'à faire' et
        reciproquement (passage à 'à faire' si la tâche était faite).

        :return:Etat de la tâche
        """
        LOGGER.info(f"Change state")
        self.__state = not self.__state
        return self.__state

    @property
    def date(self):
        """renvoie la __date formaté au format "JJ/MM/AAAA
        :return: la date de la tâche"""
        LOGGER.info(f"Date")
        return self.__date.strftime("%d/%m/%Y")


def get_today():
    """Retourne la date du jour au format AAAA-MM-JJ.

    :return: La date du jour
    :rtype: str
    :see also: :py:obj:`datetime.date`
    """
    LOGGER.info(f"Get today")
    return datetime.date.today()


def main():
    """
    Tests manuels
    """
    tache = Task("Première tache")
    tache.description = "Description"
    tache = Task("Une description")
    tache.description = "Une nouvelle description"
    print(tache.date)


if __name__ == "__main__":
    # Configuration de la journalisation
    logging.basicConfig(level=logging.DEBUG)

    main()
