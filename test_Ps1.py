import unittest
import Ps1 

class TestBankAccount(unittest.TestCase):
    def test_withdraw(self):
        SabahAcnt = Ps1.BankAccount("Sabah", 100, 108780)
        self.assertEqual(SabahAcnt.withdraw(10), True)
        self.assertEqual(SabahAcnt.withdraw(105), False)
        self.assertNotEqual(SabahAcnt.withdraw(115), True)

    def test_deposit(self):
        SabahAcnt = Ps1.BankAccount("Sabah", 100, 108780)
        self.assertEqual(SabahAcnt.deposit(5), 105)
        self.assertNotEqual(SabahAcnt.deposit(20), 115)
        self.assertEqual(SabahAcnt.deposit(20), 145)

    def test_current_balance(self):
        SabahAcnt = Ps1.BankAccount("Sabah", 100, 108780)
        self.assertEqual(SabahAcnt.current_balance(), "Your current balance is $100.")
        TrishaAcnt = Ps1.BankAccount("Trisha", 106, 109234)
        self.assertEqual(TrishaAcnt.current_balance(), "Your current balance is $106.")
        AllisonAcnt = Ps1.BankAccount("Allison", 10008, 109234)
        self.assertNotEqual(AllisonAcnt.current_balance(), "Your current balance is $12020.")
if __name__ == "__main__":
    unittest.main()