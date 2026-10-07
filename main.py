class CoffeeMachine:
    def __init__(self):
        self.water: int = 400
        self.milk: int = 540
        self.beans: int = 120
        self.cups: int = 9
        self.money: int = 550

    def process_input(self, action: str):
        if action in ("buy", "fill", "take", "remaining", "exit"):
            return self._handle_main(action)
        else:
            print("Invalid action")
            return None

    def _handle_main(self, action: str):
        if action == "buy":
            self._handle_buy()
            return None
        elif action == "fill":
            self._handle_fill_water()
            self._handle_fill_milk()
            self._handle_fill_beans()
            self._handle_fill_cups()
            return None
        elif action == "take":
            self._take_money_out()
            return None
        elif action == "remaining":
            self._status()
            return None
        elif action == "exit":
             return "exit"
        else:
            return None

    def _handle_buy(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        cafe_option = input()

        if cafe_option == "1":
            is_available = self._check_resources(250, 0, 16)
            if is_available:
                self._update_resources(4, 16, 250)
        elif cafe_option == "2":
            is_available = self._check_resources(350, 75, 20)
            if is_available:
                self._update_resources(7, 20, 350, 75)
        elif cafe_option == "3":
            is_available = self._check_resources(200, 100, 12)
            if is_available:
                self._update_resources(6, 12, 200, 100)
        elif cafe_option == "back":
            pass
        else:
            print("Invalid item")

    def _handle_fill_water(self):
        print()
        print("Write how many ml of water you want to add:")
        g_water = int(input())
        self.water += g_water

    def _handle_fill_milk(self):
        print("Write how many ml of milk you want to add:")
        g_milk = int(input())
        self.milk += g_milk

    def _handle_fill_beans(self):
        print("Write how many grams of coffee beans you want to add:")
        g_coffee = int(input())
        self.beans += g_coffee

    def _handle_fill_cups(self):
        print("Write how many disposable cups you want to add:")
        g_cups = int(input())
        self.cups += g_cups

    def _check_resources(self, g_water: int, g_milk: int, g_coffee: int, g_cups: int = 1):
        if g_milk != 0:
            max_cups = min(
                self.water // g_water,
                self.milk // g_milk,
                self.beans // g_coffee,
                self.cups // g_cups
            )
        else:
            max_cups = min(
                self.water // g_water,
                self.beans // g_coffee,
                self.cups // g_cups
            )

        if max_cups >= 1:
            print("I have enough resources, making you a coffee!")
            return True

        else:
            if self.water // g_water == 0:
                print("Sorry, not enough water!")
            if g_milk != 0 and self.milk // g_milk == 0:
                print("Sorry, not enough milk!")
            if self.beans // g_coffee == 0:
                print("Sorry, not enough coffee beans!")
            if self.cups // g_cups == 0:
                print("Sorry, not enough cups!")
            return False

    def _update_resources(self, g_money = None, g_coffee = None, g_water = None, g_milk = None):
        if g_money is not None:
            self.money += g_money
        if g_coffee is not None:
            self.beans -= g_coffee
        if g_water is not None:
            self.water -= g_water
        if g_milk is not None:
            self.milk -= g_milk

        self.cups -= 1

    def _take_money_out(self):
        print()
        print("I gave you $" + str(self.money))
        self.money = 0

    def _status(self):
        print()
        print("The coffee machine has:")
        print(str(self.water) + " ml of water")
        print(str(self.milk) + " ml of milk")
        print(str(self.beans) + " g of coffee beans")
        print(str(self.cups) + " disposable cups")
        print("$" + str(self.money) + " of money")


def io_input():
    print()
    print("Write action (buy, fill, take, remaining, exit):")
    return input()


def coffee_machine():
    is_running = True
    coffee_machine_instance = CoffeeMachine()

    while is_running:
        action = io_input()
        action = coffee_machine_instance.process_input(action)

        if action == "exit":
            break

if __name__ == '__main__':
    coffee_machine()