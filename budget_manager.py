class BudgetManager:
    """
    Manages the user's budget, allowing for setting, increasing, and decreasing the total budget.
    """
    def __init__(self) -> None:
        self._budget = 0.0  # Initialize the budget to zero

    def set_budget(self, amount: float) -> None:
        """Sets the total available budget."""
        self._budget = amount

    def adjust_budget(self, sign: str, amount: float) -> None:
        """Adjusts the budget by a specified amount. Positive to increase, negative to decrease."""
        if sign == '-':
            self._budget -= amount
        elif sign == '+':
            self._budget += amount
        else:
            raise KeyError('Invalid sign')

    def get_budget(self) -> float:
        """Returns the current available budget."""
        return self._budget
