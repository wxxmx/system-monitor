import subprocess

def analyze_logs():
    findings = {
        "errors": 0,
        "warnings": 0,
        "auth_events": 0
    }

    try:
        command = [
            "log", "show",
            "--predicate", '(eventMessage CONTAINS[c] "error" OR eventMessage CONTAINS[c] "warning" OR eventMessage CONTAINS[c] "authentication")',
            "--last", "1h"
        ]

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        for line in result.stdout.splitlines():
            lower = line.lower()
            if "error" in lower:
                findings["errors"] += 1
            if "warning" in lower:
                findings["warnings"] += 1
            if "auth" in lower:
                findings["auth_events"] += 1

    except Exception as e:
        print(f"[!] Log analysis failed: {e}")

    return findings
