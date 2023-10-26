import logging
import unittest
import tasks.task
import tasks.tasks_list

LOGGER = logging.getLogger(__name__)

class TestTasksList(unittest.TestCase):
    """Tests for tasks_list.py"""
    def test_getter(self):
        """Test du getter de la propriété `description`"""
        task = tasks.task.Task("tâche 1", True)
        self.assertEqual(task.description, "tâche 1")

    def test_setter(self):
        """Test du setter de la propriété `description`"""
        task = tasks.task.Task("tâche 1", True)
        task.description = "tâche 2"
        self.assertEqual(task.description, "tâche 2")

    def test_add_task(self):
        """Test de la fonction `add_task`"""
        listeTaches = []
        tasks.tasks_list.add_task("tâche 1", listeTaches)
        self.assertEqual(len(listeTaches), 1)
        self.assertEqual(listeTaches[0].description, "tâche 1")
        self.assertEqual(listeTaches[0].state, False)
        self.assertEqual(listeTaches[0].date, tasks.task.Task.get_today())

    def test_add_task_exists(self):
        """Test de la fonction `add_task` avec une tâche déjà présente"""
        listeTaches = []
        tasks.tasks_list.add_task("tâche 1", listeTaches)
        with self.assertRaises(ValueError):
            tasks.tasks_list.add_task("tâche 1", listeTaches)
