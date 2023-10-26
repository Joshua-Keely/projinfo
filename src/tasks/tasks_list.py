"""Ce module prévoit :

    une fonction main pour centraliser les tests manuels

    de l’exécuter lorsque le fichier est exécuté en tant que script (if name=="main":)

    un système de log s’appuyant sur :
    LOGGER = logging.getLogger(self.__name__)
"""
listeTaches = []

import logging
import tasks.task

LOGGER = logging.getLogger(__name__)


def main():
    task1 = tasks.task.Task("tâche 1", True)
    task2 = tasks.task.Task("tâche 2", False)

    print(task1)
    print(task2)


def add_task(tache, listeTaches):
    """
    Ajoute la `tache` à la liste des tâches `listeTaches`.

    * Si `tache` est une chaine de caractères, instancie l'objet :py:class:`tasks.task.Task` qui lui correspond.
    * Si la `tache` est déjà présente (c'est à dire à le même descriptif qu'une tache de `listeTaches` peu importe l'état ou la date), l'ajout n'a pas lieu et une exception est levée de type :py:obj:`ValueError`

    :param tache: La tache à ajouter ou son descriptif
    :param listeTaches: La liste de tâches dans laquelle ajouter la tache
    :return: :py:obj:`None`
    """
    LOGGER.info(f"Ajout de la tâche {tache}")
    if isinstance(tache, str):
        tache = tasks.task.Task(tache)
    if tache in listeTaches:
        raise ValueError(f"La tâche {tache} est déjà présente dans la liste")
    listeTaches.append(tache)

def remove_done_tasks():
    """
    Supprime les tâches faites de la liste des tâches.

    :return: :py:obj:`None`
    """
    LOGGER.info(f"Suppression des tâches faites")
    for tache in listeTaches:
        if tache.state is "fait":
            listeTaches.remove(tache)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
