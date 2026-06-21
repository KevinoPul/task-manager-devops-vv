import unittest
from app import app, tasks

class TaskManagerTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        tasks.clear()

    def test_home_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        response = self.client.post("/add", data={
            "title": "Tarea de prueba",
            "status": "Pendiente"
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tarea de prueba", response.data)

    def test_empty_task_validation(self):
        response = self.client.post("/add", data={
            "title": "",
            "status": "Pendiente"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"El nombre de la tarea no puede estar", response.data)

if __name__ == "__main__":
    unittest.main()
