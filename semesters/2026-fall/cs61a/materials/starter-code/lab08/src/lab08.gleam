//// Lab 8: Gleam Lists.

/// Whether there are `n` different positive perfect squares that sum to
/// `total`, where `total` and `n` are nonnegative.
pub fn perfect_fit(total: Int, n: Int) -> Bool {
  fit_from(total, n, 1)
}

/// Whether there are `n` different perfect squares, each `k * k` or greater,
/// that sum to `total`.
pub fn fit_from(total: Int, n: Int, k: Int) -> Bool {
  case total, n {
    0, 0 -> True
    _, _ if total < k * k -> False
    // YOUR CODE HERE (replace the code below)
    _, _ -> todo
  }
}

/// A list of the elements of `s` that are not equal to `x`, in order.
pub fn remove(s: List(Int), x: Int) -> List(Int) {
  case s {
    [] -> []
    // YOUR CODE HERE (replace the code below)
    [first, ..rest] -> todo
  }
}

/// The items of `s` in order, grouped into lists of 2 items, except that
/// the last list has 3 items when the length of `s` is odd and at least 3.
/// If `s` has fewer than 2 items, the result is a list containing just `s`.
pub fn pair_up(s: List(a)) -> List(List(a)) {
  // YOUR CODE HERE (replace the code below)
  todo
}

/// The shortest rope of the digits of `n` in which the numbers in each list
/// are increasing, where `n` is positive.
pub fn up(n: Int) -> List(List(Int)) {
  // YOUR CODE HERE (replace the code below)
  up_helper(n / 10, todo)
}

/// The rope `result` with the digits of `n` added to its front.
pub fn up_helper(n: Int, result: List(List(Int))) -> List(List(Int)) {
  let first = n % 10
  case n, result {
    0, _ -> result
    // YOUR CODE HERE (replace the code below)
    _, _ -> todo
  }
}

pub fn main() {
  echo "Try calling your functions here, then run this code with gleam run"
}
