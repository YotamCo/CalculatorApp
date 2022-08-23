
class Calculator:
    def add(self, num1, num2):
        return num1 + num2
        
    def substract(self, num1, num2):
        return num1 - num2

    def multipy(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def calculate(self, num1, num2, operator):
        if(operator == 'add'):
            return self.add(num1, num2)
        elif(operator == 'substract'): 
            return self.substract(num1, num2)
        elif(operator == 'multiply'):
            return self.multipy(num1, num2)
        elif(operator == 'divide'):
            return self.divide(num1, num2)