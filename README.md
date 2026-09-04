# pybench

A tiny dependency-free benchmarking helper for comparing Python callables.

## Features

- Repeat a callable with a configurable iteration count
- Report elapsed time and per-call timing
- Return structured benchmark results
- No runtime dependencies

## Usage

```python
from pybench import benchmark

result = benchmark(lambda: sum(range(100)), iterations=1000)
print(result)
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

https://guns.lol/meduu
