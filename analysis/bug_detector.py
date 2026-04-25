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