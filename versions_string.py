"""Version string processing and sorting utility.

This module provides functionality to clean, normalize, and sort version strings
from git repositories or other sources.
"""

import functools
import re
import sys
from enum import Enum


class SpecialVersion(Enum):
    """Special version identifiers."""

    CURRENT = "current"


# Git-related strings to remove during cleaning
GIT_PREFIXES_TO_REMOVE = {
    "origin/": "",
    "origin": "",
    "HEAD": "",
    "gh-pages": "",
    "main": SpecialVersion.CURRENT.value,
}

VERSION_PATTERN = re.compile(rf"^(?:{SpecialVersion.CURRENT.value}|\d+\.\d+)$")


def normalize_version(version_parts: list[str]) -> tuple[int, int, int]:
    """Normalize version parts for easier comparison.

    Parameters
    ----------
    version_parts : list[str]
        List of version components as strings

    Returns
    -------
    tuple[int, int, int]
        Tuple of (major, minor, patch) as integers

    Examples
    --------
    >>> normalize_version(["1", "2"])
    (1, 2, 0)
    >>> normalize_version(["1", "2", "3", "4"])
    (1, 2, 3)
    """
    normalized: list[int] = []

    # Convert to integers, treating non-numeric parts as 0
    for part in version_parts:
        try:
            normalized.append(int(part))
        except ValueError:
            # Non-numeric strings are treated as 0 for comparison
            normalized.append(0)

    # Ensure exactly 3 components (major, minor, patch)
    while len(normalized) < 3:
        normalized.append(0)

    return tuple(normalized[:3])


def compare_versions(version_a: str, version_b: str) -> int:
    """Compare two version strings using semantic version ordering.

    Special handling for 'current' version which is treated as the highest version.

    Parameters
    ----------
    version_a : str
        First version string
    version_b : str
        Second version string

    Returns
    -------
    int
        -1 if version_a < version_b, 0 if equal, 1 if version_a > version_b

    Examples
    --------
    >>> compare_versions("1.2.3", "1.2.4")
    -1
    >>> compare_versions("current", "1.0.0")
    1
    """
    # Handle special "current" version - it's always the highest
    if version_a == SpecialVersion.CURRENT.value:
        return 0 if version_b == SpecialVersion.CURRENT.value else 1
    if version_b == SpecialVersion.CURRENT.value:
        return -1

    # Compare normalized versions using Python's tuple comparison
    normalized_a = normalize_version(version_a.split("."))
    normalized_b = normalize_version(version_b.split("."))

    # Use Python's built-in comparison for tuples
    if normalized_a < normalized_b:
        return -1
    elif normalized_a > normalized_b:
        return 1
    else:
        return 0


def clean_version_string(raw_versions: str) -> str:
    """Clean and normalize raw version string by removing git-specific prefixes.

    Parameters
    ----------
    raw_versions : str
        Raw version string from git or other source

    Returns
    -------
    str
        Cleaned version string with normalized whitespace

    Examples
    --------
    >>> clean_version_string("origin/main  origin/1.0.0  HEAD")
    "current 1.0.0"
    """
    cleaned = raw_versions

    # Apply all replacements from the mapping
    for old_string, new_string in GIT_PREFIXES_TO_REMOVE.items():
        cleaned = cleaned.replace(old_string, new_string)

    # Normalize whitespace: replace multiple spaces with single space
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    return cleaned


def format_versions_string(versions: str) -> str:
    """Format and sort version strings for display.

    Parameters
    ----------
    versions : str
        Space-separated string of version names

    Returns
    -------
    str
        Comma-separated string of sorted versions (newest first)

    Examples
    --------
    >>> format_versions_string("1.0.0 2.0.0 current")
    "current,2.0.0,1.0.0"

    Notes
    -----
    This function also prints the result to stdout as a side effect.
    """
    cleaned_versions = clean_version_string(versions)

    if not cleaned_versions:
        return ""

    # Split into individual versions, filtering out empty strings
    version_list = [version for version in cleaned_versions.split() if version]

    # Keep only supported version labels (current or x.y)
    version_list = [version for version in version_list if VERSION_PATTERN.match(version)]

    if not version_list:
        return ""

    # Sort versions using custom comparison function
    sorted_versions = sorted(version_list, key=functools.cmp_to_key(compare_versions))

    # Reverse to get newest first, then join with commas
    result = ",".join(reversed(sorted_versions))

    print(result)
    return result


def main() -> str:
    """Main function to read from stdin and process versions.

    Returns
    -------
    str
        Formatted version string, or empty string on error
    """
    try:
        versions = sys.stdin.read().strip()
        if not versions:
            print("Warning: No input received from stdin", file=sys.stderr)
            return ""

        return format_versions_string(versions)

    except Exception as e:
        print(f"Unexpected error processing versions: {e}", file=sys.stderr)
        return ""


if __name__ == "__main__":
    main()
