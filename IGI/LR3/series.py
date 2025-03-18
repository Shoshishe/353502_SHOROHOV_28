import math
MAX_ITERATION_COUNT = 500


def series() -> float:
    """
    Function for counting taylor series expansion of ln(1+x) and outputing the result in a table view
     Parameters
      x :  float (from stdin)   
           Substitution of x in ln(1+x)
      eps: float (from stdin)
           The required precision for counting a value of ln(1+x)
     Returns: -
     Exceptions
      ValueError 
        If the absolute value of x is more or equal to 1
      TimeoutError
        If function takes more iterations takes more than max interation count 
    """
    def task_1_input() -> tuple[float, float]:
        x = ''
        while x is not float:
            try:
                x = float(input('Enter an x (from -1 to 1): '))
                if (abs(x) > 1):
                    raise ValueError
                break
            except ValueError:
                print('Please enter a valid x value: ')
        eps = ''
        while eps is not float:
            try:
                eps = float(input('Enter an epsilon (> 0): '))
                if (eps <= 0):
                    raise ValueError
                break
            except ValueError:
                print('Please enter a valid epsilon: ')    
        return (x, eps)    

    def pow(a: int, n: int) -> int:
        """
        Function for taking variable a to the power of n, where n is an integer
         Params:
         ----
         a (int)  - The value to take power of
         n (int)  - The power to take the value to
         ----
         Returns: a^n
        """
        result = 1
        while (n != 0):
            if (n % 2 == 1):
                result *= a
            a = a * a
            n //= 2
        return result  
    input_tuple = task_1_input()
    x = input_tuple[0]
    eps = input_tuple[1]
    if abs(x) >= 1:
        raise(ValueError)
    result, i, diff = 0, 1, eps + 1
    while (abs(diff) > eps):
        diff = pow(-1, i - 1) * pow(x, i) / i
        result += diff
        if i > MAX_ITERATION_COUNT:
            raise(TimeoutError)
        i += 1
    true_value = math.log1p(x)
    n = str(i).center(3)
    print("╔════╦═══╦══════╦══════════╦═════╗"
        "\n║ x  ║ n ║ F(x) ║ Math F(x)║ eps ║\n"
          "╠════╬═══╬══════╬══════════╬═════╣\n"
         f"║{x:+,.1f}║{n}║{result:+,.3f}║{true_value:+,.7f}║{eps:.3f}║\n"
          "╚════╩═══╩══════╩══════════╩═════╝")
