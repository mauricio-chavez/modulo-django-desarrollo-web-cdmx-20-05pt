class Calculator:
    def add(self, a, b):
        """Adds two numbers"""
        return a + b

    def minus(self, a, b):
        """Minus two numbers"""
        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers"""
        result = 0

        for number in range(b):
            result = self.add(a, result)
        return result
