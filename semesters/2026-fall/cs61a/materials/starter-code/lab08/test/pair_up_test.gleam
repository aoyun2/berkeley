//// Tests for `pair_up`.

import lab08.{pair_up}

pub fn pair_up_examples_test() {
  assert pair_up([3, 4, 5, 6, 7, 8]) == [[3, 4], [5, 6], [7, 8]]
  assert pair_up([3, 4, 5, 6, 7, 8, 9]) == [[3, 4], [5, 6], [7, 8, 9]]
    as "The last list has 3 items when the length is odd"
}

pub fn pair_up_short_test() {
  assert pair_up([1, 2]) == [[1, 2]]
  assert pair_up([1, 2, 3]) == [[1, 2, 3]]
  assert pair_up([1, 2, 3, 4]) == [[1, 2], [3, 4]]
    as "Four items make two pairs"
  assert pair_up([1, 2, 3, 4, 5]) == [[1, 2], [3, 4, 5]]
}

pub fn pair_up_strings_test() {
  assert pair_up(["a", "b", "c", "d", "e", "f", "g", "h"])
    == [["a", "b"], ["c", "d"], ["e", "f"], ["g", "h"]]
}
