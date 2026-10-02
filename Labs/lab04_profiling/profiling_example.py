import numpy as np

# When run with `kernprof -l -v`, `profile` is provided automatically.
# This fallback lets the file also run normally with plain `python`.
try:
    profile
except NameError:
    def profile(func):
        return func


@profile
def calculate_statistics(x):
    total = np.sum(x)
    mean = np.mean(x)
    variance = np.var(x)
    result = np.sqrt(variance)
    return total, mean, result


if __name__ == "__main__":
    np.random.seed(0)
    data = np.random.normal(size=1_000_000)
    print(calculate_statistics(data))
