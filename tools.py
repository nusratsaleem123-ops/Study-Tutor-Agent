from crewai.tools import tool
from datetime import datetime
import ast
import operator


@tool("Calculator")
def calculator(expression: str) -> str:
    """
    Safely calculate basic mathematical expressions.

    Use this tool when the student asks for a mathematical
    calculation or when accurate arithmetic is required.
    """

    try:
        allowed_operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
            ast.USub: operator.neg,
        }

        def evaluate(node):
            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value
                raise ValueError("Only numbers are allowed.")

            if isinstance(node, ast.BinOp):
                left = evaluate(node.left)
                right = evaluate(node.right)
                operation = allowed_operators.get(type(node.op))

                if operation is None:
                    raise ValueError("Operator not supported.")

                return operation(left, right)

            if isinstance(node, ast.UnaryOp):
                value = evaluate(node.operand)
                operation = allowed_operators.get(type(node.op))

                if operation is None:
                    raise ValueError("Operator not supported.")

                return operation(value)

            raise ValueError("Invalid mathematical expression.")

        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree.body)

        return f"Calculation result: {result}"

    except Exception as e:
        return f"Calculator error: {str(e)}"


@tool("Current Date and Time")
def current_datetime() -> str:
    """
    Returns the current date and time.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
