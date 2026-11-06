import gleam/int
import gleam/list
import gleam/string

pub fn main() {
  echo count_all_partitions(5)
  echo double_each([3, 4, 5, 6])
  echo describe([])
  echo describe([1])
  echo describe([2])
  echo describe([4, 5, 6])
  echo describe([3, 5, 6, 7])
  echo describe([3, 5])
  echo describe([5, 3, 6])

  echo alternating([])
  echo alternating([1, 2, 1, 2, 1])
  echo alternating(["a", "b", "a", "b"])
  echo alternating([1, 2, 1, 3])
  echo alternating([1, 2, 2, 1])

  echo repeating([1, 2, 3, 1, 2, 3, 1], 3)
  echo repeating([1, 2, 1, 2], 2)
  echo repeating([4, 4, 4], 1)
  echo repeating([1, 2], 3)
  echo repeating([1, 2, 3, 1, 3, 2], 3)
  echo repeating([1, 2, 1, 2], 3)

  echo repeating2([1, 2, 3, 1, 2, 3, 1], 3)
  echo repeating2([1, 2, 1, 2], 2)
  echo repeating2([4, 4, 4], 1)
  echo repeating2([1, 2], 3)
  echo repeating2([1, 2, 3, 1, 3, 2], 3)
  echo repeating2([1, 2, 1, 2], 3)

  echo matches([1, 2, 3], [1, 2, 3])
  echo matches([1, 2, 1, 2], [1, 2])
  echo matches([1, 2], [1, 2, 3, 4])
  echo matches([], [1, 2])
  echo matches([1, 2, 3], [1, 3])

  echo show(#(3, 4))
  echo show(#(5, 1))
  echo show(#(2, 0))

  echo contact(User("Oski", EmailOnly("oski@berkeley.edu")))

  let t = Tree(1, [Tree(2, [leaf(3), leaf(4)]), Tree(5, [leaf(6)])])
  echo t
  echo sum_labels(t)

  echo sum_nested([])
  echo sum_nested([Item(1), Item(2), Item(3)])
  echo sum_nested([Item(1), Sublist([Item(2), Sublist([Item(3), Item(4)])])])
  echo sum_nested([Item(2), Sublist([Item(3), Item(4)]), Sublist([]), Item(5)])

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
}

fn double_each(s: List(Int)) -> List(Int) {
  list.map(s, fn(n) { 2 * n })
}

fn describe(s: List(Int)) -> String {
  case s {
    [] -> "Empty list"
    [1] -> "List of just 1"
    [4, ..] -> "List starting with 4"
    [a, b] if a < b ->
      "List of " <> int.to_string(a) <> " then " <> int.to_string(b)
    [_, _] -> "List of two elements"
    [a, b, ..rest] if a < b -> "List ending in " <> string.inspect(rest)
    _ -> "Some other list"
  }
}

pub fn sorted(s: List(Int)) -> Bool {
  case s {
    [] | [_] -> True
    [first, second, ..rest] -> first <= second && sorted([second, ..rest])
  }
}

pub fn sorted_tail(s: List(Int)) -> Bool {
  case s {
    [] | [_] -> True
    [first, second, ..] if first > second -> False
    [_, ..rest] -> sorted_tail(rest)
  }
}

/// Whether s is a pair of alternating items [x, y, x, y, x, ...]
pub fn alternating(s: List(a)) -> Bool {
  case s {
    [] | [_] | [_, _] -> True
    [x, _, z, ..] if x != z -> False
    [_, ..rest] -> alternating(rest)
  }
}

/// Whether s is n items repeating; for n==3: [x, y, z, x, y, z, ...]
pub fn repeating(s: List(a), n: Int) -> Bool {
  case s {
    [] -> True
    [first, ..rest] -> nth_equals(first, s, n) && repeating(rest, n)
  }
}

/// Return True if s is shorter than n or s[n] == expected
pub fn nth_equals(expected: a, s: List(a), n: Int) -> Bool {
  case s {
    [] -> True
    [first, ..rest] ->
      case n {
        0 -> first == expected
        _ -> nth_equals(expected, rest, n - 1)
      }
  }
}

/// Whether s is n items repeating; for n==3: [x, y, z, x, y, z, ...]
pub fn repeating2(s: List(a), n: Int) -> Bool {
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

/// Return a fraction (numerator, denominator) as a string
fn show(f: #(Int, Int)) -> String {
  case f {
    #(_, 0) -> "undefined"
    #(n, 1) -> int.to_string(n)
    #(n, d) -> int.to_string(n) <> "/" <> int.to_string(d)
  }
}

pub type Contact {
  EmailOnly(email: String)
  PhoneOnly(phone: Int)
  Both(email: String, phone: Int)
}

pub type User {
  User(name: String, contact: Contact)
}

pub fn contact(user: User) -> String {
  case user.contact {
    EmailOnly(e) | Both(e, _) -> "mailto:" <> e
    PhoneOnly(number) -> "tel:" <> int.to_string(number)
  }
}

// Tree
pub type Tree(a) {
  Tree(label: a, branches: List(Tree(a)))
}

// Create a leaf
pub fn leaf(label: a) -> Tree(a) {
  Tree(label, [])
}

/// Return the sum of the labels in a tree of integers
pub fn sum_labels(t: Tree(Int)) -> Int {
  t.label + int.sum(list.map(t.branches, sum_labels))
}

fn count_all_partitions(n: Int) -> Int {
  count_partitions(n, n)
}

/// Count the ways of summing to n using parts up to m.
fn count_partitions(n: Int, m: Int) -> Int {
  case n {
    0 -> 1
    _ if n < 0 || m == 0 -> 0
    _ -> count_partitions(n - m, m) + count_partitions(n, m - 1)
  }
}

// E.g., a nested list of integers is a list containing integers and nested lists of integers
pub type NestedList(a) =
  List(Nested(a))

// An item in a nested list
pub type Nested(a) {
  Sublist(NestedList(a))
  Item(a)
}

// Sum a nested list of integers
pub fn sum_nested(s: NestedList(Int)) -> Int {
  case s {
    [] -> 0
    [first, ..rest] ->
      case first {
        Sublist(t) -> sum_nested(t)
        Item(a) -> a
      }
      + sum_nested(rest)
  }
}

pub fn sum_nested2(s: NestedList(Int)) -> Int {
  int.sum(
    list.map(s, fn(x) {
      case x {
        Sublist(t) -> sum_nested(t)
        Item(a) -> a
      }
    }),
  )
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
