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

    def get_categories(self) -> dict:
        return self._categories 