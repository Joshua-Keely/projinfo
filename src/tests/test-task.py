import src.tasks.task

class TestTask:
    """
    Tests de la classe Task.
    """

    def test_getter_description(self):
        """Teste le getter de `__description` d'une tâche."""
        tache = src.tasks.task.Task("A faire rapidement")
        val = tache.description
        assert val == "A faire rapidement"

    def test_getter_taste(self):
        """Teste le getter de '__state' d'une tache. """
        tache = src.tasks.task.Task("A faire rapidement", True)
        val = tache.state
        assert val is False

    def test_state_par_defaut(self):
        """Teste l'etat par defaut"""
        tache = src.tasks.task.Task("A faire rapidement")
        val = tache.state
        assert val is False
