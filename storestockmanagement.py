class Store:
    def __init__(self):
        self.fruit = {}
    
    def add_fruit(self):
        name = input("Enter the name :")
        stock = input("Enter the stock :")

        self.fruit[name] = int(stock)
        print(f"{name}:{stock} registed!")

    def display_fruit(self):
        print("current stock list:")
        for name,stock in self.fruit.items():
            print(f"{name}:{stock}")

store = Store()
while True:
    
    user_input = input("whould you liek to add?(1:continue 2:exit):")
    if user_input.lower() == "2":
        break
    
    store.add_fruit()
store.display_fruit()