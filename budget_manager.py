class BudgetManager:
    """
    Manages multiple budgets, allowing for setting, increasing, and decreasing the total budget for each.
    """
    def __init__(self) -> None:
        # Set a default active budget
        self._budgets = {'default': 0.0}
        self._active_budget = 'default'

    def set_budget(self, name: str, amount: float) -> None:
        """Creates or updates a budget for the given name."""
        if amount < 0:
            raise ValueError('Budget amount must be non-negative.')
        self._budgets[name] = amount
        self._active_budget = name  # Set this as the active budget by default

    def set_active_budget(self, name: str) -> None:
        """Switches to the given budget name."""
        if name not in self._budgets:
            raise KeyError(f"Budget '{name}' not found.")
        self._active_budget = name

    def get_active_budget_name(self) -> str:
        """Returns the name of the currently active budget."""
        if self._active_budget is None:
            raise ValueError('No active budget selected.')
        return self._active_budget

    def adjust_budget(self, sign: str, amount: float) -> None:
        """Adjusts the currently active budget by a specified amount."""
        if self._active_budget is None:
            raise ValueError('No active budget selected.')
        if amount < 0:
            raise ValueError('Amount to adjust must be non-negative.')

        if sign == '-':
            self._budgets[self._active_budget] -= amount
        elif sign == '+':
            self._budgets[self._active_budget] += amount
        else:
            raise ValueError('Invalid sign. Use "+" to increase or "-" to decrease.')

    def get_budget(self, name: str) -> float:
        """Returns the current available budget for the given name."""
        if name not in self._budgets:
            raise KeyError(f"Budget with name '{name}' not found.")
        return self._budgets[name]

    def get_active_budget(self) -> float:
        """Returns the budget for the currently active budget."""
        if self._active_budget is None:
            raise ValueError('No active budget selected.')
        return self._budgets[self._active_budget]

