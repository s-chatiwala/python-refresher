import unittest
import Ps1 

class TestBankAccount(unittest.TestCase):
    def test_withdraw(self):
        SabahAcnt = Ps1.BankAccount("Sabah", 100, 108780)
        self.assertEqual(SabahAcnt.withdraw(10), True)
        self.assertEqual(SabahAcnt.withdraw(105), False)

    def test_deposit(self):
        SabahAcnt = Ps1.BankAccount("Sabah", 100, 108780)
        self.assertEqual(SabahAcnt.deposit(5), 105)
        self.assertNotEqual(SabahAcnt.deposit(20), 115)

    def test_current_balance(self):
        SabahAcnt = Ps1.BankAccount("Sabah", 100, 108780)
        self.assertEqual(SabahAcnt.current_balance(), "Your current balance is $100.")
        TrishaAcnt = Ps1.BankAccount("Trisha", 106, 109234)
        self.assertEqual(TrishaAcnt.current_balance(), "Your current balance is $106.")
if __name__ == "__main__":
    unittest.main()