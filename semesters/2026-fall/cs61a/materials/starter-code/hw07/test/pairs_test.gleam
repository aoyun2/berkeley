//// Tests for `pairs`.

import hw07.{pairs}

pub fn pairs_true_test() {
  assert pairs([1, 1, 2, 2, 3, 3]) == True
  assert pairs([4, 4]) == True
  assert pairs(["a", "a", "b", "b"]) == True
}

pub fn pairs_false_test() {
  assert pairs([1, 1, 2, 3]) == False
  assert pairs([1, 2, 1, 2]) == False
  assert pairs([1, 1, 2, 2, 3, 4]) == False
}

pub fn pairs_alignment_test() {
  assert pairs([1, 2, 2, 3, 3, 1]) == False
    as "pairs start at the first element, so [1, 2] is the first pair"
  assert pairs([5, 5, 5, 5]) == True as "two pairs may hold the same value"
  assert pairs([5, 5, 5]) == False as "the last 5 has no partner"
}

pub fn pairs_short_test() {
  assert pairs([]) == True
  assert pairs([7]) == False
  assert pairs([1, 1, 2]) == False
}
