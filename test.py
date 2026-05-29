from pathlib import Path
import argparse

   
def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def sum_primes_up_to(limit: int) -> int:
    """Return the sum of all primes up to and including the limit."""
    return sum(n for n in range(2, limit + 1) if is_prime(n))


def write_primes(limit: int, output_path: Path) -> None:
    """Write all prime numbers up to the limit into a text file."""
    primes = [str(n) for n in range(2, limit + 1) if is_prime(n)]
    output_path.write_text("\n".join(primes), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Berechne Primzahlen und speichere das Ergebnis in einer Datei."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Obergrenze für die Primzahlsumme",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("primes.txt"),
        help="Zieldatei für die Primzahlen",
    )
    args = parser.parse_args()

    total = sum_primes_up_to(args.limit)
    write_primes(args.limit, args.output)

    print(f"Summe der Primzahlen bis {args.limit}: {total}")
    print(f"Primzahlen geschrieben nach: {args.output}")


if __name__ == "__main__":
    main()
