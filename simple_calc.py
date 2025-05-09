import re

class Calculator:
    def __init__(self, expression):
        self.expression = expression
        #setting up placeholders for split expression
        self. a = None
        self.b = None
        self.op = None

    def clean(self):
        match = re.match(r"\s*(\d+(?:\.\d+)?)\s*([\+\-\*/])\s*(\d+(?:\/\d+)?)\s*", self.expression)

        if match:
            a, op, b = match.groups()
            

            self.a = float(a) if "." in a else int(a)
            self.b = float(b) if "." in b else int(b)
            self.op = op
            return "Parsing complete!"
        else:
            return "Invalid expression!"
        
    def evaluate(self):
        if self.op == "+":
            return self.a + self.b
        if self.op == "-":
            return self.a - self.b
        if self.op == "*":
            return self.a * self.b
        if self.op == "/":
            return self.a / self.b


def lines():
    print("-"*50)

if __name__ == "__main__":

    while True:
        lines()
        print("ENTER A STRING EXPRESSION ('1 + 1`)\nI GIVE YOU THE RESULT!")

        try:

            user_input = input("enter a string or a float: ")

            if not user_input:
                print("try again")
                continue

            if user_input == "q":
                print("bye bye !")
                break

            calc = Calculator(user_input)
            if calc.clean():
                print(f"RESULT: {calc.evaluate()}")
            else:
                print("Invalid expression")

        
        except ValueError:
            print("Error: Int or Float only!")
            continue
        except ZeroDivisionError:
            print("Error: can't divide by zero!")
        except EOFError:
            print("Error: no input entered")
            continue
        except KeyboardInterrupt:
            print("Goodbye!")
            break





            
    
        