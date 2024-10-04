 
# ---------- BUDGET MANAGEMENT ----------

class BudgetManager:
    def __init__(self):
        "Initialise budget to zero"
        self.budget = 0

    def setBudget(self, amount):
        self.budget = amount

    def addToBudget(self, amount):
        self.budget += amount

    def decreaseBudget(self, amount):
        self.budget -= amount

 # ---------- EXPENSE MANAGEMENT ----------

class ExpenseManager:
    def __init__(self):
        self.expense_list = {}

    def addExpense(self, topic, amount, category):
        if topic in self.expense_list:
            raise KeyError('Topic already in expenses')
        else:
            # Add the expense to the expense_list
            self.expense_list[topic] = {'amount': amount, 'category': category}

    def adjustExpense(self, topic, amount, category):
        # Raise error if topic isn't contained in expenses
        if topic not in self.expense_list:
            raise KeyError('Topic not found in expenses')
        # Change the category if passed a differing one
        elif self.expense_list[topic]['category'] != category:
            self.expense_list[topic]['category'] = category
        # Set the amount of the expense
        else:
            # Update the amount in the existing dictionary
            self.expense_list[topic]['amount'] = amount  # Corrected this line

    def removeExpense(self, topic):
        if topic in self.expense_list:
            del self.expense_list[topic]

    def getExpenses(self):
        return self.expense_list

    def getTotalExpenses(self):
        return sum(expense['amount'] for expense in self.expense_list.values())

    
# ---------- CATEGORY MANAGEMENT ----------

class CategoryManager:
    def __init__(self):
        self.categories = {}

    def addCategory(self, category):
        if category in self.categories:
            raise ValueError("Category already exists")
        else: self.categories[category] = []

    def addExpenseToCategory(self, topic, amount, category):
        if category not in self.categories:
            self.addCategory(category)
        else:
            self.categories[category].append({'topic': topic, 'amount': amount})


 # ---------- WHOLE FILE MANAGEMENT ----------

class ExpenseHandler:
    def __init__(self):
        self.budgetManager = BudgetManager()
        self.expenseManager = ExpenseManager()
        self.categoryManager = CategoryManager()

manager = ExpenseHandler()