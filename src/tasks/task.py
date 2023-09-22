import logging

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
        # Configuration de la journalisation pour l'objet
        LOGGER.info(f"Instantiation de la tâche \"{self.__description}\"")

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
        if self.__state:
            raise AttributeError("La description ne peut être modifiée pour une tâche faite")
        self.__description = valeur








def main():
    """
    Tests manuels
    """
    tache = Task("Première tache")
    tache.description = "Description"
    tache = Task("Une description")
    tache.description = "Une nouvelle description"

if __name__ == "__main__":
    # Configuration de la journalisation
    logging.basicConfig(level=logging.DEBUG)

    main()