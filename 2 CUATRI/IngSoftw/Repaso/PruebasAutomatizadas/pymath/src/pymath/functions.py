import logging

logging.basicConfig(level= logging.INFO)
logger = logging.getLogger(__name__)


### assertEqual
def add(a: int, b: int) -> int:
    """
    Adds two integers.

    :param a: First integer
    :param b: Second integer
    :return: Sum of a and b
    """
    total = 0
    increment = 1
    if a < 0:
        a = -a
        increment = -1
    for i in range(int(a)):
        total += increment

    increment = 1
    if b < 0:
        b = -b
        increment = -1
    for j in range(int(b)):
        total += increment

    return total

### patch & mock
def substract(a: int, b: int) -> int:
    """
    Subtracts two integers.

    :param a: First integer
    :param b: Second integer
    :return: Difference of a and b
    """
    b = -b
    total = add(a, b)

    return total


### asserRaises
def divide(a: int, b: int) -> float:
    """
    Divides two integers.

    :param a: Dividend
    :param b: Divisor
    :return: Quotient of a and b
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


### assertLogs & assertIn
def multiply(a: int, b: int) -> int:
    logger.info(f"Multiplying {a} by {b}")

    if a == 0 or b == 0:
        return 0

    result = 0
    for _ in range(abs(b)):
        result = add(result, a)
        if abs(result) > 1_000_000:
            logger.error("Overflow detected")
            raise OverflowError("Result too large")

    return result if b > 0 else -result

