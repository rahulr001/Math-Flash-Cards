from tkinter import *
from PIL import Image, ImageTk
from conditions import conditionCheck, levels, SubconditionCheck, MulconditionCheck


class FirstPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("home.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Label(self, text="MENU", height=2, fg="white", font="bold 14", width=10, bg='#974d27').place(x=451,
                                                                                                     y=308)

        Button(self, text="START", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(SecondPage)
               ).place(x=455,
                       y=395)
        Button(self, text="EXIT", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda :self.exit()
               ).place(x=455, y=483)

    def exit(self):
        import sys
        sys.exit()


class SecondPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("mode.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        Button(self, text="Addition", borderwidth=0, height=1, fg="white", font="bold 14", width=11, bg='#974d27',
               command=lambda: controller.show_frame(AdditionPage)).place(x=451,
                                                                          y=284)

        Button(self, text="Subtraction", borderwidth=0, height=1, fg="white", font="bold 14", width=11, bg='#974d27',
               command=lambda: controller.show_frame(SubstractionPage)

               ).place(x=450,
                       y=374)
        Button(self, text="Multiplication", borderwidth=0, height=1, fg="white", font="bold 14", width=11, bg='#974d27',
               command=lambda: controller.show_frame(MultiplicationPage)

               ).place(x=455, y=458)
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(FirstPage)).place(x=10, y=10)


class SubstractionPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Levels.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        Button(self, text="Level 1", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(SubstractionLevel1)).place(
            x=450, y=232)
        Button(self, text="Level 2", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(SubstractionLevel2)).place(
            x=451, y=320)
        Button(self, text="Level 3", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(SubstractionLevel3)).place(
            x=455, y=413)
        Button(self, text="Level 4", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(SubstractionLevel4)).place(
            x=455, y=500)
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(SecondPage)).place(x=10, y=10)


class SubstractionLevel1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Subtraction.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level1(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(SubstractionPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: SubconditionCheck.condition1(self, self.val1, self.val2, self.correct, self.wrong,
                                                            self.attempts)).place(x=270, y=590)


class SubstractionLevel2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Subtraction.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level1(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(SubstractionPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: SubconditionCheck.condition2(self, self.val1, self.val2, self.correct, self.wrong,
                                                            self.attempts)).place(x=270, y=590)


class SubstractionLevel3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Subtraction.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level1(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(SubstractionPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: SubconditionCheck.condition3(self, self.val1, self.val2, self.correct, self.wrong,
                                                            self.attempts)).place(x=270, y=590)


class SubstractionLevel4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Subtraction.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level1(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(SubstractionPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: SubconditionCheck.condition4(self, self.val1, self.val2, self.correct, self.wrong,
                                                            self.attempts)).place(x=270, y=590)


class AdditionPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Levels.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        Button(self, text="Level 1", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(AdditionLevel1)).place(
            x=450, y=232)
        Button(self, text="Level 2", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(AdditionLevel2)).place(
            x=451, y=320)
        Button(self, text="Level 3", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(AdditionLevel3)).place(
            x=455, y=413)
        Button(self, text="Level 4", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(AdditionLevel4)).place(
            x=455, y=500)
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(SecondPage)).place(x=10, y=10)


class AdditionLevel1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Addition.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level1(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(AdditionPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: conditionCheck.condition1(self, self.val1, self.val2, self.correct, self.wrong,
                                                         self.attempts)).place(x=270, y=590)


class AdditionLevel2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Addition.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level2(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(AdditionPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: conditionCheck.condition2(self, self.val1, self.val2, self.correct, self.wrong,
                                                         self.attempts)).place(x=270, y=590)


class AdditionLevel3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Addition.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level3(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(AdditionPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: conditionCheck.condition3(self, self.val1, self.val2, self.correct, self.wrong,
                                                         self.attempts)).place(x=270, y=590)


class AdditionLevel4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Addition.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()
        self.val1, self.val2 = levels.level4(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(AdditionPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: conditionCheck.condition4(self, self.val1, self.val2, self.correct, self.wrong,
                                                         self.attempts)).place(x=270, y=590)


class MultiplicationPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Levels.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        Button(self, text="Level 1", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(MultiplicationLevel1)
               ).place(
            x=450, y=232)
        Button(self, text="Level 2", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(MultiplicationLevel2)).place(
            x=451, y=320)
        Button(self, text="Level 3", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(MultiplicationLevel3)).place(
            x=455, y=413)
        Button(self, text="Level 4", borderwidth=0, height=1, fg="white", font="bold 14", width=9, bg='#974d27',
               command=lambda: controller.show_frame(MultiplicationLevel4)).place(
            x=455, y=500)
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(SecondPage)).place(x=10, y=10)


class MultiplicationLevel1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Multiplication.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level1(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(MultiplicationPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: MulconditionCheck.condition1(self, self.val1, self.val2, self.correct, self.wrong,
                                                            self.attempts)).place(x=270, y=590)


class MultiplicationLevel2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Multiplication.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level1(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(MultiplicationPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: MulconditionCheck.condition2(self, self.val1, self.val2, self.correct, self.wrong,
                                                            self.attempts)).place(x=270, y=590)


class MultiplicationLevel3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Multiplication.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level1(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(MultiplicationPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: MulconditionCheck.condition3(self, self.val1, self.val2, self.correct, self.wrong,
                                                            self.attempts)).place(x=270, y=590)


class MultiplicationLevel4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        load = Image.open("Multiplication.jpg")
        photo = ImageTk.PhotoImage(load)
        label = Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)
        global val3
        self.val3 = StringVar()

        self.val1, self.val2 = levels.level1(self)
        self.correct = 0
        self.wrong = 0
        self.attempts = 0
        Button(self, text="Back", borderwidth=0, font="bold 14", height=2, width=10, bg='#974d27', fg="white",
               command=lambda: controller.show_frame(MultiplicationPage)).place(x=10, y=10)
        self.value1 = Label(self, text=self.val1, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value1.place(x=140, y=375)
        self.value2 = Label(self, text=self.val2, height=1, bg="#b39163", font="bold 44", width=2, )
        self.value2.place(x=478, y=383)
        self.value = Entry(self, textvariable=self.val3, bg="#c68d25", fg="white", font="bold 44", width=2, )
        self.value.place(x=820, y=380)
        self.correctAns = Label(self, text=self.correct, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.correctAns.place(x=920, y=585)
        self.wrongAns = Label(self, text=self.wrong, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.wrongAns.place(x=920, y=649)
        self.Attempts = Label(self, text=self.attempts, height=1, fg="white", bg="#7f3f01", font="bold 14", width=5, )
        self.Attempts.place(x=935, y=720)
        Button(self, text="CHECK", borderwidth=0, height=1, font="bold 24", width=7, bg='#dda477',
               command=lambda: MulconditionCheck.condition4(self, self.val1, self.val2, self.correct, self.wrong,
                                                            self.attempts)).place(x=270, y=590)


class Application(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        window = Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=768)
        window.grid_columnconfigure(0, minsize=1024)

        self.frames = {}
        for F in (
                FirstPage, SecondPage, AdditionPage, MultiplicationPage, SubstractionPage, AdditionLevel1,
                AdditionLevel2,
                AdditionLevel3, AdditionLevel4, MultiplicationLevel1, MultiplicationLevel2, MultiplicationLevel3,
                MultiplicationLevel4, SubstractionLevel2, SubstractionLevel3, SubstractionLevel4, SubstractionLevel1
        ):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Math Flash Card")


if __name__ == "__main__":
    app = Application()
    app.maxsize(1024, 768)
    app.mainloop()
