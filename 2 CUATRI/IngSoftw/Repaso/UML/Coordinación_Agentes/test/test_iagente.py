import unittest
from agentes import AgenteAsistencia, AgenteComercial, IAgente
from tarea import Tarea

class TestAgenteAsistenciaImplementsIAgente(unittest.TestCase):
    
    def test_is_instance_of_iagente(self):
        agenteAsistencia = AgenteAsistencia()
        self.assertIsInstance(agenteAsistencia, IAgente)

        AgenteComercial = AgenteAsistencia()
        self.assertIsInstance(AgenteComercial, IAgente)

    def test_is_abstract(self):
        with self.assertRaises(TypeError):
           iAgente = IAgente() 


