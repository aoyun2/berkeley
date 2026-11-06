//// Tests for `perfect_fit`.

import lab08.{perfect_fit}

pub fn perfect_fit_examples_test() {
  assert perfect_fit(10, 2) == True as "10 = 1*1 + 3*3"
  assert perfect_fit(9, 1) == True as "9 = 3*3"
  assert perfect_fit(9, 2) == False
    as "No two different perfect squares sum to 9"
  assert perfect_fit(25, 1) == True as "25 = 5*5"
  assert perfect_fit(25, 2) == True as "25 = 3*3 + 4*4"
}

pub fn perfect_fit_different_squares_test() {
  assert perfect_fit(9, 3) == False
    as "9 = 1*1 + 2*2 + 2*2 doesn't count, because 2*2 is repeated"
  assert perfect_fit(8, 2) == False
    as "8 = 2*2 + 2*2 doesn't count, because 2*2 is repeated"
  assert perfect_fit(2, 2) == False
    as "2 = 1*1 + 1*1 doesn't count, because 1*1 is repeated"
}

pub fn perfect_fit_more_squares_test() {
  assert perfect_fit(14, 3) == True as "14 = 1*1 + 2*2 + 3*3"
  assert perfect_fit(30, 4) == True as "30 = 1*1 + 2*2 + 3*3 + 4*4"
  assert perfect_fit(50, 2) == True as "50 = 1*1 + 7*7"
  assert perfect_fit(50, 3) == True as "50 = 3*3 + 4*4 + 5*5"
  assert perfect_fit(29, 4) == False
    as "Four different squares sum to at least 30"
}

pub fn perfect_fit_zero_test() {
  assert perfect_fit(0, 0) == True as "Zero squares sum to 0"
  assert perfect_fit(4, 0) == False as "Zero squares can't sum to 4"
  assert perfect_fit(0, 1) == False as "One positive square can't sum to 0"
}
