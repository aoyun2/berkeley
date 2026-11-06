import gleam/int

pub fn main() {
  echo fact(5)
  echo describe(12)
  echo make_adder(3)(4)
  echo combine(2, 3, 4, fn(x, y) { x * y })
  echo sum_first_n(5)
  echo fact_tail(5)
  echo fib(50)
}

fn fact(n) {
  case n {
    0 -> 1
    _ -> n * fact(n - 1)
  }
}

fn describe(n: Int) -> String {
  int.to_string(n)
  <> " is "
  <> case n {
    _ if n < 0 -> "negative"
    0 -> "zero"
    1 -> "one"
    2 | 3 | 4 -> "small"
    _ -> "large"
  }
}

fn make_adder(n: Int) -> fn(Int) -> Int {
  fn(k) { n + k }
}

fn combine(x: Int, y: Int, z: Int, f: fn(Int, Int) -> Int) -> Int {
  f(f(x, y), z)
}

fn sum_first_n(n) {
  sum_from(n, 1, 0)
}

fn sum_from(n, k, total) {
  case k > n {
    True -> total
    False -> sum_from(n, k + 1, total + k)
  }
}

fn fact_tail(n) {
  fact_iter(n, 1)
}

fn fact_iter(n, product) {
  case n {
    0 -> product
    _ -> fact_iter(n - 1, n * product)
  }
}

fn fib(n) {
  fib_iter(1, 0, n)
}

fn fib_iter(prev, curr, steps) {
  case steps {
    0 -> curr
    _ -> fib_iter(curr, prev + curr, steps - 1)
  }
}
