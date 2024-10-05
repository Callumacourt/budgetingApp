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
