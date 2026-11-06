//// Tests for `min` and `sqrt`.

import hw07.{min, sqrt}

pub fn min_examples_test() {
  assert min(0, 10, fn(x) { { x - 6 } * { x - 2 } }) == 4
  assert min(3, 8, fn(_) { 0 }) == 3
}

pub fn min_range_test() {
  assert min(-5, 5, fn(x) { x * x }) == 0
    as "the range includes negative integers when start is negative"
  assert min(0, 10, fn(x) { 0 - x }) == 9
    as "the largest integer in the range is 9, since end is not included"
  assert min(4, 5, fn(x) { x }) == 4 as "a range with one integer"
}

pub fn min_ties_test() {
  assert min(1, 10, fn(x) { x % 3 }) == 3
    as "3, 6, and 9 all have key 0, so return the smallest of them"
  assert min(-3, 4, fn(x) { { x * x - 4 } * { x * x - 4 } }) == -2
    as "-2 and 2 both have key 0, so return -2"
}

pub fn sqrt_examples_test() {
  assert sqrt(144) == 12
  assert sqrt(50) == 7
  assert sqrt(56) == 7
  assert sqrt(57) == 8
  assert sqrt(90) == 9
  assert sqrt(91) == 10
  assert sqrt(169) == 13
  assert sqrt(210) == 14
  assert sqrt(211) == 15
  assert sqrt(250) == 16
}

pub fn sqrt_small_test() {
  assert sqrt(1) == 1
  assert sqrt(2) == 1
  assert sqrt(3) == 2
  assert sqrt(4) == 2
}
