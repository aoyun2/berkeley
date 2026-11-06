import grader.{check, question}
import pair_up_test
import perfect_fit_test
import remove_test
import rope_test

pub fn main() -> Nil {
  grader.main([
    question("perfect_fit", 0, [
      check(
        "perfect_fit_examples_test",
        perfect_fit_test.perfect_fit_examples_test,
      ),
      check(
        "perfect_fit_different_squares_test",
        perfect_fit_test.perfect_fit_different_squares_test,
      ),
      check(
        "perfect_fit_more_squares_test",
        perfect_fit_test.perfect_fit_more_squares_test,
      ),
      check("perfect_fit_zero_test", perfect_fit_test.perfect_fit_zero_test),
    ]),
    question("remove", 0, [
      check("remove_examples_test", remove_test.remove_examples_test),
      check("remove_keeps_order_test", remove_test.remove_keeps_order_test),
      check("remove_nothing_test", remove_test.remove_nothing_test),
    ]),
    question("pair_up", 0, [
      check("pair_up_examples_test", pair_up_test.pair_up_examples_test),
      check("pair_up_short_test", pair_up_test.pair_up_short_test),
      check("pair_up_strings_test", pair_up_test.pair_up_strings_test),
    ]),
    question("up", 0, [
      check("up_examples_test", rope_test.up_examples_test),
      check("up_one_digit_test", rope_test.up_one_digit_test),
      check("up_equal_digits_test", rope_test.up_equal_digits_test),
    ]),
  ])
}
