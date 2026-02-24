import sys
import re
import functools

# Normalize version for easier comparison
def normalize(version):
    normalized = []
    # Cast to int to avoid "10" < "2"
    for v in version:
        try:
            normalized.append(int(v))
        except:
            # Actual strings are not handled
            normalized.append(-1)

    # Add minor and patch versions as 0 if missing 
    while len(normalized) < 3:
        normalized.append(0)

    return normalized

def compare_versions(a, b):
    if a == "current":
        return 1
    if b == "current":
        return -1

    a_ = normalize(a.split("."))
    b_ = normalize(b.split("."))

    if a_[0] == b_[0]:
        if a_[1] == b_[1]:
            if a_[2] < b_[2]:
                return -1
            return 1
        if a_[1] < b_[1]:
            return -1
        return 1
    if a_[0] < b_[0]:
        return -1
    return 1

def format_versions_string(versions):
    s = versions.replace("origin/", "").replace("origin", "").replace("HEAD", "").replace("gh-pages", "").replace("main", "current")
    s = re.sub(" +", " ", s).strip()

    sa = sorted(s.split(" "), key=functools.cmp_to_key(compare_versions))
    s = ",".join(list(reversed(sa))[:4])

    print(s)
    return s

def main():
    versions = sys.stdin.read()
    return(format_versions_string(versions))

if __name__ == "__main__":
    main()