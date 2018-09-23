import unittest
from collections import Iterable, Sequence
from collections import Iterator, Generator

try:
    from sol_range import Range, RangeIterator
except (ModuleNotFoundError, ImportError):
    from range import Range, RangeIterator


class Int:

    def __init__(self, value):
        self.value = int(value)

    def __int__(self):
        return self.value


class TestRange(unittest.TestCase):

    def test_init(self):
        r = Range(2, 100, 5)
        self.assertTrue(hasattr(r, "start"))
        self.assertTrue(hasattr(r, "stop"))
        self.assertTrue(hasattr(r, "step"))

        exp = range(2, 100, 5)
        self.assertEqual(r.start, exp.start)
        self.assertEqual(r.stop, exp.stop)
        self.assertEqual(r.step, exp.step)

        with self.assertRaises(TypeError) as e:
            Range(1, 0.0, "a")
        with self.assertRaises(TypeError) as exp:
            range(1, 0.0, "a")
        self.assertEqual(e.exception.args, exp.exception.args)

        with self.assertRaises(TypeError) as e:
            Range("a", 0.0, 0)
        with self.assertRaises(TypeError) as exp:
            range("a", 0.0, 0)
        self.assertEqual(e.exception.args, exp.exception.args)

        with self.assertRaises(ValueError) as e:
            Range(1, 0, 0)
        with self.assertRaises(ValueError) as exp:
            range(1, 0, 0)
        self.assertEqual(e.exception.args, exp.exception.args)

        with self.assertRaises(TypeError) as e:
            Range(1, 0, 0, 0)
        with self.assertRaises(TypeError) as exp:
            range(1, 0, 0, 0)
        self.assertEqual(e.exception.args, exp.exception.args)

    def test_str(self):
        self.assertEqual(str(Range(10)), str(range(10)))
        self.assertEqual(str(Range(101)), str(range(101)))
        self.assertEqual(str(Range(10, 20)), str(range(10, 20)))
        self.assertEqual(str(Range(1, 3, 1)), str(range(1, 3, 1)))
        self.assertEqual(str(Range(1, 3, 10)), str(range(1, 3, 10)))
        self.assertEqual(str(Range(10, -1, -1)), str(range(10, -1, -1)))
        self.assertEqual(repr(Range(10, -1, -1)), repr(range(10, -1, -1)))
        self.assertEqual(repr(Range(10)), repr(range(10)))
        self.assertEqual(repr(Range(101)), str(range(101)))
        self.assertEqual(repr(Range(10, 20)), repr(range(10, 20)))
        self.assertEqual(repr(Range(1, 3, 1)), repr(range(1, 3, 1)))
        self.assertEqual(repr(Range(1, 3, 10)), repr(range(1, 3, 10)))
        self.assertEqual(repr(Range(10, -1, -1)), repr(range(10, -1, -1)))

    def test_iterable(self):
        self.assertTrue(issubclass(RangeIterator, Iterator))
        self.assertTrue(issubclass(Range, Iterable))
        self.assertTrue(issubclass(Range, Sequence))

        r = Range(2, 10, 5)
        self.assertTrue(isinstance(r, Iterable))
        self.assertTrue(isinstance(r, Sequence))
        self.assertFalse(isinstance(iter(r), Generator))
        self.assertTrue(isinstance(iter(r), Iterator))
        self.assertTrue(isinstance(RangeIterator(r), Iterator))
        self.assertFalse(isinstance(RangeIterator(r), Generator))

    def test_range(self):
        self.assertEqual(list(Range(10)), list(range(10)))
        self.assertEqual(list(Range(5, 10)), list(range(5, 10)))
        self.assertEqual(list(Range(5, 100, 2)), list(range(5, 100, 2)))
        self.assertEqual(list(Range(-5, -19, -2)), list(range(-5, -19, -2)))
        self.assertEqual(
            list(Range(100, -100, -11)), list(range(100, -100, -11))
        )
        self.assertEqual(list(Range(-9)), list(range(-9)))

    def test_len(self):
        self.assertEqual(len(Range(10)), len(range(10)))
        self.assertEqual(len(Range(5, 10)), len(range(5, 10)))
        self.assertEqual(len(Range(5, 100, 3)), len(range(5, 100, 3)))
        self.assertEqual(len(Range(5, 100, 2)), len(range(5, 100, 2)))
        self.assertEqual(len(Range(-5, -19, -2)), len(range(-5, -19, -2)))
        self.assertEqual(
            len(Range(100, -100, -10)), len(range(100, -100, -10))
        )
        self.assertEqual(len(Range(-10)), len(range(-10)))
        self.assertEqual(
            len(Range(100, -100, -11)), len(range(100, -100, -11))
        )
        self.assertEqual(
            len(Range(100, -100, -33)), len(range(100, -100, -33))
        )

    def test_eq(self):
        self.assertEqual(Range(1, 2, 3), Range(1, 2, 3))
        self.assertEqual(Range(-100), Range(-100))
        self.assertEqual(Range(5, 10), Range(5, 10))

        self.assertNotEqual(Range(5, 10), slice(5, 10))
        self.assertNotEqual(Range(10), slice(10))
        self.assertNotEqual(Range(5, 10), range(5, 10))
        self.assertNotEqual(Range(10), range(20))

    def test_iter(self):
        self.assertEqual(list(iter(Range(9))), list(iter(range(9))))
        self.assertEqual(
            list(iter(Range(9, 1, 2))), list(iter(range(9, 1, 2)))
        )
        self.assertEqual(
            list(iter(Range(9, 12, 1))), list(iter(range(9, 12, 1)))
        )
        self.assertEqual(
            list(iter(Range(-9, -100, -5))), list(iter(range(-9, -100, -5)))
        )
        r = Range(-9)
        self.assertNotEqual(iter(r), iter(iter(r)))
        self.assertEqual(id(iter(r)), id(iter(iter(r))))
        self.assertRaises(StopIteration, next, iter(r))

    def test_index(self):
        self.assertEqual(Range(3, 11, 2).index(9), range(3, 11, 2).index(9))
        self.assertEqual(Range(100).index(98), range(100).index(98))
        self.assertEqual(
            Range(5, -1000, -13).index(-216),
            range(5, -1000, -13).index(-216)
        )
        self.assertEqual(
            Range(19, 13333, 3).index(2713),
            range(19, 13333, 3).index(2713)
        )
        self.assertEqual(
            Range(19, 13333000, 3).index(37351.0),
            range(19, 13333000, 3).index(37351.0)
        )
        self.assertEqual(
            Range(101).index(float(100)),
            range(101).index(float(100))
        )

        with self.assertRaises(ValueError) as e:
            Range(3, 11, 2).index(11)
        with self.assertRaises(ValueError) as exp:
            range(3, 11, 2).index(11)
        self.assertEqual(e.exception.args, exp.exception.args)

        with self.assertRaises(ValueError) as e:
            Range(3, 11, 2).index("a")
        with self.assertRaises(ValueError) as exp:
            range(3, 11, 2).index("a")
        self.assertEqual(e.exception.args, exp.exception.args)

        with self.assertRaises(ValueError) as e:
            Range(3, 11, 2).index(Int(3))
        with self.assertRaises(ValueError) as exp:
            range(3, 11, 2).index(Int(3))
        self.assertEqual(e.exception.args, exp.exception.args)

    def test_count(self):
        self.assertEqual(Range(3, 11, 2).count(9), range(3, 11, 2).count(9))
        self.assertEqual(Range(100).count(98), range(100).count(98))
        self.assertEqual(
            Range(5, -1000, -13).count(-216),
            range(5, -1000, -13).count(-216)
        )
        self.assertEqual(
            Range(19, 13333, 3).count(2713),
            range(19, 13333, 3).count(2713)
        )
        self.assertEqual(
            Range(19, 13333000, 3).count(37351.0),
            range(19, 13333000, 3).count(37351.0)
        )
        self.assertEqual(
            Range(101).count(float(100)),
            range(101).count(float(100))
        )

        self.assertEqual(
            Range(101).count("a"),
            range(101).count("a")
        )
        self.assertEqual(
            Range(101).count([]),
            range(101).count([])
        )
        self.assertEqual(
            Range(101).count(-17),
            range(101).count(-17)
        )

    def test_contains(self):
        self.assertEqual(
            17 in Range(0, 18, 1),
            17 in range(0, 18, 1)
        )
        self.assertEqual(
            101 not in Range(101),
            101 not in range(101)
        )
        self.assertEqual(
            "a" not in Range(101),
            "a" not in range(101)
        )
        self.assertEqual(
            Int(2) not in Range(101),
            Int(2) not in range(101)
        )
        self.assertEqual(
            2713 in Range(19, 13333, 3),
            2713 in range(19, 13333, 3)
        )
        self.assertEqual(
            2714 not in Range(19, 13333, 3),
            2714 not in range(19, 13333, 3)
        )
        self.assertEqual(
            -216 in Range(5, -1000, -13),
            -216 in range(5, -1000, -13)
        )

    def test_getitem(self):
        self.assertEqual(Range(10)[0], range(10)[0])
        self.assertEqual(Range(10)[4], range(10)[4])
        self.assertEqual(Range(19, 13333, 3)[17], range(19, 13333, 3)[17])
        self.assertEqual(Range(19, 13333, 3)[31], range(19, 13333, 3)[31])
        self.assertEqual(Range(-10, -100, -1)[15], range(-10, -100, -1)[15])
        self.assertEqual(Range(-13, -113, -6)[11], range(-13, -113, -6)[11])

    def test_getitem_slice(self):
        # self.assertEqual(str(Range(10)[::-1]), str(range(10)[::-1]))
        # self.assertEqual(str(Range(10)[1:2:3]), str(range(10)[1:2:3]))
        self.assertEqual(str(Range(10)[1:6:3]), str(range(10)[1:6:3]))
        self.assertEqual(
            str(Range(19, 13333, 3)[17:50:3]),
            str(range(19, 13333, 3)[17:50:3])
        )
        self.assertEqual(
            str(Range(19, 13338, 3)[17:10001:3]),
            str(range(19, 13338, 3)[17:10001:3])
        )
        self.assertEqual(
            str(Range(19, 13333, 3)[31]), str(range(19, 13333, 3)[31])
        )
        # self.assertEqual(
        #     str(Range(-10, -100, -1)[::-11]), str(range(-10, -100, -1)[::-11])
        # )
        self.assertEqual(
            str(Range(-30, -2)[slice(2, 6, 3)]),
            str(range(-30, -2)[slice(2, 6, 3)])
        )
        self.assertEqual(
            str(Range(-13, -113, -6)[slice(2, 11, -3)]),
            str(range(-13, -113, -6)[slice(2, 11, -3)])
        )
        self.assertEqual(
            str(Range(-13, -113, -6)[slice(12, 33, 3)]),
            str(range(-13, -113, -6)[slice(12, 33, 3)])
        )
        # self.assertEqual(
        #     str(Range(-13, -113, -6)[-3:-10:-2]),
        #     str(range(-13, -113, -6)[-3:-10:-2])
        # )


if __name__ == "__main__":
    unittest.main()
