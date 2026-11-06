//// Tests for `up`.

import lab08.{up}

pub fn up_examples_test() {
  assert up(314_152_667_899) == [[3], [1, 4], [1, 5], [2, 6], [6, 7, 8, 9], [9]]
  assert up(1234) == [[1, 2, 3, 4]]
    as "Every digit is larger than the one before"
  assert up(4321) == [[4], [3], [2], [1]]
    as "Every digit is smaller than the one before"
}

pub fn up_one_digit_test() {
  assert up(7) == [[7]]
}

pub fn up_equal_digits_test() {
  assert up(1223) == [[1, 2], [2, 3]]
    as "2 is not greater than 2, so the second 2 starts a new list"
  assert up(55) == [[5], [5]]
}
