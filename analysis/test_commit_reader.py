from pydriller import Repository
from bug_detector import detect_none_issues, detect_exception_issues

repo_path = "repos/fastapi"

commits = list(Repository(repo_path).traverse_commits())

n = len(commits)

early = commits[:n//3]
middle = commits[n//3:2*n//3]
late = commits[2*n//3:]


def analyze_phase(commits):
    none_count = 0
    exception_count = 0

    for commit in commits:
        for mod in commit.modified_files:
            if mod.source_code:
                none_count += detect_none_issues(mod.source_code)
                exception_count += detect_exception_issues(mod.source_code)

    return none_count, exception_count


# Analyze all phases
early_none, early_exc = analyze_phase(early)
middle_none, middle_exc = analyze_phase(middle)
late_none, late_exc = analyze_phase(late)


print("EARLY:", early_none, early_exc)
print("MIDDLE:", middle_none, middle_exc)
print("LATE:", late_none, late_exc)