import unittest
import main 



class TestMain(unittest.TestCase):
    def test_cargardatos1(self):
        '''
        Trying with empty files...
        '''
        lista = []
        archivotxt = ''
        main.cargardatos(lista,archivotxt)
        '''
        Result: Added a try/except block in cargardatos
        '''
    def test_guardardatos1(self):
        '''
        Trying with empty files
        '''
        lista = []
        archivotxt = ''
        main.guardarcambios(lista,archivotxt)
        '''
        Result: Added an if statement to prevent that
        '''
    def test_nuevo1(self):
        '''
        Trying with empty files
        '''
        lista = []
        donante_donatario = ' '
        main.nuevo(lista,donante_donatario)
        '''
        result: everything is OK
        '''
    def test_nuevo2(self):
        '''
        Trying with existing users
        '''
        nombre = 'Hernan'
        apellido = 'Dominguez'
        donantes = []
        main.nuevo(donantes,' ')
        '''
        result = adding if statements to verify users first
        '''
unittest.main()