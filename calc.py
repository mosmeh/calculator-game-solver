from itertools import product

class Operation:
    def __init__(self):
        pass

    def apply(self, n):
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()

class Append(Operation):
    def __init__(self, n):
        self.n = n
    
    def apply(self, n):
        return n * 10 + (1 if n >= 0 else -1) * self.n

    def __str__(self):
        return str(self.n)

class Add(Operation):
    def __init__(self, n):
        self.n = n
    
    def apply(self, n):
        return n + self.n

    def __str__(self):
        return '{}{}'.format('+' if self.n > 0 else '', self.n)

class Multiply(Operation):
    def __init__(self, n):
        self.n = n
    
    def apply(self, n):
        return self.n * n
    
    def __str__(self):
        return 'x{}'.format(self.n)

class Divide(Operation):
    def __init__(self, n):
        self.n = n

    def apply(self, n):
        return n / self.n
    
    def __str__(self):
        return '/{}'.format(self.n)

class Replace(Operation):
    def __init__(self, before, after):
        self.before = str(before)
        self.after = str(after)
    
    def apply(self, n):
        return float(str(n).replace(self.before, self.after))
    
    def __str__(self):
        return '{}=>{}'.format(self.before, self.after)

class Power(Operation):
    def __init__(self, power):
        self.power = power

    def apply(self, n):
        return n ** self.power 
    
    def __str__(self):
        return 'x^{}'.format(self.power)

class Reverse(Operation):
    @staticmethod
    def apply(n):
        return (1 if n > 0 else -1) * int(reversed(str(abs(n))))
    
    @staticmethod
    def __str__():
        return 'Reverse'

class Negate(Operation):
    @staticmethod
    def apply(n):
        return -n
    
    @staticmethod
    def __str__():
        return '+/-'

class Sum(Operation):
    @staticmethod
    def apply(n):
        s = 0
        while n > 0:
            s += n % 10
            n = int(n / 10)
        return s
    
    @staticmethod
    def __str__():
        return 'SUM'

class Backspace(Operation):
    @staticmethod
    def apply(n):
        return int(n / 10)
    
    @staticmethod
    def __str__():
        return '<<'

def solve(moves, init, goal, num_moves):
    for pattern in product(moves, repeat=num_moves):
        n = init
        for move in pattern:
            n = move.apply(n)
        if n == goal:
            return pattern
