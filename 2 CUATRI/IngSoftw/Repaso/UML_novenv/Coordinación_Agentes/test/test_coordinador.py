import unittest
from unittest.mock import patch, Mock
from tarea import Tarea
from coordinador import Coordinador
from agentes.agenteAsistencia import AgenteAsistencia
from agentes.agenteComercial import AgenteComercial

class TestTareaClass(unittest.TestCase):

    def setUp(self):
        self.coordinador = Coordinador()  # se crea después del patch

    def test_tiene_agentes(self):
        self.assertGreater(len(self.coordinador), 0)

    def test_everyone_working(self):
        for agente in self.coordinador.agentes:
            self.coordinador.asignar_tarea(Tarea("Tarea", "COMERCIAL", "PENDIENTE"))
            

    @patch.object(AgenteAsistencia, "ejecutar_tarea")
    @patch.object(AgenteComercial, "ejecutar_tarea")
    def test_ejecutar_tarea(self, mock_comercial: Mock, mock_asistencia: Mock):
        t1 = Tarea("Tarea 1", "ASISTENCIA", "PENDIENTE")
        t2 = Tarea("Tarea 2", "COMERCIAL", "PENDIENTE")

        self.coordinador.asignar_tarea(t1)
        self.coordinador.asignar_tarea(t2)

        mock_asistencia.assert_called_once_with(t1)
        mock_comercial.assert_called_once_with(t2)


    @patch.object(AgenteAsistencia, "ejecutar_tarea")
    def test_asistentes_ocupados(self, mock_asistencia: Mock):
        t = Tarea("Tarea difícil", "ASISTENCIA", "PENDIENTE")
        for agente in self.coordinador.agentes:
            if agente.get_tipo() == "ASISTENCIA":
                agente.bloquear()

        self.coordinador.asignar_tarea(t)
        mock_asistencia.assert_not_called()
        
    
   