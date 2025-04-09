import pytest 
from fatorial import fatorial

@pytest.mark.parametrize("Numero, expected", [(5, 120),(7,5040)])

def test_factorial(Numero, expected):
    assert fatorial(Numero) == expected

# -----------------------------------------------
# def test_fatorial_positivo(self):
#         self.assertEqual(fatorial(5), 120)  
#         self.assertEqual(fatorial(7), 5040) 
#         self.assertEqual(fatorial(10), 3628800)    

# -------------------------------------------------------

# class TestFatorial(unittest.TestCase):

   
#     def test_fatorial_zero(self):
#         self.assertEqual(fatorial(0), 1)
#     def test_fatorial_um(self):
#         self.assertEqual(fatorial(1), 1)  