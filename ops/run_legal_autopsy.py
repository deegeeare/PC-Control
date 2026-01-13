import json
import os
import sys

# Ensure imports work
sys.path.append(os.getcwd())

from core.clo.adversary import AdversarialAuditor

def run_legal_autopsy():
    print("INITIALIZING CLO AUTOPSY: Vetoed Energy Project")

    # 1. Load Vetoed Audit Artifact (to get memo path)
    audit_path = "memory/treasury/audit_001.json"
    if not os.path.exists(audit_path):
        print("Error: Treasury Audit artifact not found.")
        return

    with open(audit_path, 'r') as f:
        audit_data = json.load(f)

    memo_path = audit_data.get("credit_memo_path")
    if not memo_path or not os.path.exists(memo_path):
        print("Error: Credit Memo artifact not found.")
        return

    # 2. Read Credit Memo
    with open(memo_path, 'r') as f:
        memo_content = f.read()

    # 3. Initialize CLO
    clo = AdversarialAuditor()

    # 4. Perform Autopsy
    autopsy = clo.perform_autopsy(memo_content, context="Vetoed Credit Memo")

    # 5. Save Legal Brief
    legal_brief = {
        "target_document": memo_path,
        "veto_context": "Project Vetoed by CFO (ROI 0.11)",
        "autopsy_results": autopsy,
        "clo_recommendation": "SUSTAIN_VETO. Proceeding would have triggered TRAIGA non-compliance penalties."
    }

    output_path = "memory/legal/audit_001_v2.json"
    with open(output_path, 'w') as f:
        json.dump(legal_brief, f, indent=2)

    print(f"Legal Autopsy Complete. Saved to {output_path}")
    print(json.dumps(legal_brief, indent=2))

if __name__ == "__main__":
    run_legal_autopsy()
