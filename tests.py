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
        self.assertEqual(self.manager.categoryManager.get_categories(), {'Bills': []})

    def test_task_category(self):
        """Tests adding an expense to a category"""
        self.manager.add_expense('Rent', 1000, 'Bills')
        self.assertEqual(self.manager.categoryManager.get_categories(), {'Bills': [{'amount': 1000, 'topic': 'Rent'}]})

    # ---------- EXPENSE TESTING ----------

    def test_add_expense(self):
        """Test adding an expense"""
        self.manager.add_expense('Rent', 1000, 'Bills')
        expected_expense = {'Rent': {'amount': 1000, 'category': 'Bills'}}
        self.assertEqual(self.manager.expenseManager.get_expenses(), expected_expense)

    def test_adjust_expense(self):
        """Test adjusting an expense"""
        self.manager.add_expense('Rent', 1000, 'Bills')
        self.manager.adjust_expense('Rent', 500, 'Bills')
        self.assertEqual(self.manager.expenseManager.get_expenses()['Rent']['amount'], 500)
        self.assertEqual(self.manager.expenseManager.get_expenses()['Rent']['category'], 'Bills')

    def test_remove_expense(self):
        """Test removing an expense"""
        self.manager.add_expense('Rent', 1000, 'Bills')  # Add before removing
        self.manager.remove_expense("Rent")
        self.assertNotIn("Rent", self.manager.expenseManager.get_expenses())

    def test_get_expenses(self):
        """Test returning the expenses"""
        self.manager.add_expense('Rent', 1000, 'Bills')
        expected_expense = {'Rent': {'amount': 1000, 'category': 'Bills'}}
        self.assertEqual(self.manager.expenseManager.get_expenses(), expected_expense)

    # ---------- BUDGET TESTING ----------

    def test_budget(self):
        """Test setting a budget"""
        self.manager.budgetManager.set_budget('January', 1000)
        self.assertEqual(self.manager.budgetManager.get_budget('January'), 1000)


    def test_total(self):
        """Test calculating budget - expenses"""
        self.manager.budgetManager.set_budget('January', 1000)
        self.manager.add_expense('Rent', 1000, 'Bills')
        total_remaining = self.manager.budgetManager.get_budget('January')
        self.assertEqual(total_remaining, 0)

    def test_budget_adjust(self):
        """Test adjustment of budget when expense is modified."""
        # Set an initial budget
        self.manager.budgetManager.set_budget('January', 1000)
        self.manager.add_expense('Rent', 500, 'Bills')

        # The budget should now reflect the expense
        self.assertEqual(self.manager.budgetManager.get_budget('January'), 500)  # 1000 - 500 = 500

        # Adjust the expense to a higher value
        self.manager.adjust_expense('Rent', 700, 'Bills')  # Adjusting to a higher amount (700)

        # The budget should reflect the additional decrease
        self.assertEqual(self.manager.budgetManager.get_budget('January'), 500 - 200)  # 500 - (700 - 500) = 300

        # Adjust the expense to a lower value
        self.manager.adjust_expense('Rent', 300, 'Bills')  # Adjusting to a lower amount (300)

        # The budget should now reflect the increase
        self.assertEqual(self.manager.budgetManager.get_budget('January'), 300 + 400)  # 300 + (500 - 300) = 700

        # Test that this still works when current budget switched
        self.manager.budgetManager.set_budget('Feburary', 1000)
        self.manager.budgetManager.set_active_budget('Feburary')
        self.manager.add_expense('More rent', 500, 'Bills')
        self.assertEqual(self.manager.budgetManager.get_budget('Feburary'), 500) 




if __name__ == '__main__':
    unittest.main()
