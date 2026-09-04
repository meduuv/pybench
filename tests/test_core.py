import unittest

from pybench import BenchmarkResult, benchmark


class TestCore(unittest.TestCase):
    def test_benchmark(self):
        result = benchmark(lambda: 1 + 1, iterations=10)
        self.assertIsInstance(result, BenchmarkResult)
        self.assertEqual(result.iterations, 10)
        self.assertGreaterEqual(result.elapsed, 0)
        self.assertGreaterEqual(result.per_call, 0)

    def test_invalid_iterations(self):
        with self.assertRaises(ValueError):
            benchmark(lambda: None, iterations=0)


if __name__ == "__main__":
    unittest.main()
