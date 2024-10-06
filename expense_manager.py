class ExpenseManager:
    """
    Manages expenses by adding, adjusting, and removing expenses, and categorizing them.
    Links expenses to their respective categories.
    """
    def __init__(self) -> None:
        self._expense_list = {}  # Holds expenses with details of amount and category

    def add_expense(self, topic: str, amount: float, category: str) -> None:
        """Adds a new expense to both the expense list and category."""
        if topic in self._expense_list:
            raise KeyError('Topic already in expenses')  # Avoid duplicate expenses
        # Add the expense to the list 
        self._expense_list[topic] = {'amount': amount, 'category': category}

    def adjust_expense(self, topic: str, amount: float, category: str) -> float:
        """
        Adjusts the amount or category of an existing expense.
        Raises KeyError if the expense does not exist.
        """
        if topic not in self._expense_list:
            raise KeyError('Topic not found in expenses')  # Ensure the expense exists
        
        # Update the expense amount and calculate the difference
        previous_amount = self._expense_list[topic]['amount']
        self._expense_list[topic]['amount'] = amount

        # If the category has changed, update it
        if self._expense_list[topic]['category'] != category:
            self._expense_list[topic]['category'] = category
        
        # Calculate the difference (new amount - previous amount)
        difference = amount - previous_amount
        return difference

    def remove_expense(self, topic: str) -> float:
        """Removes an expense by its topic, if it exists and returns the amount."""
        if topic in self._expense_list:
            # Store the value so that the budget can be adjusted accordingly
            amount = self._expense_list[topic]['amount']
            del self._expense_list[topic]
            return amount
        else:
            raise KeyError('Topic not found in expenses')  # Raise error if topic doesn't exist

    def get_expenses(self) -> dict:
        """Returns a dictionary of all expenses."""
        return self._expense_list

    def get_total_expenses(self) -> float:
        """Calculates and returns the total sum of all expenses."""
        return sum(expense['amount'] for expense in self._expense_list.values())
