# Encapsulation in Personal Budget Management

# Task 1: Define Budget Category Class 

# Creating a class BudgetCategory with private attributes for category name and allocated budget.
class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.__name = name
        self.__allocated_budget = allocated_budget
        self.__expenses = 0

# Task 2:  Implement Getters and Setters

    def get_name(self):
        return self.__name

    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_name(self, name):
        self.__name = name

    def set_allocated_budget(self, budget):
        if budget > 0:
            self.__allocated_budget = budget
        else:
         raise ValueError("Budget should be a positive number")
    
# Task 3

    def add_expenses(self, expense): # method to add expenses to a category and adjust the budget accordingly
        if not isinstance(expense, (int, float)) or expense < 0:
            raise ValueError("Expense must be a positive number.")
        if expense > self.__allocated_budget - self.__expenses:
            raise ValueError("Expense exceeds remaining budget.")
        self.__expenses += expense

# Task 4

    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expenses
        print(f"Category Name: {self.__name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Expenses: {self.__expenses}")
        print(f"Remaining Budget: {remaining_budget}")

food_category = BudgetCategory("Food", 50) # Name of category and allocated budget
print(food_category.add_expenses(0.75)) # How much expenses
food_category.display_category_summary()

# E-commerce Product Catalog System

# Task 1: Create Base Product Class

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

def display_product_info(self):
    print(f"Product ID: {self.product_id}\n Name: {self.name} \n Price: {self.price}")

# Task 2 and Task 3


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_product_info(self):
        print(f"\nThe author of the book is {self.author}")
    
class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_product_info(self):
        print(f"\nA spec of the electronic is {self.specs}")
    
class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size
    
    def display_product_info(self):
       print(f"\nThe size of the clothing is {self.size}")
    
# Task 4

# Instantiating a Book class object
book1 = Book("b1", "Life Span", "28.00", "David A. SinClaire")


# Instantiating a Electronic class object
electronic1 = Electronic("e1", "flipper", "206.00", "165 Hertz")


# Instantiating a Clothing class object
clothing1 = Clothing("c1", "Socks", "28.88", "Large")


print(book1.display_product_info())
print(electronic1.display_product_info())
print(clothing1.display_product_info())