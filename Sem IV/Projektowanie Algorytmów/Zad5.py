class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape) + ['_']  #pusty znak na koncu tasmy (akceptuje wejscie gdy dojdzie do konca tasmy)
        self.head = 0  #pozycja głowicy
        self.state = "q0"  #stan początkowy
        self.accepted = False

    def move_head(self, direction):
        if direction == 'R':
            self.head += 1
        elif direction == 'L' and self.head > 0:
            self.head -= 1

    def run(self):
        while True:
            symbol = self.tape[self.head]

            if self.state == "q0":
                if symbol == "[":
                    self.state = "q1"
                    self.move_head('R')
                else:
                    self.state = "q_reject"

            elif self.state == "q1":
                if symbol.isdigit():
                    self.move_head('R')
                elif symbol == ",":
                    self.state = "q3"
                    self.move_head('R')
                elif symbol == "]":
                    self.state = "q4"
                    self.move_head('R')
                else:
                    self.state = "q_reject"

            elif self.state == "q3":
                if symbol.isdigit():
                    self.state = "q1"
                    self.move_head('R')
                else:
                    self.state = "q_reject"

            elif self.state == "q4":
                if symbol == "_":  # Koniec taśmy, akceptacja
                    self.accepted = True
                    break
                else:
                    self.state = "q_reject"

            elif self.state == "q_reject":
                break

        return self.accepted


#testy
test_cases = [
    "[0107,999422,3]",
    "[0107 999422,3]",
    "[0107,999a22,3]"
]

for case in test_cases:
    tm = TuringMachine(case)
    result = "AKCEPTACJA" if tm.run() else "ODRZUCENIE"
    print(f"Wejście: {case} --> {result}")