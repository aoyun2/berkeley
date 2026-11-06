//// Homework 7: Gleam.

import gleam/int
import gleam/list

/// `base` raised to the power `exp`, where `exp` is a nonnegative integer.
pub fn pow(base: Int, exp: Int) -> Int {
  // YOUR CODE HERE (replace the code below)
  todo
}

/// The smallest factor of `n` greater than 1, where `n` is greater than 1.
pub fn smallest_factor(n: Int) -> Int {
  // YOUR CODE HERE (replace the code below)
  todo
}

/// The integer `k` from `start` up to (but not including) `end` for
/// which `key(k)` is smallest. If several integers tie for the smallest key
/// value, return the smallest of them. Assume `start` is less than `end`.
pub fn min(start: Int, end: Int, key: fn(Int) -> Int) -> Int {
  // YOUR CODE HERE (replace the code below)
  todo
}

/// The positive integer whose square is closest to `n`, where `n` is positive.
pub fn sqrt(n: Int) -> Int {
  // YOUR CODE HERE (replace the code below)
  int.absolute_value(n)
}

/// Whether `s` is made up of adjacent pairs of equal elements.
/// An empty list is, but a list with an odd length is not.
pub fn pairs(s: List(a)) -> Bool {
  // YOUR CODE HERE (replace the code below)
  todo
}

/// The longest sublist of `s` whose elements are strictly increasing.
/// Assume that this longest sublist is unique.
pub fn longest_increasing(s: List(Int)) -> List(Int) {
  // YOUR CODE HERE (replace the code below)
  todo
}

pub fn main() {
  echo "Try calling your functions here, then run this code with gleam run"
}
