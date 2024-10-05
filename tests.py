import unittest
from handler import ExpenseHandler

class TestExpenseHandler(unittest.TestCase):

    def setUp(self):
        """Set up a new instance of ExpenseHandler for each test"""
        self.manager = ExpenseHandler()  # Initialize the main manager

    # ---------- CATEGORY TESTING ----------

    def test_return_categories(self):
        """Tests returning category list"""
        self.manager.categoryManager.add_category('Bills')
        self.assertEqual(self.manager.categoryManager._categories, {'Bills': []})

    def test_task_category(self):
        """Tests adding an expense to a category"""
        self.manager.expenseManager.add_expense('Rent', 1000, 'Bills')
        self.assertEqual(self.manager.categoryManager._categories, {'Bills': [{'amount': 1000, 'topic': 'Rent'}]})

    # ---------- EXPENSE TESTING ----------

    def test_add_expense(self):
        """Test adding an expense"""
        self.manager.expenseManager.add_expense('Rent', 1000, 'Bills')
        expected_expense = {'Rent': {'amount': 1000, 'category': 'Bills'}}
        self.assertEqual(self.manager.expenseManager.get_expenses(), expected_expense)

    def test_adjust_expense(self):
        """Test adjusting an expense"""
        self.manager.expenseManager.add_expense('Rent', 1000, 'Bills')
        self.manager.expenseManager.adjust_expense('Rent', 500, 'Bills')
        self.assertEqual(self.manager.expenseManager.get_expenses()['Rent']['amount'], 500)
        self.assertEqual(self.manager.expenseManager.get_expenses()['Rent']['category'], 'Bills')

    def test_remove_expense(self):
        """Test removing an expense"""
        self.manager.expenseManager.add_expense('Rent', 1000, 'Bills')  # Add before removing
        self.manager.expenseManager.remove_expense("Rent")
        self.assertNotIn("Rent", self.manager.expenseManager.get_expenses())

    def test_get_expenses(self):
        """Test returning the expenses"""
        self.manager.expenseManager.add_expense('Rent', 1000, 'Bills')
        expected_expense = {'Rent': {'amount': 1000, 'category': 'Bills'}}
        self.assertEqual(self.manager.expenseManager.get_expenses(), expected_expense)

    # ---------- BUDGET TESTING ----------

    def test_budget(self):
        """Test setting a budget"""
        self.manager.budgetManager.set_budget(1000)
        self.assertEqual(self.manager.budgetManager.get_budget(), 1000)

    def test_increase_budget(self):
        """Test adding to the budget"""
        self.manager.budgetManager.set_budget(1000)
        self.manager.budgetManager.add_to_budget(1000)
        self.assertEqual(self.manager.budgetManager.get_budget(), 2000)

    def test_decrease_budget(self):
        """Test decreasing the budget"""
        self.manager.budgetManager.set_budget(1000)
        self.manager.budgetManager.decrease_budget(500)
        self.assertEqual(self.manager.budgetManager.get_budget(), 500)

    def test_total(self):
        """Test calculating budget - expenses"""
        self.manager.budgetManager.set_budget(1000)
        self.manager.expenseManager.add_expense('Rent', 1000, 'Bills')
        total_remaining = self.manager.budgetManager.get_budget() - self.manager.expenseManager.get_total_expenses()
        self.assertEqual(total_remaining, 0)


if __name__ == '__main__':
    unittest.main()
