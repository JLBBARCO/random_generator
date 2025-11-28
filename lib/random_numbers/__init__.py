import customtkinter as ctk
import random

padMain = 10
# Module-level storage so callers can read `randomNumbers.numbers` after calling
numbers = []

def randomNumbers(quantity, min_num=0, max_num=100):
    """Generate `quantity` random integers between min_num and max_num.
    The generated list is stored on the function object as `randomNumbers.numbers`
    and also in the module-level `numbers` variable to keep backward compatibility.
    """
    global numbers
    try:
        qty = int(quantity)
    except (TypeError, ValueError):
        qty = 0

    if qty < 1:
        numbers = []
        randomNumbers.numbers = numbers
        return

    # ensure min < max
    try:
        min_v = int(min_num)
        max_v = int(max_num)
    except (TypeError, ValueError):
        min_v = 0
        max_v = 100

    if min_v > max_v:
        min_v, max_v = max_v, min_v

    gen = []
    for i in range(qty):
        gen.append((i, random.randint(min_v, max_v)))

    numbers = gen
    randomNumbers.numbers = numbers
    return

class randomNumbers(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('Random Numbers')
        self.resizable(False, False)
        self.geometry('400x350')

        self.quantityNumbers = None
        self.minNumber = None
        self.maxNumber = None

        # Create main frame
        self.main_frame = ctk.CTkFrame(self, width=380, height=330)
        self.main_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Title
        self.titleLabel = ctk.CTkLabel(self.main_frame, text='Random Numbers', font=('Arial', 14, 'bold'))
        self.titleLabel.pack(padx=padMain, pady=padMain)

        self.inputQuantity = ctk.CTkEntry(self.main_frame, placeholder_text='Quantity of Numbers')
        self.inputQuantity.pack(padx=padMain, pady=padMain)
        self.inputMinNumbers = ctk.CTkEntry(self.main_frame, placeholder_text='Min of Numbers')
        self.inputMinNumbers.pack(padx=padMain, pady=padMain)
        self.inputMaxNumbers = ctk.CTkEntry(self.main_frame, placeholder_text='Max of Numbers')
        self.inputMaxNumbers.pack(padx=padMain, pady=padMain)

        # Frame for buttons
        button_frame = ctk.CTkFrame(self.main_frame)
        button_frame.pack(padx=padMain, pady=20)

        self.submitButton = ctk.CTkButton(button_frame, text='Submit', command=self.submit, width=100)
        self.submitButton.pack(side='left', padx=5)

        self.cancelButton = ctk.CTkButton(button_frame, text='Cancel', command=self.destroy, width=100)
        self.cancelButton.pack(side='left', padx=5)

        numbers = list()
        if self.quantityNumbers < 1:
            pass
        elif self.minNumber < self.maxNumber:
            pass
        else:
            for c in range(self.quantityNumbers):
                value = random.randint(self.minNumber, self.maxNumber)
                if value not in numbers:
                    numbers.append(value)

    def submit(self):
        if hasattr(self, 'addressEntry'):
            self.address = self.addressEntry.get()
        if hasattr(self, 'userEntry'):
            self.user = self.userEntry.get()
        if hasattr(self, 'passwordEntry'):
            self.password = self.passwordEntry.get()
        elif self.generated_password:
            self.password = self.generated_password
        if hasattr(self, 'charactersEntry'):
            self.characters = self.charactersEntry.get()
        self.destroy()