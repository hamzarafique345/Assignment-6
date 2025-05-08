# Assignment 4:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name)
#  that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "Old Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example
b1 = Bank()
b2 = Bank()
print(Bank.bank_name)
Bank.change_bank_name("New Bank")
print(b1.bank_name)
print(b2.bank_name)