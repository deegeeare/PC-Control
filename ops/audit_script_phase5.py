import sys
import os

# Ensure we can import from core
sys.path.append(os.getcwd())

from core.cto_node import CTONode

def audit_files(files):
    cto = CTONode()
    print(f"--- CTO Auditing {len(files)} files ---")
    all_passed = True
    for filepath in files:
        if not os.path.exists(filepath):
             print(f"Skipping {filepath} (Not Found)")
             continue
        with open(filepath, 'r') as f:
            content = f.read()

        print(f"Auditing: {filepath}")
        passed = cto.audit_code(content)
        if not passed:
            print(f"FAILED: {filepath}")
            all_passed = False
        else:
            print(f"PASSED: {filepath}")

    if all_passed:
        print("--- All files passed Resonance Check ---")
    else:
        print("--- Audit Failed ---")
        sys.exit(1)

if __name__ == "__main__":
    # Audit Phase 4 (CFO) and Phase 5 (CLO) files
    files_to_audit = [
        "core/ledger.py",
        "core/allocator.py",
        "core/cfo/vault.py",
        "core/cfo/registrar.py",
        "core/cfo/underwriter.py",
        "core/clo/adversary.py"
    ]
    audit_files(files_to_audit)
