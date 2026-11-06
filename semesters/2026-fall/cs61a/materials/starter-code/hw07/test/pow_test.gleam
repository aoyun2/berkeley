//// Tests for `pow`: that it computes the right power, and that it
//// does so quickly without too many recursive calls.

import hw07.{pow}

pub fn pow_examples_test() {
  assert pow(2, 10) == 1024
  assert pow(3, 3) == 27
  assert pow(5, 4) == 625
  assert pow(2, 19) == 524_288
  assert pow(2, 32) == 4_294_967_296
  assert pow(5, 19) == 19_073_486_328_125
  assert pow(2, 0) == 1
  assert pow(7, 1) == 7
  assert pow(1, 20) == 1
}

// Try a very large exponent to ensure the implementation is fast.
pub fn pow_is_fast_test() {
  assert pow(1, 10_000_000_000) == 1
}
