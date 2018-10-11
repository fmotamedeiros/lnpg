class Pilha:
    def __init__(self):
        self.pilha = []
        self.top = -1

    def push(self, data):
        self.pilha.append(data)
        self.top += 1

    def pop(self):
        temp = self.pilha[self.top]
        del self.pilha[self.top]
        self.top -= 1
        return temp

    def __str__(self):
        count = 0
        string = ""
        for item in self.pilha[::-1]:
            string += (str(item) + "  ")
            if count == 0:
                string += "TOP"
            string += "\n"
            count += 1
        return string


def readString(string):
    stack = Pilha()
    for c in string:
        decision = decide(c)
        if decide(c) == False:
            stack.push(int(c))
        else:
            b = stack.pop()
            a = stack.pop()
            val = decision(a, b)
            stack.push(val)
    return stack.pop()


def decide(char):
    def Mult(a, b):
        return a * b

    def Div(a, b):
        return a / b

    def Soma(a, b):
        return a + b

    def Sub(a, b):
        return a - b

    switcher = {
        "+": Soma,
        "-": Sub,
        "*": Mult,
        "/": Div
    }

    return switcher.get(char, False)

print(readString('10+'))
