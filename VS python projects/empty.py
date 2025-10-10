print("Welcome to ATM")

class ATM:
    """Simple ATM class with PIN verification and basic operations."""
    def __init__(self, pin, balance=0.0):
        # use single-underscore to avoid unnecessary name-mangling
        self._pin = int(pin)
        self._balance = float(balance)

    def verify_pin(self, pin):
        try:
            return int(pin) == self._pin
        except (ValueError, TypeError):
            return False

    def deposit(self, amount):
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            print("Enter a numeric amount to deposit.")
            return
        if amount <= 0:
            print("Enter a valid amount (> 0).")
            return
        self._balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self._balance:.2f}")

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            print("Enter a numeric amount to withdraw.")
            return
        if amount <= 0:
            print("Enter a valid amount (> 0).")
            return
        if amount > self._balance:
            print("Insufficient funds. Transaction cancelled.")
            return
        self._balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self._balance:.2f}")

    def get_balance(self):
        print(f"Your balance is {self._balance:.2f}")
        return self._balance


def main():
    # initial values (could be adapted to load from a file/db)
    starting_balance = 1000.0
    correct_pin = 1234
    atm = ATM(correct_pin, starting_balance)

    attempts = 0
    MAX_ATTEMPTS = 3

    while True:
        try:
            pas = input("Enter your PIN: ").strip()
        except (KeyboardInterrupt, EOFError):
            print('\nExiting.')
            break

        if not atm.verify_pin(pas):
            attempts += 1
            print("Incorrect PIN. Please try again.")
            if attempts >= MAX_ATTEMPTS:
                print("Too many incorrect attempts. Exiting.")
                break
            continue

        # reset attempts after successful login
        attempts = 0

        option = input("Choose option: 1) deposit  2) withdraw  3) check balance  4) quit\n:").strip()
        if option == '1':
            amount = input("Enter the amount you want to deposit: ").strip()
            atm.deposit(amount)
        elif option == '2':
            amount = input("Enter the amount you want to withdraw: ").strip()
            atm.withdraw(amount)
        elif option == '3':
            atm.get_balance()
        elif option == '4':
            print("Goodbye.")
            break
        else:
            print("Enter a valid option (1-4).")

        decide = input("Do you want to continue? (y/n): ").strip().lower()
        if decide in ('n', 'no'):
            print("Goodbye.")
            break
        # otherwise loop continues


if __name__ == '__main__':
    main()


