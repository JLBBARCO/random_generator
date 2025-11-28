import customtkinter as ctk

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

        self.printArea = ctk.CTkFrame(self, width=350, height=150)
        self.printArea.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)

    def randomNumber(self):
        dialog = ctk.CTkInputDialog(title='Random Number', text='Input the quantity of numbers generated')
        value = dialog.get_input()

        from lib.random_numbers import randomNumbers

        if value is None:
            # user cancelled
            return

        try:
            qty = int(value)
        except (TypeError, ValueError):
            # show error in print area
            self.printArea.destroy()
            self.printArea = ctk.CTkFrame(self, width=350, height=150)
            self.printArea.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)
            err = ctk.CTkLabel(self.printArea, text='Entrada inválida: informe um número inteiro')
            err.grid(row=0, column=0, padx=padMain, pady=padMain)
            return

        if qty < 1:
            self.printArea.destroy()
            self.printArea = ctk.CTkFrame(self, width=350, height=150)
            self.printArea.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)
            err = ctk.CTkLabel(self.printArea, text='Quantidade deve ser >= 1')
            err.grid(row=0, column=0, padx=padMain, pady=padMain)
            return

        randomNumbers(qty)
        numbers = getattr(randomNumbers, 'numbers', [])

        self.printArea.destroy()
        self.printArea = ctk.CTkFrame(self, width=350, height=150)
        self.printArea.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)

        for c, n in numbers:
            item = ctk.CTkLabel(self.printArea, text=str(n))
            item.grid(row=c, column=0, padx=padMain, pady=padMain)

    def randomName(self):
        dialog = ctk.CTkInputDialog(title='Random Name', text='Input the quantity of names generated')
        value = dialog.get_input()

        from lib.random_names import randomNames

        if value is None:
            return

        try:
            qty = int(value)
        except (TypeError, ValueError):
            self.printArea.destroy()
            self.printArea = ctk.CTkFrame(self, width=350, height=150)
            self.printArea.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)
            err = ctk.CTkLabel(self.printArea, text='Entrada inválida: informe um número inteiro')
            err.grid(row=0, column=0, padx=padMain, pady=padMain)
            return

        if qty < 1:
            self.printArea.destroy()
            self.printArea = ctk.CTkFrame(self, width=350, height=150)
            self.printArea.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)
            err = ctk.CTkLabel(self.printArea, text='Quantidade deve ser >= 1')
            err.grid(row=0, column=0, padx=padMain, pady=padMain)
            return

        randomNames(qty)
        names = getattr(randomNames, 'names', [])

        self.printArea.destroy()
        self.printArea = ctk.CTkFrame(self, width=350, height=150)
        self.printArea.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)

        for c, n in names:
            item = ctk.CTkLabel(self.printArea, text=str(n))
            item.grid(row=c, column=0, padx=padMain, pady=padMain)


if __name__ == '__main__':
    app = App()
    app.mainloop()