from pytest_grader import points


@points(0)
def mutation_wwpd():
    """What Would Python Display?

    >>> x = [2, 3]
    >>> y = x
    >>> x.extend([4, 5])
    >>> x
    LOCKED: ad56d55c8b4e6f93
    >>> y
    LOCKED: dc060b03964c4f67

    >>> x = [2, 3]
    >>> y = x
    >>> x = x + [4, 5]
    >>> x
    LOCKED: 0a2f88c139ddf4dd
    >>> y
    LOCKED: cd54972ad5e1a7a0

    >>> s1 = [1, 2, 3]
    >>> s2 = s1
    >>> s1 is s2
    LOCKED: aaa2c9be8b84cffa
    >>> s2.extend([5, 6])
    >>> s1[4]
    LOCKED: b2ee7ef75f2a8830
    >>> s1.append([-1, 0, 1])
    >>> s2[5]
    LOCKED: fa15444834e46ea6
    >>> s3 = s2[:]
    >>> s3.insert(3, s2.pop(3))
    >>> len(s1)
    LOCKED: f5a1a1381a8d8839
    >>> s1[4] is s3[6]
    LOCKED: c14ed961ab14858c
    >>> s3[s2[4][1]]
    LOCKED: 08fc693e5e3f72c5
    >>> s1[:3] is s2[:3]
    LOCKED: 62fe5fc0dc6bbba6
    >>> s1[:3] == s2[:3]
    LOCKED: 3eaf44ebc0514102
    >>> s1[4].append(2)
    >>> s3[6][3]
    LOCKED: c5bb927c37e67e58
    """
