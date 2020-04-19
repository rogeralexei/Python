import unittest
import main 



class TestMain(unittest.TestCase):
    def test_autenticador1(self):
        '''It will return false if I add a random int, as expected'''
        fallo = True
        num = 8-970524 #Everityhing is manually, so I don't need this variable. But I put it to show my test num
        result = main.autenticador(fallo)
        self.assertFalse(result)
    def test_autenticador2(self):
        '''It will return false if I add a string, as expected'''
        fallo = True
        num = 'Hello' #Everityhing is manually, so I don't need this variable. But I put it to show my test num
        result = main.autenticador(fallo)
        self.assertFalse(result)
    def test_siono1(self):
        '''It will return True if I don't put the correct word, as expected'''
        arg = 'tal vez'
        result = main.siono(arg)
        self.assertTrue(result)
unittest.main()