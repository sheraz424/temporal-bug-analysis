from pydriller import Repository
import csv

# ---------------------------
# BUG DETECTORS
# ---------------------------
def detect_none_issues(code):
    issues = 0
    if "== None" in code:
        issues += 1
    if "is None" in code:
        issues += 1
    return issues

def detect_exception_issues(code):
    issues = 0
    if "except:" in code:
        issues += 1
    if "except Exception" in code:
        issues += 1
    return issues

# ---------------------------
# LOC COUNTER
# ---------------------------
def count_loc(code):
    if not code:
        return 0
    return len([line for line in code.split("\n") if line.strip()])


# ---------------------------
# MAIN ANALYSIS FUNCTION
# ---------------------------
def analyze_repo(repo_path, repo_name):
    print("\nAnalyzing:", repo_name)

    try:
        commits = list(Repository(
            repo_path,
            only_no_merge=True,
            only_modifications_with_file_types=['.py']
        ).traverse_commits())[:1000]   # LIMIT for performance

    except Exception as e:
        print("Repo load error:", e)
        return None

    if not commits:
        print("No commits found.")
        return None

    n = len(commits)

    early = commits[:n//3]
    middle = commits[n//3:2*n//3]
    late = commits[2*n//3:]

    def process_phase(commits_subset):
        none_count = 0
        exc_count = 0
        loc_count = 0

        for commit in commits_subset:
            try:
                for mod in commit.modified_files:
                    if mod.source_code and mod.filename.endswith(".py"):
                        code = mod.source_code

                        none_count += detect_none_issues(code)
                        exc_count += detect_exception_issues(code)
                        loc_count += count_loc(code)

            except Exception:
                continue  # skip problematic commits safely

        none_density = (none_count / loc_count * 1000) if loc_count else 0
        exc_density = (exc_count / loc_count * 1000) if loc_count else 0

        return round(none_density, 2), round(exc_density, 2)

    # Run phases
    early_none, early_exc = process_phase(early)
    middle_none, middle_exc = process_phase(middle)
    late_none, late_exc = process_phase(late)

    # PRINT RESULTS
    print("NONE DENSITY (per KLOC)")
    print("EARLY:", early_none)
    print("MIDDLE:", middle_none)
    print("LATE:", late_none)

    print("EXCEPTION DENSITY (per KLOC)")
    print("EARLY:", early_exc)
    print("MIDDLE:", middle_exc)
    print("LATE:", late_exc)

    return [
        repo_name,
        early_none, middle_none, late_none,
        early_exc, middle_exc, late_exc
    ]


# ---------------------------
# REPOSITORY LIST
# ---------------------------
repos = [
    ("repos/fastapi", "fastapi"),
    ("repos/black", "black"),
    ("repos/click", "click"),
    ("repos/pytest", "pytest"),
    ("repos/scrapy", "scrapy"),
    ("repos/tern", "tern"),
    ("repos/typer", "typer"),
    ("repos/RecoverPy", "RecoverPy"),
    ("repos/Name-That-Hash", "Name-That-Hash"), 
]


# ---------------------------
# RUN ALL
# ---------------------------
results = []

for path, name in repos:
    try:
        result = analyze_repo(path, name)
        if result:
            results.append(result)
    except Exception as e:
        print("Error in", name, ":", e)


# ---------------------------
# SAVE RESULTS TO CSV
# ---------------------------
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Repo",
        "Early_None",
        "Middle_None",
        "Late_None",
        "Early_Exception",
        "Middle_Exception",
        "Late_Exception"
    ])
    writer.writerows(results)

print("\n✅ Results saved to results.csv")