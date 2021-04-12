class Budget:
    def __init__(self, food = 0, clothing = 0, entertainment = 0):
        self.foodBudget = food
        self.clothingBudget = clothing
        self.entertainment = entertainment

    def deposit(self):
        depositCategory = int(input("Press 1 for Food, 2 for Clothing or 3 for Entertainment \n"))
        depositValue = int(input("How much do you want to deposit? \n"))
        if depositCategory == 1:
            self.foodBudget += depositValue
            print(f"{depositValue} has been deposited into your food budget")
        elif depositCategory == 2:
            self.clothingBudget += depositValue
            print(f"{depositValue} has been deposited into your clothing budget")
        elif depositCategory == 3:
            self.entertainment += depositValue
            print(f"{depositValue} has been deposited into your entertainment budget")
        else:
            print("Please enter a valid answer")

    
    def withdrawal(self):
        withdrawalCategory = int(input("Press 1 for Food, 2 for Clothing or 3 for Entertainment \n"))
        withdrawalValue = int(input("How much do you want to withdraw? \n"))
        if withdrawalCategory == 1:
            self.foodBudget -= withdrawalValue
            print(f"{withdrawalValue} has been withdrawn from your food budget")
        elif withdrawalCategory == 2:
            self.clothingBudget -= withdrawalValue
            print(f"{withdrawalValue} has been withdrawn from your clothing budget")
        elif withdrawalCategory == 3:
            self.entertainment -= withdrawalValue
            print(f"{withdrawalValue} has been withdrawn from your entertainment budget")
        else:
            print("Please enter a valid answer")

        return withdrawalValue
    
    def transfer(self):
        transferAmount = int(self.withdrawal())
        transferCategory = int(input("Where will you like to transfer to? Press 1 for Food, 2 for Clothing or 3 for Entertainment \n"))
        if transferCategory == 1:
            self.foodBudget += transferAmount
            print(f"{transferAmount} has been transfered into your food budget")
        elif transferCategory == 2:
            self.clothingBudget += transferAmount
            print(f"{transferAmount} has been transfered into your clothing budget")
        elif transferCategory == 3:
            self.entertainment += transferAmount
            print(f"{transferAmount} has been transfered into your entertainment budget")
        else:
            print("Please enter a valid answer")


    def balance(self):
        print(f"Current food budget is {self.foodBudget}, current  clothing budget is {self.clothingBudget} and current entertainment budget is {self.entertainment}")


myBudget = Budget()
#myBudget.deposit()
#myBudget.withdrawal()
#myBudget.transfer()
myBudget.balance()
