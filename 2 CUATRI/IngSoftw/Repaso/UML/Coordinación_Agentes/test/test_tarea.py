import unittest
from tarea import Tarea


class TestTareaClass(unittest.TestCase):

    def test_tipo_error(self):
        with self.assertRaises(ValueError):
            Tarea("Tarea 1", "error", "PENDIENTE")

    def test_estado_error(self):
        with self.assertRaises(ValueError):
            Tarea("Tarea 1", "ASISTENCIA", "error")

    def test_tipo_correcto(self):
        tarea = Tarea("Tarea 1", "ASISTENCIA", "PENDIENTE")
        self.assertEqual(tarea.descripcion, "Tarea 1")
        self.assertEqual(tarea.tipo, "ASISTENCIA")
        self.assertEqual(tarea.estado, "PENDIENTE")