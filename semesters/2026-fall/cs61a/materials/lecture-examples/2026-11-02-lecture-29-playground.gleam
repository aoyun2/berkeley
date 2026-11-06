import gleam/dict
import gleam/int
import gleam/list
import gleam/string

pub fn main() {
  echo repeating([1, 2, 3, 1, 2, 3, 1], 3)
  echo repeating([1, 2, 1, 2], 2)
  echo repeating([4, 4, 4], 1)
  echo repeating([1, 2], 3)
  echo repeating([1, 2, 3, 1, 3, 2], 3)
  echo repeating([1, 2, 1, 2], 3)

  echo matches([1, 2, 3], [1, 2, 3])
  echo matches([1, 2, 1, 2], [1, 2])
  echo matches([1, 2], [1, 2, 3, 4])
  echo matches([], [1, 2])
  echo matches([1, 2, 3], [1, 3])

  echo list.try_map(["1", "2", "3"], int.parse)
  echo list.try_map(["1", "two", "3"], int.parse)

  let s = Link(1, Link(3, Last(5)))
  echo starts_with(s, 1)
  echo starts_with(s, 3)
  echo increasing(Last(4))
  echo increasing(s)
  echo increasing(Link(1, Link(4, Link(2, Last(5)))))
  echo increasing(Link(3, Last(2)))

  echo wrong_increasing(s)
  echo wrong_increasing(Link(1, Link(4, Link(2, Last(5)))))
  echo wrong_increasing(Link(3, Last(2)))
  echo wrong_increasing(Link(1, Link(3, Last(2))))

  let t = Tree(1, [Tree(2, [leaf(3), leaf(4)]), leaf(5)])
  echo remove_leaf(t)
  echo remove_leaf(remove_leaf(t))
  echo remove_leaf(remove_leaf(remove_leaf(t)))
  echo remove_leaf(leaf(6))

  let sqrt = invert(fn(x) { x * x }, countdown(100))
  echo sqrt(0)
  echo sqrt(49)
  echo sqrt(50)
  echo sqrt(1_000_000)
  echo sqrt(81)

  echo first_int([5, 6, 7])
  echo first_int([])
  echo nth_int([5, 6, 7], 0)
  echo nth_int([5, 6, 7], 2)
  echo nth_int([5, 6, 7], 3)
  echo nth_int([], 0)

  echo nth_using_first([5, 6, 7], 0)
  echo nth_using_first([5, 6, 7], 2)
  echo nth_using_first([5, 6, 7], 3)
  echo nth_using_first([], 0)
  echo nth_using_first([5, 6, 7], -1)
  echo nth_using_first(["a", "b", "c"], 1)

  echo nth([5, 6, 7], 0)
  echo nth([5, 6, 7], 2)
  echo nth([5, 6, 7], 3)
  echo nth([], 0)
  echo nth([5, 6, 7], -1)
  echo nth(["a", "b", "c"], 1)

  echo fib(0)
  echo fib(1)
  echo fib(10)
  echo fib(25)
  echo fib_fast(10)
  echo fib_fast(90)
  echo fib_memoized(5, dict.from_list([#(0, 0), #(1, 1)]))
}

fn first_int(s: List(Int)) -> Int {
  case s {
    [] -> 0
    [x, ..] -> x
  }
}

fn nth_int(s: List(Int), n: Int) -> Int {
  case list.first(list.drop(s, n)) {
    Ok(k) -> k
    Error(Nil) -> 0
  }
}

fn nth_using_first(s: List(a), n: Int) -> Result(a, Nil) {
  list.first(list.drop(s, n))
}

fn nth(s: List(a), n: Int) -> Result(a, Nil) {
  case s, n {
    [], _ -> Error(Nil)
    _, _ if n < 0 -> Error(Nil)
    [x, ..], 0 -> Ok(x)
    [_, ..rest], _ -> nth(rest, n - 1)
  }
}

/// Whether s is n items repeating; for n==3: [x, y, z, x, y, z, ...]
pub fn repeating(s: List(a), n: Int) -> Bool {
  matches(s, drop(s, n))
}

/// Remove up to the first n items of s
fn drop(s: List(a), n: Int) -> List(a) {
  case n {
    0 -> s
    _ ->
      case s {
        [] -> []
        [_, ..rest] -> drop(rest, n - 1)
      }
  }
}

/// Whether s and t are equal or one is a prefix of the other
fn matches(s: List(a), t: List(a)) -> Bool {
  case s, t {
    [x, ..s_rest], [y, ..t_rest] -> x == y && matches(s_rest, t_rest)
    _, _ -> True
  }
}

/// The nth Fibonacci number.
pub fn fib(n: Int) -> Int {
  case n {
    0 | 1 -> n
    _ -> fib(n - 2) + fib(n - 1)
  }
}

/// A dictionary of each Fibonacci number found so far, keyed by its index.
pub type Cache =
  dict.Dict(Int, Int)

pub fn fib_fast(n: Int) -> Int {
  fib_memoized(n, dict.from_list([#(0, 0), #(1, 1)])).0
}

/// The nth Fibonacci number, found using the cache, along with a cache that also
/// contains every Fibonacci number found along the way.
pub fn fib_memoized(n: Int, cache: Cache) -> #(Int, Cache) {
  case dict.get(cache, n) {
    Ok(fib_n) -> #(fib_n, cache)
    Error(Nil) -> {
      let #(a, cache) = fib_memoized(n - 2, cache)
      let #(b, cache) = fib_memoized(n - 1, cache)
      #(a + b, dict.insert(cache, n, a + b))
    }
  }
}

pub type NotEmpty(a) {
  Last(first: a)
  Link(first: a, rest: NotEmpty(a))
}

pub fn starts_with(s: NotEmpty(a), v: a) -> Bool {
  s.first == v
}

pub fn wrong_increasing(s: NotEmpty(Int)) -> Bool {
  case s {
    Last(_) -> True
    Link(first, Link(second, _)) if second <= first -> False
    Link(_, rest) -> wrong_increasing(rest)
  }
}

pub fn increasing(s: NotEmpty(Int)) -> Bool {
  case s {
    Last(_) -> True
    Link(first, rest) -> rest.first > first && increasing(s.rest)
  }
}

pub type Tree(a) {
  Tree(label: a, branches: List(Tree(a)))
}

pub fn leaf(label: a) -> Tree(a) {
  Tree(label, [])
}

/// A new tree without its leftmost leaf; a tree that is a leaf is unchanged
pub fn remove_leaf(tree: Tree(a)) -> Tree(a) {
  case tree {
    Tree(label, [Tree(_, []), ..rest]) -> Tree(label, rest)
    Tree(label, [first, ..rest]) -> Tree(label, [remove_leaf(first), ..rest])
    Tree(_, []) -> tree
  }
}

/// Integers from n down to 0
pub fn countdown(n: Int) {
  case n {
    0 -> [0]
    _ -> [n, ..countdown(n - 1)]
  }
}

/// Return a function that is the inverse of f: f(invert(f, _)(x)) == x
pub fn invert(f: fn(a) -> b, inputs: List(a)) -> fn(b) -> Result(a, Nil) {
  let inverse = dict.from_list(list.map(inputs, fn(x) { #(f(x), x) }))
  fn(x) { dict.get(inverse, x) }
}
