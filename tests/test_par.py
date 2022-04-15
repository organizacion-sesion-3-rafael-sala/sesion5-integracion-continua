# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_par(self):
        assert par(5) == False
        assert par(2) == True
        assert par(9) == False
        assert par(10) == True
