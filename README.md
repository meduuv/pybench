# pybench

A tiny standard-library benchmarking helper for comparing callable runtimes.

## Features

- Repeated callable timing
- Warm-up support
- Min, max, mean, and median measurements
- JSON-friendly benchmark results

## Usage

```python
from pybench import benchmark

result = benchmark(lambda: sum(range(1000)), repeats=20)
print(result.mean_seconds)
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

https://guns.lol/meduu
