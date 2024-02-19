import unittest
from Sales import SalesTaxes
class TestSales(unittest.TestCase):
    def test_input1(self):
        input_file = "inputs/demo.txt"
        output_file = "output/actual1.txt"
        ST = SalesTaxes()
        ST.getInputFile(input_file)
        ST.processInput()
        ST.dumpOutput(output_file)
        expected_output = "output/expected1.txt"
        self.assertListEqual(list(open(output_file)), list(open(expected_output)))
    
    


if __name__ == '__main__':
    unittest.main()