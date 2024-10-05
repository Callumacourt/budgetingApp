# handler.py

from budget_manager import BudgetManager
from category_manager import CategoryManager
from expense_manager import ExpenseManager

class ExpenseHandler:
    """
    Handles the interaction between budget, expenses, and categories.
    Links the budget manager, category manager, and expense manager together.
    """
    def __init__(self) -> None:
        self.budgetManager = BudgetManager()
        self.categoryManager = CategoryManager()

        # Pass category manager to the expense manager for proper expense categorization
        self.expenseManager = ExpenseManager(self.categoryManager)

# Initialize the main expense handler
if __name__ == "__main__":
    manager = ExpenseHandler()
 
