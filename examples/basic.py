"""Minimal example for RetryLib."""

from retrylib import retrylib


def main():
 runner = retrylib({"name": "RetryLib", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()