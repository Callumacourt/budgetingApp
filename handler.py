from budget_manager import BudgetManager
from category_manager import CategoryManager
from expense_manager import ExpenseManager

# handler.py
class ExpenseHandler:
    def __init__(self) -> None:
        self.budgetManager = BudgetManager()
        self.categoryManager = CategoryManager()
        self.expenseManager = ExpenseManager()

    def add_expense(self, topic: str, amount: float, category: str) -> None:
        # Add expense in ExpenseManager
        self.expenseManager.add_expense(topic, amount, category)
        # Add expense to corresponding category
        self.categoryManager.add_expense_to_category(topic, amount, category)

    def adjust_expense(self, topic: str, amount: float, category: str) -> None:
        # Adjust expense in ExpenseManager
        self.expenseManager.adjust_expense(topic, amount, category)

    def remove_expense(self, topic: str) -> None:
        # Remove expense from ExpenseManager
        self.expenseManager.remove_expense(topic)

manager = ExpenseHandler()