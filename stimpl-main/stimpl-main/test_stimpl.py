
import sys
from stimpl.expression import *
from stimpl.runtime import *
from stimpl.robustness import run_stimpl_robustness_tests
from stimpl.test import run_stimpl_sanity_tests
from stimpl.runtime import run_stimpl
from stimpl.test_state import test_state_implementation

if __name__=='__main__':
  test_state_implementation()
  run_stimpl_sanity_tests()
  run_stimpl_robustness_tests()
  
  # program = Eq(BooleanLiteral(False), BooleanLiteral(True))
  # print(run_stimpl(program))