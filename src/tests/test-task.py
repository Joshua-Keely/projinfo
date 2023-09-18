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