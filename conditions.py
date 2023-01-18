from tkinter import messagebox
import random


class conditionCheck:
    def __init__(self, val1, val2, correct, wrong, attempts):
        self.val1 = val1
        self.val2 = val2
        self.correct = correct
        self.wrong = wrong
        self.attempts = attempts

    def condition1(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 + val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level1(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")

    def condition2(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 + val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level2(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")

    def condition3(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 + val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level3(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")

    def condition4(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 + val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level4(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")


class SubconditionCheck:
    def __init__(self, val1, val2, correct, wrong, attempts):
        self.val1 = val1
        self.val2 = val2
        self.correct = correct
        self.wrong = wrong
        self.attempts = attempts

    def condition1(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 - val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level1(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")

    def condition2(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 - val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level2(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")

    def condition3(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 - val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level3(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")

    def condition4(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 - val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level4(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")


class MulconditionCheck:
    def __init__(self, val1, val2, correct, wrong, attempts):
        self.val1 = val1
        self.val2 = val2
        self.correct = correct
        self.wrong = wrong
        self.attempts = attempts

    def condition1(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 * val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level1(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")

    def condition2(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 * val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level2(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")

    def condition3(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 * val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level3(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")

    def condition4(self, val1, val2, correct, wrong, attempts):

        try:
            self.val3 = int(self.value.get())
            if val1 * val2 == self.val3:
                messagebox.showinfo("Result", "Congrats Correct Answer")
                self.correct += 1
                self.attempts += 1
                val1, val2 = levels.level4(self)
                self.value1['text'] = val1
                self.value2['text'] = val2
                self.correctAns['text'] = self.correct
                self.Attempts['text'] = self.attempts
                print(self.correct)

            else:
                messagebox.showinfo("Result", "Oops Try again")
                self.wrong += 1
                self.attempts += 1
                self.wrongAns['text'] = self.wrong
                self.Attempts['text'] = self.attempts

        except:
            messagebox.showinfo("Alert", "Please Enter a valid Answer")


class levels:
    def __init__(self, val1, val2, correct, wrong):
        self.val1 = val1
        self.val2 = val2
        self.correct = correct
        self.wrong = wrong

    def level1(self):
        self.val1 = random.randrange(1, 4)
        self.val2 = random.randrange(1, 4)
        return self.val1, self.val2

    def level2(self):
        self.val1 = random.randrange(1, 7)
        self.val2 = random.randrange(1, 7)
        return self.val1, self.val2

    def level3(self):
        self.val1 = random.randrange(1, 10)
        self.val2 = random.randrange(1, 10)
        return self.val1, self.val2

    def level4(self):
        self.val1 = random.randrange(1, 13)
        self.val2 = random.randrange(1, 13)
        return self.val1, self.val2
