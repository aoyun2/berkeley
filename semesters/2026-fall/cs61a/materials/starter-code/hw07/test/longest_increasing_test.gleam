//// Tests for `longest_increasing`.

import hw07.{longest_increasing}

pub fn longest_increasing_examples_test() {
  assert longest_increasing([1, 2, 3, 4, 9, 3, 4, 1, 10, 5])
    == [1, 2, 3, 4, 9, 10]
  assert longest_increasing([3, 1, 2]) == [1, 2]
  assert longest_increasing([5, 1, 6, 2, 7, 3, 4]) == [1, 2, 3, 4]
}

pub fn longest_increasing_strict_test() {
  assert longest_increasing([2, 2, 2]) == [2]
    as "equal elements are not strictly increasing, so only one can be kept"
  assert longest_increasing([1, 3, 3, 5, 5, 2]) == [1, 3, 5]
}

pub fn longest_increasing_skips_test() {
  assert longest_increasing([10, 1, 2, 3]) == [1, 2, 3]
    as "the first element is not always kept"
  assert longest_increasing([1, 9, 2, 8, 3, 4]) == [1, 2, 3, 4]
  assert longest_increasing([-3, 10, -2, 11, -1, 0, 12]) == [-3, -2, -1, 0, 12]
}

pub fn longest_increasing_short_test() {
  assert longest_increasing([]) == []
  assert longest_increasing([7]) == [7]
  assert longest_increasing([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
}
