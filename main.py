import math
import PySimpleGUI as psg

class App:
    def __init__(self):
        psg.theme("reddit")
        self.displayed_value = ""
        self.memory = []
        self.value_input = psg.Input(self.displayed_value, key="-INPUT-", expand_x=True, expand_y=True, justification="right", disabled=True, font=("Arial", 20))
        mathfuncs = psg.Frame("", [
            [psg.Button("+", size=(2, 1), font=("Arial", 12, "bold"), key="-ADD-"), psg.Push(),
             psg.Button("-", size=(2, 1), font=("Arial", 12, "bold"), key="-SUB-"), psg.Push(),
             psg.Button("×", size=(2, 1), font=("Arial", 12, "bold"), key="-MULTI-"), psg.Push(),
             psg.Button("÷", size=(2, 1), font=("Arial", 12, "bold"), key="-DIV-")]
        ], border_width=0)
        exitfuncs = psg.Frame("", [
            [psg.Button("CLEAR", size=(6, 1), font=("Arial", 13, "bold"), key="-CLEAR-"),
             psg.Push(), psg.Button("=", size=(6, 1), font=("Arial", 13, "bold"), key="-EQUAL-")]
        ], border_width=0)
        figures = psg.Frame("", [
            [psg.Button("1", size=(2,1), font=("Arial", 12, "bold")), psg.Push(),
             psg.Button("2", size=(2,1), font=("Arial", 12, "bold")), psg.Push(),
             psg.Button("3", size=(2,1), font=("Arial", 12, "bold")), psg.Push(),
             psg.Button("4", size=(2,1), font=("Arial", 12, "bold"))],
            [psg.VPush()],
            [psg.Button("5", size=(2, 1), font=("Arial", 12, "bold")), psg.Push(),
             psg.Button("6", size=(2, 1), font=("Arial", 12, "bold")), psg.Push(),
             psg.Button("7", size=(2, 1), font=("Arial", 12, "bold")), psg.Push(),
             psg.Button("8", size=(2, 1), font=("Arial", 12, "bold"))],
            [psg.VPush()],
            [psg.Button("9", size=(2, 1), font=("Arial", 12, "bold")), psg.Push(),
             psg.Button("0", size=(2, 1), font=("Arial", 12, "bold")), psg.Push(),
             psg.Button("+/-", size=(3, 1), font=("Arial", 12, "bold"), key="-SIGNKEY-")]
        ], size=(200, 150), border_width=0)
        layout = [
            [self.value_input],
            [psg.VPush()],
            [psg.Push(), mathfuncs, psg.Push()],
            [psg.VPush()],
            [psg.Push(), figures, psg.Push()],
            [psg.VPush()],
            [psg.Push(), exitfuncs, psg.Push()]
        ]
        calc_window = psg.Window("Calculator", layout, titlebar_font=("Arial", 12), icon="calc.ico", size=(250, 400))

        while True:
            event, values = calc_window.read()
            match event:
                case psg.WIN_CLOSED:
                    break
                case "-ADD-":
                    if len(values["-INPUT-"]) != 0:
                        self.adding()
                case "-SUB-":
                    if len(values["-INPUT-"]) != 0:
                        self.subtracting()
                case "-MULTI-":
                    if len(values["-INPUT-"]) != 0:
                        self.multiplying()
                case "-DIV-":
                    if len(values["-INPUT-"]) != 0:
                        self.dividing()
                case "-SIGNKEY-":
                    if len(values["-INPUT-"]) != 0:
                        if self.displayed_value[0] == "-":
                            self.displayed_value = self.displayed_value[1:]
                        else:
                            self.displayed_value = f"-{self.displayed_value}"
                        self.value_input.update(self.displayed_value)
                case "-CLEAR-":
                    self.clearing()
                case "-EQUAL-":
                    if len(self.memory) != 0 and len(values["-INPUT-"]) != 0:
                        self.memory.append(float(self.displayed_value))
                        if str(self.memory[-1]) in "+-*/":
                            self.memory.pop(-1)
                        self.processing()


            if event.isnumeric():
                if event == "0":
                    self.displayed_value += event if len(values["-INPUT-"]) != 0 else ""
                else:
                    self.displayed_value += event
                self.value_input.update(self.displayed_value)

    def clearing(self):
        self.displayed_value = ""
        self.value_input.update(self.displayed_value)

    def adding(self):
        self.memory.append(float(self.displayed_value))
        self.memory.append("+")
        self.clearing()

    def subtracting(self):
        self.memory.append(float(self.displayed_value))
        self.memory.append("-")
        self.clearing()

    def multiplying(self):
        self.memory.append(float(self.displayed_value))
        self.memory.append("*")
        self.clearing()

    def dividing(self):
        self.memory.append(float(self.displayed_value))
        self.memory.append("/")
        self.clearing()

    def processing(self):
        pmemory = self.memory
        pvalue = pmemory[0]
        pmemory.pop(0)
        while len(pmemory) > 0:
            if pmemory[0] == "+":
                pvalue += pmemory[1]
            elif pmemory[0] == "-":
                pvalue -= pmemory[1]
            elif pmemory[0] == "*":
                pvalue *= pmemory[1]
            else:
                pvalue /= pmemory[1]
            pmemory.pop(0)
            pmemory.pop(0)
        self.memory = []
        self.displayed_value = str(pvalue)
        self.value_input(pvalue)



App()
