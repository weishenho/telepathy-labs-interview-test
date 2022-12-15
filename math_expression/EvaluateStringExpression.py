from BinaryTreeNode import BinaryTreeNode

class EvaluateStringExpression:
    def __init__(self) -> None:
        self.root = None

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
            val = float(node.data)

            return val

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

    def insert(self, postfix_exp: list):
        """
        Insert the postfix expression into the tree using stack
        """
        # postfix_exp = self.infix_to_postfix(expression)
        # if max size is 0, then it is infinite
        stack = []
        char = postfix_exp[0]
        # create a node for the first element of the expression
        node = BinaryTreeNode(char)
        # push it to stack
        stack.append(node)

        # iterator for expression
        i = 1
        self.size = 0
        while len(stack) != 0:
            char = postfix_exp[i]
            # if char is float or int
            if  char.isdigit():
                # create a node and push the node into the stack
                node = BinaryTreeNode(char)
                stack.append(node)
            else:
                # create a parent(operator) node for operands
                operator_node = BinaryTreeNode(char)
                operator_node.operator = True
                # pop the last pushed item and create right_child
                right_child = stack.pop()
                # pop item one before the last item and create left_child
                left_child = stack.pop()
                # assign those as a child of the (parent)operator
                operator_node.right = right_child
                operator_node.left = left_child
                # push back the operator node(subtree) to the stack
                stack.append(operator_node)
                # check if we reach last element in the expression
                # so we can define the root of the tree
                if len(stack) == 1 and i == len(postfix_exp) - 1:
                    self.root = stack.pop()
            # increment i
            i += 1
            # self.size += 1
        # print(f"i is {i} in insert ")

    def infix_to_postfix(self, infix_input: list) -> list:
        """
        Converts infix expression to postfix.
        Args:
            infix_input(list): infix expression user entered
        """

        # precedence order and associativity helps to determine which
        # expression is needs to be calculated first
        precedence_order = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
        associativity = {'+': "LR", '-': "LR", '*': "LR", '/': "LR", '^': "RL"}
        # clean the infix expression
        clean_infix = infix_input #self._clean_input(infix_input)

        i = 0
        postfix = []
        operators = "+-/*^"
        stack = []
        while i < len(clean_infix):

            char = clean_infix[i]
            # print(f"char: {char}")
            # check if char is operator
            if char in operators:
                # check if the stack is empty or the top element is '('
                if len(stack) == 0 or stack[-1] == '(':
                    # just push the operator into stack
                    stack.append(char)
                    i += 1
                # otherwise compare the curr char with top of the element
                else:
                    # peek the top element
                    top_element = stack[-1]
                    # check for precedence
                    # if they have equal precedence
                    if precedence_order[char] == precedence_order[top_element]:
                        # check for associativity
                        if associativity[char] == "LR":
                            # pop the top of the stack and add to the postfix
                            popped_element = stack.pop()
                            postfix.append(popped_element)
                        # if associativity of char is Right to left
                        elif associativity[char] == "RL":
                            # push the new operator to the stack
                            stack.append(char)
                            i += 1
                    elif precedence_order[char] > precedence_order[top_element]:
                        # push the char into stack
                        stack.append(char)
                        i += 1
                    elif precedence_order[char] < precedence_order[top_element]:
                        # pop the top element
                        popped_element = stack.pop()
                        postfix.append(popped_element)
            elif char == '(':
                # add it to the stack
                stack.append(char)
                i += 1
            elif char == ')':
                top_element = stack[-1]
                while top_element != '(':
                    popped_element = stack.pop()
                    postfix.append(popped_element)
                    # update the top element
                    top_element = stack[-1]
                # now we pop opening parenthases and discard it
                stack.pop()
                i += 1
            # char is operand
            else:
                postfix.append(char)
                i += 1
            #     print(postfix)
            # print(f"stack: {stack}")

        # empty the stack
        if len(stack) > 0:
            for i in range(len(stack)):
                postfix.append(stack.pop())
        # while len(stack) > 0:
        #     postfix.append(stack.pop())

        return postfix
    
    def main(self,infix_expression):
        infix_expression_list = list(infix_expression)

        postfix_expression_list = self.infix_to_postfix(infix_expression_list)
        # print(postfix_expression_list)
        self.insert(postfix_expression_list)
        if(self.root):
            # print(self.root.data)
            result = self.evaluate(self.root)
            print(result)