//// Tests for `remove`.

import lab08.{remove}

pub fn remove_examples_test() {
  assert remove([3, 4, 3, 4, 4, 3], 3) == [4, 4, 4]
  assert remove([3, 4, 3, 4, 4, 3], 4) == [3, 3, 3]
}

pub fn remove_keeps_order_test() {
  assert remove([1, 3, 2], 1) == [3, 2]
  assert remove([1, 3, 2], 2) == [1, 3]
  assert remove([1, 3, 3, 7], 3) == [1, 7]
    as "Remove every 3, not just the first"
}

pub fn remove_nothing_test() {
  assert remove([1, 3, 2], 42) == [1, 3, 2] as "There's no 42 to remove"
  assert remove([], 3) == []
  assert remove([5, 5, 5], 5) == [] as "Every element is removed"
}
