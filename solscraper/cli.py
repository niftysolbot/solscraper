"""Console script for solscraper."""
import argparse
import sys

from solscraper.solscraper_base import entrypoint


def main():
    """Console script for solscraper."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("SOL Scraper has started")

    entrypoint(args._)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
