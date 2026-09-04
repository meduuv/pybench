from dataclasses import dataclass
from time import perf_counter
from typing import Callable, Any


@dataclass(frozen=True)
class BenchmarkResult:
    iterations: int
    elapsed: float

    @property
    def per_call(self) -> float:
        return self.elapsed / self.iterations


def benchmark(function: Callable[[], Any], iterations: int = 1000) -> BenchmarkResult:
    if iterations <= 0:
        raise ValueError("iterations must be positive")
    start = perf_counter()
    for _ in range(iterations):
        function()
    return BenchmarkResult(iterations, perf_counter() - start)
