import unittest
from agentes import AgenteComercial
from tarea import Tarea


class TestAgenteComercialClass(unittest.TestCase):

    agente = AgenteComercial()


    def test_read_tipo(self):
        estado = TestAgenteComercialClass.agente.get_tipo()
        self.assertIn(estado, "COMERCIAL")
            
    def test_tarea_logs(self):
        
        expected_logs = [
            "INFO:agentes.agenteComercial:Procesando Tarea: Tarea2.",
            "INFO:agentes.agenteComercial:Tarea Procesada."
        ]

        with self.assertLogs("agentes.agenteComercial", level="INFO") as log:
            TestAgenteComercialClass.agente.ejecutar_tarea(Tarea("Tarea2", "COMERCIAL", "PENDIENTE"))

            for expected in expected_logs:
                self.assertIn(expected, log.output)
        

    