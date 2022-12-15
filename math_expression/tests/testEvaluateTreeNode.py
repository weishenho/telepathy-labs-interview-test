import unittest
from EvaluateStringExpression import EvaluateStringExpression

class TestBinaryTreeNode(unittest.TestCase):
    def setUp(self):
        self.EvaluateStringExpression = EvaluateStringExpression()

    def test_infix_to_postfix(self):
        result = self.EvaluateStringExpression.infix_to_postfix("2+4/5*(5-3)/2")
        self.assertEqual(result, list("245/53-*2/+"))
        
    def test_insert(self):
        self.EvaluateStringExpression.insert(list("245/53-*2/+"))
        self.assertIsNotNone(self.EvaluateStringExpression.root)

    def test_evaluate(self):
        self.EvaluateStringExpression.insert(list("245/53-*2/+"))
        result = self.EvaluateStringExpression.evaluate()
        self.assertEqual(result, 2.8)
   
    def test_main(self):
        result = self.EvaluateStringExpression.main("2+4/5*(5-3)/2")
        self.assertEqual(result, 2.8)
    
if __name__ == '__main__':
    unittest.main()