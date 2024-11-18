class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12:
            return 50
        elif 13 <= age <= 20:
            return 100
        elif 21 <= age <= 60:
            return 150
        elif age > 60:
            return 100
        else:
            return ("invalid")
age = int(input("Please enter your age: "))
zoo = Zoo()
ticket_price = zoo.get_ticket_price(age)
print(f"Ticket price: {ticket_price}")