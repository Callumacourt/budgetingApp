from budget_manager import BudgetManager
from category_manager import CategoryManager
from expense_manager import ExpenseManager

class ExpenseHandler:
    def __init__(self) -> None:
        """Initialises each handler with each manager"""
        self.budgetManager = BudgetManager()
        self.categoryManager = CategoryManager()
        self.expenseManager = ExpenseManager()

    def switchBudget(self, name):
        """Switch to the specified budget"""
        self.budgetManager.set_active_budget(name)

    def add_expense(self, topic: str, amount: float, category: str) -> None:
        """Handles adding an expense and it's effect on budget etc"""
        # Add expense in ExpenseManager
        self.expenseManager.add_expense(topic, amount, category)
        # Add expense to corresponding category
        self.categoryManager.add_expense_to_category(topic, amount, category)
        # Decrease the budget by the expense
        self.budgetManager.adjust_budget('-', amount) 

    def adjust_expense(self, topic: str, new_amount: float, category: str) -> None:
        """Handles changing expense amount after they are already initialised"""
        # Adjust the expense in ExpenseManager
        difference = self.expenseManager.adjust_expense(topic, new_amount, category)
        
        # Adjust the budget based on the change
        if difference < 0:
            # If difference is negative, we are reducing the expense, so we add to the budget
            self.budgetManager.adjust_budget('+', abs(difference))
        else:
            # If difference is positive, we are increasing the expense, so we subtract from the budget
            self.budgetManager.adjust_budget('-', difference)

    def remove_expense(self, topic: str) -> None:
        """Handles consequences of removing an expense"""
        # Remove expense from ExpenseManager and add the amount back to the budget
        amount = self.expenseManager.remove_expense(topic)
        self.budgetManager.adjust_budget('+', amount)