import src.tasks.task


class TestTask:
    """
    Tests de la classe Task.
    """

    def test_getter_description(self):
        """Teste le getter de `__description` d'une tâche."""
        tache = src.tasks.task.Task("test de description")
        val = tache.description
        assert val == "test de description"

    def test_getter_state(self):
        """Teste le getter de '__state' d'une tache. """
        tache = src.tasks.task.Task("test d'etat", True)
        val = tache.state
        assert val is True

    def test_state_par_defaut(self):
        """Teste l'etat par defaut"""
        tache = src.tasks.task.Task("test d'etat par defaut")
        val = tache.state
        assert val is False

    def test_setter_description(self):
        """Teste le setter de `__description` d'une tâche."""
        tache = src.tasks.task.Task("test de description")
        tache.description = "nouvelle description"
        val = tache.description
        if tache.state == "à faire":
            assert val == "nouvelle description"

