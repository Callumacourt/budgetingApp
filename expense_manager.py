# expense_manager.py

from category_manager import CategoryManager

class ExpenseManager:
    """
    Manages expenses by adding, adjusting, and removing expenses, and categorizing them.
    Links expenses to their respective categories.
    """
    def __init__(self, category_manager: CategoryManager) -> None:
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
