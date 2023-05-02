import unittest

from unittest.loader import makeSuite

from test_cases.add_player import TestAddPlayer
from test_cases.framework import Test
from test_cases.open_add_player_form import TestOpenAddPlayer
from test_cases.add_language_to_existing_player_form import TestAddLanguageToExistingPlayerForm
from test_cases.clear_add_player_form import TestClearAddPlayerForm
from test_cases.remove_language_from_existing_player import TestRemoveLanguageFromExistingPlayerForm
from test_cases.login_to_the_system import TestLoginPage
from test_cases.sign_out_from_the_system import TestSignOutFromTheSystem

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestOpenAddPlayer))
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestAddLanguageToExistingPlayerForm))
   test_suite.addTest(makeSuite(TestClearAddPlayerForm))
   test_suite.addTest(makeSuite(TestRemoveLanguageFromExistingPlayerForm))
   test_suite.addTest(makeSuite(TestSignOutFromTheSystem))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
