//// Examples from 3.2 Functional Programming of Composing Programs:
//// https://composingprograms.com/3ed/functional-programming

import gleam/io
import gleam/string

/// Triple an integer
pub fn triple(x: Int) -> Int {
  3 * x
}

/// Sum the squares of x and y.
pub fn sum_squares(x: Int, y: Int) -> Int {
  let x2 = x * x
  let y2 = y * y
  x2 + y2
}

/// Compute a*x*x + b*x + c
pub fn quadratic(x: Int, a: Int, b: Int, c: Int) -> Int {
  let ax2 = {
    let x2 = x * x
    a * x2
  }

  // ax2 is in scope here, but x2 is not
  ax2 + b * x + c
}

/// x + 1, doubled
pub fn add_one_and_double(x: Int) -> Int {
  { x + 1 } * 2
}

pub fn print_thrice(s: String) {
  io.println(s)
  io.println(s)
  io.println(s)
}

/// cheer("bears") prints
/// Go BEARS!
/// Go BEARS!
/// Go BEARS!
pub fn cheer(mascot: String) {
  print_thrice("Go " <> string.uppercase(mascot) <> "!")
}

/// Combine x, y, and z by calling f on x and y, then z.
pub fn combine(x: Int, y: Int, z: Int, f: fn(Int, Int) -> Int) -> Int {
  f(f(x, y), z)
}

/// 3 + 4 + 5
pub fn twelve() -> Int {
  combine(3, 4, 5, fn(x, y) { x + y })
}

/// Calling three() returns 3, not 4.
pub fn three() -> Int {
  let x = 3
  let f = fn() { x }
  let x = 4
  f()
}

/// Call a function f twice on x.
fn twice(f: fn(t) -> t, x: t) -> t {
  f(f(x))
}

/// Echoes 12 and then "Hello!!", each after its line number.
pub fn test_twice() {
  let add_one = fn(x) { x + 1 }
  let exclaim = fn(x) { x <> "!" }

  echo twice(add_one, 10)
  echo twice(exclaim, "Hello")
}

/// Divide n by d if d evenly divides n, and otherwise return n.
pub fn attempt_to_divide(n: Int, d: Int) -> Int {
  case n % d == 0 {
    True -> n / d
    False -> n
  }
}

pub fn describe_positive(n: Int) -> String {
  case n {
    1 -> "One"
    2 | 3 | 4 -> "Few"
    _ -> "Many"
  }
}

pub fn describe(n: Int) -> String {
  case n {
    _ if n < 0 -> "Negative"
    0 -> "None"
    1 -> "One"
    2 | 3 | 4 -> "Few"
    _ -> "Many"
  }
}

/// Return True if either a or b is True but not both, and False otherwise.
pub fn exclusive_or(a: Bool, b: Bool) -> Bool {
  case a, b {
    True, False -> True
    False, True -> True
    _, _ -> False
  }
}

/// n * (n-1) * (n-2) * ... * 1
pub fn factorial(n: Int) -> Int {
  case n {
    _ if n <= 0 -> 1
    _ -> n * factorial(n - 1)
  }
}

/// Return the number of ways that a non-decreasing sequence of positive integers can sum to n.
/// E.g., count_all_partitions(5) counts 5, 1+4, 2+3, 1+1+3, 1+2+2, 1+1+1+2, and 1+1+1+1+1.
pub fn count_all_partitions(n: Int) -> Int {
  count_partitions(n, n)
}

/// Count the ways of summing to n using parts up to m to implement count_all_partitions.
fn count_partitions(n: Int, m: Int) -> Int {
  case n, m {
    0, _ -> 1
    _, _ if n < 0 || m <= 0 -> 0
    _, _ -> count_partitions(n - m, m) + count_partitions(n, m - 1)
  }
}
