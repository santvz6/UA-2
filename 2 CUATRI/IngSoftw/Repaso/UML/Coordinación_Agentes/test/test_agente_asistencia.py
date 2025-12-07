import unittest
from unittest.mock import patch, Mock, MagicMock
from agentes import AgenteAsistencia
from tarea import Tarea


class TestAgenteAsistenciaClass(unittest.TestCase):

    agente = AgenteAsistencia()

    def test_read_estado(self):
        estado = TestAgenteAsistenciaClass.agente.estado
        self.assertIn(estado, "LIBRE")
    
    def test_write_estado(self):
        with self.assertRaises(AttributeError):
            TestAgenteAsistenciaClass.agente.estado = "TEST"

    def test_read_tipo(self):
        estado = TestAgenteAsistenciaClass.agente.get_tipo()
        self.assertIn(estado, "ASISTENCIA")
    
    def test_write_tipo(self): 
        TestAgenteAsistenciaClass.agente.tipo = "TEST"
        self.assertIn(TestAgenteAsistenciaClass.agente.tipo, "TEST")
            
    def test_tarea_logs(self):
        
        expected_logs = [
            "INFO:agentes.agenteAsistencia:Procesando Tarea: Tarea1.",
            "INFO:agentes.agenteAsistencia:Tarea Procesada."
        ]

        with self.assertLogs("agentes.agenteAsistencia", level="INFO") as log:
            TestAgenteAsistenciaClass.agente.ejecutar_tarea(Tarea("Tarea1", "ASISTENCIA", "PENDIENTE"))

            for expected in expected_logs:
                self.assertIn(expected, log.output)
        
        estado = TestAgenteAsistenciaClass.agente.estado
        self.assertIn(estado, "LIBRE")

    
    @patch("tarea.Tarea")
    def test_change_task_state(self, mock_tarea_cls: Mock):

        tarea_mock = MagicMock()
        tarea_mock.estado = "COMPLETADA"
        TestAgenteAsistenciaClass.agente.ejecutar_tarea(Tarea("Tarea1", "ASISTENCIA", "PENDIENTE"))