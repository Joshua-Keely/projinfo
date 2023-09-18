import logging

LOGGER = logging.getLogger(__name__)


class Task:
    """
    Classe modélisant une tâche.

    Avec :

    * son descriptif (attribut privé __description)
    """

    def __init__(self, description):
        """Constructeur.

        :param description: Le descriptif à renseigner pour la tâche
        """
        self.__description = description

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

def main():
    """
    Tests manuels
    """
    tache = Task("Première tache")
    tache.description

if __name__ == "__main__":
    # Configuration de la journalisation
    logging.basicConfig(level=logging.DEBUG)

    main()