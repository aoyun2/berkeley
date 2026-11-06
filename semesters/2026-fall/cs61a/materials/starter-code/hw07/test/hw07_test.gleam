import grader.{check, question}
import longest_increasing_test
import min_test
import pairs_test
import pow_test
import smallest_factor_test

pub fn main() -> Nil {
  grader.main([
    question("pow", 0, [
      check("pow_examples_test", pow_test.pow_examples_test),
      check("pow_is_fast_test", pow_test.pow_is_fast_test),
    ]),
    question("smallest_factor", 0, [
      check(
        "smallest_factor_examples_test",
        smallest_factor_test.smallest_factor_examples_test,
      ),
      check(
        "smallest_factor_even_test",
        smallest_factor_test.smallest_factor_even_test,
      ),
      check(
        "smallest_factor_prime_test",
        smallest_factor_test.smallest_factor_prime_test,
      ),
      check(
        "smallest_factor_product_test",
        smallest_factor_test.smallest_factor_product_test,
      ),
    ]),
    question("min", 0, [
      check("min_examples_test", min_test.min_examples_test),
      check("min_range_test", min_test.min_range_test),
      check("min_ties_test", min_test.min_ties_test),
    ]),
    question("sqrt", 0, [
      check("sqrt_examples_test", min_test.sqrt_examples_test),
      check("sqrt_small_test", min_test.sqrt_small_test),
    ]),
    question("pairs", 0, [
      check("pairs_true_test", pairs_test.pairs_true_test),
      check("pairs_false_test", pairs_test.pairs_false_test),
      check("pairs_alignment_test", pairs_test.pairs_alignment_test),
      check("pairs_short_test", pairs_test.pairs_short_test),
    ]),
    question("longest_increasing", 0, [
      check(
        "longest_increasing_examples_test",
        longest_increasing_test.longest_increasing_examples_test,
      ),
      check(
        "longest_increasing_strict_test",
        longest_increasing_test.longest_increasing_strict_test,
      ),
      check(
        "longest_increasing_skips_test",
        longest_increasing_test.longest_increasing_skips_test,
      ),
      check(
        "longest_increasing_short_test",
        longest_increasing_test.longest_increasing_short_test,
      ),
    ]),
  ])
}
