import tasks.task
import pytest
import datetime
from mock import mock

class TestTask:
    """
    Tests de la classe Task.
    """

    def test_getter_description(self):
        """Teste le getter de `__description` d'une tâche."""
        tache = tasks.task.Task("test de description")
        val = tache.description
        assert val == "test de description"

    def test_getter_state(self):
        """Teste le getter de '__state' d'une tache. """
        tache = tasks.task.Task("test d'etat", True)
        val = tache.state
        assert val is True

    def test_state_par_defaut(self):
        """Teste l'etat par defaut"""
        tache = tasks.task.Task("test d'etat par defaut")
        val = tache.state
        assert val == False

    def test_setter_description(self):
        """Teste le setter de `__description` d'une tâche."""
        tache = tasks.task.Task("test de description")
        tache.description = "nouvelle description"
        val = tache.description
        if tache.state == "à faire":
            assert val == "nouvelle description"

    @pytest.mark.parametrize("etat_ini, etat_final",
                             [
                                 pytest.param(False, True, id="a faire->fait"),
                                 pytest.param(True, False, id="fait->a faire")
                             ])
    def test_change_state(self, etat_ini, etat_final):
        tache = tasks.task.Task("Un descriptif", state=etat_ini)
        tache.change_state()
        assert tache.state == etat_final

    # def test_date(self):
    #     """Teste la date de création de la tâche."""
    #     tache = src.tasks.task.Task("test de date")
    #     val = tache.date
    #     assert val == datetime.date.today()

    @mock.patch('tasks.task.get_today',
                return_value=datetime.date.fromisoformat("2023-08-23"))
    def test_getter_date(self, mocker):
        tache = tasks.task.Task("un descriptif")
        assert tache.date == "23/08/2023"

