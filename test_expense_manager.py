import unittest
from expense import ExpenseHandler, BudgetManager, CategoryManager  # Import the necessary classes from your main module

class TestExpenseHandler(unittest.TestCase):

    def setUp(self):
        """Set up a new instance of ExpenseHandler for each test"""
        self.manager = ExpenseHandler()  # Initialize the main manager

    def testCategoryAdder(self):
        """Test adding categories to expenses and vice versa"""
        self.manager.expenseManager.addExpense('Rent', 1000, 'Bills')
        self.assertEqual(self.manager.expenseManager.getExpenses()['Rent']['amount'], 1000)

    # ---------- EXPENSE TESTS ----------

    def testAddExpense(self):
        """Test adding an expense"""
        self.manager.expenseManager.addExpense('Rent', 1000, 'Bills')
        expectedExpense = {'Rent': {'amount': 1000, 'category': 'Bills'}}
        self.assertEqual(self.manager.expenseManager.getExpenses(), expectedExpense)

    def testAdjustExpense(self):
        """Test adjusting an expense"""
        self.manager.expenseManager.addExpense('Rent', 1000, 'Bills')
        self.manager.expenseManager.adjustExpense('Rent', 500, 'Bills')
        self.assertEqual(self.manager.expenseManager.getExpenses()['Rent']['amount'], 500)

    def testRemoveExpense(self):
        """Test removing an expense"""
        self.manager.expenseManager.addExpense('Rent', 1000, 'Bills')  # Add before removing
        self.manager.expenseManager.removeExpense("Rent")
        self.assertNotIn("Rent", self.manager.expenseManager.getExpenses())

    def testGetExpenses(self):
        """Test returning the expenses"""
        self.manager.expenseManager.addExpense('Rent', 1000, 'Bills')
        expectedExpense = {'Rent': {'amount': 1000, 'category': 'Bills'}}
        self.assertEqual(self.manager.expenseManager.getExpenses(), expectedExpense)

    def testBudget(self):
        """Test setting a budget"""
        self.manager.budgetManager.setBudget(1000)
        self.assertEqual(self.manager.budgetManager.budget, 1000)

    def testIncreaseBudget(self):
        """Test adding to the budget"""
        self.manager.budgetManager.setBudget(1000)
        self.manager.budgetManager.addToBudget(1000)
        self.assertEqual(self.manager.budgetManager.budget, 2000)

    def testDecreaseBudget(self):
        """Test decreasing the budget"""
        self.manager.budgetManager.setBudget(1000)
        self.manager.budgetManager.decreaseBudget(500)
        self.assertEqual(self.manager.budgetManager.budget, 500)

    def testTotal(self):
        """Test calculating budget - expenses"""
        self.manager.budgetManager.setBudget(1000)
        self.manager.expenseManager.addExpense('Rent', 1000, 'Bills')
        total_remaining = self.manager.budgetManager.budget - sum(e['amount'] for e in self.manager.expenseManager.getExpenses().values())
        self.assertEqual(total_remaining, 0)

if __name__ == '__main__':
    unittest.main()  # This allows you to run the tests directly
