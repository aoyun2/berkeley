//// Tests for `smallest_factor`.

import hw07.{smallest_factor}

pub fn smallest_factor_examples_test() {
  assert smallest_factor(51) == 3
  assert smallest_factor(49) == 7
  assert smallest_factor(13) == 13
}

// Even numbers, including 2 itself, have 2 as their smallest factor.
pub fn smallest_factor_even_test() {
  assert smallest_factor(2) == 2
  assert smallest_factor(4) == 2
  assert smallest_factor(72_000) == 2
}

// A prime's smallest factor is itself, so the search runs all the way to n.
pub fn smallest_factor_prime_test() {
  assert smallest_factor(3) == 3
  assert smallest_factor(97) == 97
  assert smallest_factor(7919) == 7919
}

// The product of two primes has the smaller one as its smallest factor.
pub fn smallest_factor_product_test() {
  assert smallest_factor(15) == 3
  assert smallest_factor(11 * 13) == 11
  assert smallest_factor(101 * 103) == 101
}
