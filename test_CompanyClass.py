import unittest
from CompanyClass import Company

class TestCompany(unittest.TestCase):
    
    def setUp(self): # function that does something before each test method
        self.company1 = Company('United States', 'Oreo Inc', 55000, 100000)
        self.company2 = Company('Germany', 'Black&Decker', 3400, 89000)
    
    def tearDown(self): # unused function that does something after each test method
        pass
    
    def test_company_name(self): # test name property of class
        self.assertEqual(self.company1.name, 'Oreo Inc')
        self.assertEqual(self.company2.name, 'Black&Decker')

    def test_company_origin(self): # test origin property of class
        self.assertEqual(self.company1.country, 'United States')
        self.assertEqual(self.company2.country, 'Germany')
    
    def test_number_of_employees(self): # test output of check workers function
        self.assertEqual(self.company1.check_number_of_workers(), '55000 Total Employees')
        self.assertEqual(self.company2.check_number_of_workers(), '3400 Total Employees')
    
    def test_taxed_revenue_of_companies(self): # test taxed revenue output for accuracy
        self.assertEqual(self.company1.check_taxed_revenue(), 95000)
        self.assertEqual(self.company2.check_taxed_revenue(), 84550)



if __name__ == '__main__': # allows easier running of script
    unittest.main()