from BinaryTreeNode import BinaryTreeNode
import sys
import re


class EvaluateStringExpression:
    def __init__(self) -> None:
        self.root = None

    def is_operator(self, x:str) -> bool:
        return x in "+-/*"

    def evaluate(self, node=None) -> float:
        """
        Calculate this tree expression recursively

        Args:
            node(BinaryTreeNode): starts at the root node
        """
        # initialize

        if node is None:
            node = self.root

        # empty tree
        if node is None:
            return 0

        # check if we are at the leaf, it means it is a operand
        if node.is_leaf():
            return float(node.data)

        left_value = self.evaluate(node.left)
        right_value = self.evaluate(node.right)

        # addition
        if node.data == "+":

            return left_value + right_value
        # subtraction
        elif node.data == "-":
            return left_value - right_value
        # division
        elif node.data == "/":
            return left_value / right_value
        # multiplication
        elif node.data == "*":
            return left_value * right_value
        # power
        else:
            return left_value ** right_value

    def insert(self, postfix_exp: list[str]):
        """
        Insert the postfix expression into the tree using stack
        """
        stack = []
        for char in postfix_exp:
            # if char is float or int
            if not self.is_operator(char):
                # create a node and push the node into the stack
                node = BinaryTreeNode(char)
                stack.append(node)
            else:
                right = stack.pop() 
                left = stack.pop()
                operator_node = BinaryTreeNode(char, left, right, True)
                stack.append(operator_node)
        self.root = stack.pop()

    def infix_to_postfix(self, infix_input: str) -> list:
        """
        Converts infix expression to postfix.
        Args:
            infix_input(str): infix expression user entered
        """

        # precedence order and associativity helps to determine which
        # expression is needs to be calculated first
        precedence_order = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, "(":-1}
        infix_cleaned = list(infix_input.replace(" ", ""))
        postfix = []
        stack = []
        operand = []
        for i in range(len(infix_cleaned)):
            char = infix_cleaned[i]

            if (char == "÷"):
                char = "/"
            elif (char == "×"):
                char = "*"
            elif (char == "−"):
                char = "-"
            elif (char == "+"):
                char = "+"

            # handle negative operand
            if(char == "-" and (i-1 < 0 or (not infix_cleaned[i-1].isdigit() and infix_cleaned[i+1].isdigit()))):
                operand.append(char)
                continue

            # handle multiple digit operand
            if(char.isdigit()):
                operand.append(char)
                continue
            # combine the different characters of the operands into a single token and push to stack
            if len(operand) > 0:
                postfix.append("".join(operand))
                operand = []

            if char == '(':
                # add it to the stack
                stack.append(char)
            elif char == '^':
                # add it to the stack
                stack.append(char)
            elif char == ')':
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                # now we pop opening parenthases and discard it
                stack.pop()
            # char is operator
            else:
                while len(stack) > 0 and precedence_order[char] <= precedence_order[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(char)

        if len(operand) > 0:
            postfix.append("".join(operand))
            operand = []
        # empty the stack
        while len(stack) > 0:
            postfix.append(stack.pop())

        return postfix
    
    def main(self,infix_expression):

        postfix_expression_list = self.infix_to_postfix(infix_expression)
        # print(postfix_expression_list)
        self.insert(postfix_expression_list)
        if(self.root):
            # print(self.root.data)
            result = self.evaluate()
            return result

if __name__ == "__main__":
    EvaluateStringExpression = EvaluateStringExpression()
    # result = EvaluateStringExpression.infix_to_postfix("2+4/5*(5-3)/2")
    # print(result)
    result = EvaluateStringExpression.main(sys.argv[1])
    print(result)