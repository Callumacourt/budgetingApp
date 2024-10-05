# ---------- BUDGET MANAGEMENT ----------

class BudgetManager:
    """
    Manages the user's budget, allowing for setting, increasing, and decreasing the total budget.
    """
    def __init__(self) -> None:
        self._budget = 0.0  # Initialize the budget to zero

    def set_budget(self, amount: float) -> None:
        """Sets the total available budget."""
        self._budget = amount

    def add_to_budget(self, amount: float) -> None:
        """Increases the budget by a specified amount."""
        self._budget += amount

    def decrease_budget(self, amount: float) -> None:
        """Decreases the budget by a specified amount."""
        self._budget -= amount

    def get_budget(self) -> float:
        """Returns the current available budget."""
        return self._budget


# ---------- EXPENSE MANAGEMENT ----------

class ExpenseManager:
    """
    Manages expenses by adding, adjusting, removing expenses and categorizing them.
    Links expenses to their respective categories.
    """
    def __init__(self, category_manager: 'CategoryManager') -> None:
        self._expense_list = {}  # Holds expenses with details of amount and category
        self._category_manager = category_manager

    def add_expense(self, topic: str, amount: float, category: str) -> None:
        """Adds a new expense to both the expense list and category."""
        if topic in self._expense_list:
            raise KeyError('Topic already in expenses')  # Avoid duplicate expenses

        # Add the expense to the list and update the category manager
        self._expense_list[topic] = {'amount': amount, 'category': category}
        self._category_manager.add_expense_to_category(topic, amount, category)

    def adjust_expense(self, topic: str, amount: float, category: str) -> None:
        """
        Adjusts the amount or category of an existing expense.
        Raises KeyError if the expense does not exist.
        """
        if topic not in self._expense_list:
            raise KeyError('Topic not found in expenses')  # Ensure the expense exists
        
        # Update the expense amount
        self._expense_list[topic]['amount'] = amount

        # If the category has changed, update it
        if self._expense_list[topic]['category'] != category:
            self._expense_list[topic]['category'] = category

    def remove_expense(self, topic: str) -> None:
        """Removes an expense by its topic, if it exists."""
        if topic in self._expense_list:
            del self._expense_list[topic]

    def get_expenses(self) -> dict:
        """Returns a dictionary of all expenses."""
        return self._expense_list

    def get_total_expenses(self) -> float:
        """Calculates and returns the total sum of all expenses."""
        return sum(expense['amount'] for expense in self._expense_list.values())


# ---------- CATEGORY MANAGEMENT ----------

class CategoryManager:
    """
    Manages expense categories. Allows adding categories and assigning expenses to them.
    """
    def __init__(self) -> None:
        self._categories = {}  # Dictionary of categories with expenses

    def add_category(self, category: str) -> None:
        """Adds a new category. Raises an error if the category already exists."""
        if category in self._categories:
            raise ValueError("Category already exists")
        # Initialize the category with an empty list of expenses
        self._categories[category] = []

    def add_expense_to_category(self, topic: str, amount: float, category: str) -> None:
        """Adds an expense under the specified category. Creates the category if it doesn't exist."""
        if category not in self._categories:
            self.add_category(category)  # Automatically create the category if it's missing
        # Add the expense to the correct category
        self._categories[category].append({'topic': topic, 'amount': amount})


# ---------- WHOLE FILE MANAGEMENT ----------

class ExpenseHandler:
    """
    Handles the interaction between budget, expenses, and categories.
    Links the budget manager, category manager, and expense manager together.
    """
    def __init__(self) -> None:
        self.budgetManager = BudgetManager()
        self.categoryManager = CategoryManager()

        # Pass category manager to the expense manager for expense categorization
        self.expenseManager = ExpenseManager(self.categoryManager)

# Initialize the main expense handler
manager = ExpenseHandler()
