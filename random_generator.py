import customtkinter as ctk
from lib import random_names, random_numbers

padMain = 10
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Random Generator')
        self.geometry('420x220')

        self.main_frame = ctk.CTkFrame(self, width=350, height=150)
        self.main_frame.grid(row=0, column=0, padx=padMain, pady=padMain)

        self.textTitle = ctk.CTkLabel(self.main_frame, text='Random Generator')
        self.textTitle.grid(row=0, column=0, columnspan=3, padx=padMain, pady=padMain)

        self.buttonNumber = ctk.CTkButton(self.main_frame, text='Random Number', command=self.randomNumber)
        self.buttonNumber.grid(row=1, column=0, padx=padMain, pady=padMain)

        self.buttonName = ctk.CTkButton(self.main_frame, text='Random Name', command=self.randomName)
        self.buttonName.grid(row=1, column=2, padx=padMain, pady=padMain)

        self.printArea = ctk.CTkLabel(self, width=350, height=150)

    def randomNumber(self):
        dialog = ctk.CTkInputDialog(title='Random Number', text='Input the quantity of numbers generated')
        value = dialog.get_input()

        random_numbers.randomNumbers(value)
        names = random_names.randomNames.names

        self.printArea.destroy()
        self.printArea = ctk.CTkFrame(self, width=350, height=150)
        self.printArea.grid(row=1, column=0, padx=padMain, pady=padMain)

        for c, n in names:
            self.printItem = ctk.CTkLabel(self.printArea, text=n)
            self.printItem.grid(row=c, column=0, padx=padMain, pady=padMain)

    def randomName(self):
        dialog = ctk.CTkInputDialog(title='Random Name', text='Input the quantity of names generated')
        value = dialog.get_input()

        random_names.randomNames(value)
        names = random_names.randomNames.names

        self.printArea.destroy()
        self.printArea = ctk.CTkFrame(self, width=350, height=150)
        self.printArea.grid(row=1, column=0, padx=padMain, pady=padMain)

        for c, n in names:
            self.printItem = ctk.CTkLabel(self.printArea, text=n)
            self.printItem.grid(row=c, column=0, padx=padMain, pady=padMain)


if __name__ == '__main__':
    app = App()
    app.mainloop()