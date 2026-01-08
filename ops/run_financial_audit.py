import json
import os
import sys

# Ensure imports work
sys.path.append(os.getcwd())

from core.ledger import BayesianLedger
from core.allocator import ExecutionAllocator
from core.cfo.underwriter import CreditUnderwriter
from core.cfo.registrar import AutonomousRegistrar
from core.cfo.vault import IdentityVault

def run_financial_audit():
    print("INITIALIZING FINANCIAL AUDIT: Energy Resilience Project")

    # 0. Load Phase 3 Artifact
    brief_path = "memory/intelligence_briefs/distilled_brief_001.json"
    if not os.path.exists(brief_path):
        print("Error: Phase 3 brief not found.")
        return

    with open(brief_path, 'r') as f:
        brief = json.load(f)

    # 1. Initialize Nodes
    ledger = BayesianLedger()
    allocator = ExecutionAllocator()
    underwriter = CreditUnderwriter()
    registrar = AutonomousRegistrar()

    # 2. Simulate Spending Scenario ($2M Burn)
    # The prompt asks to see how the Ledger handles a $2M burn vs current reserves.
    project_cost = 2000000.0

    # 2a. Update Ledger Burn Forecast
    # Assuming this project incurs a monthly burn of ~100k roughly?
    # Or is the 2M the CAPEX? Let's treat 2M as total cost, amortized monthly for the update?
    # Let's say we observe a massive data point of burn.
    burn_update = ledger.update_burn_forecast(project_cost / 12.0) # Monthly slice

    # 3. Create Execution Plan
    plan = allocator.create_execution_plan(brief, project_cost)

    # 4. Calculate ROI (Veto Check)
    # Strategic value from plan
    strat_val = plan['strategic_value_score']
    roi = ledger.calculate_aura_gain(project_cost, strat_val)

    print(f"Audit Result: ROI = {roi:.2f} (Threshold 1.2)")

    # 5. Underwrite Credit
    # Mock Financials for DSCR
    financials = {
        "EBITDA": 500000.0, # Annual
        "DEBT_SERVICE": 350000.0 # Annual
    }
    memo_path = underwriter.generate_credit_memo("Energy Resilience Grid", financials)

    # 6. Draft Filings
    entity_data = {
        "name": "Energy Resilience Ops LLC",
        "purpose": "Grid infrastructure management",
        "agent_name": "CFO Node",
        "officer_name": "David Roark"
    }
    registrar.draft_filing("ARTICLES_OF_INCORPORATION", entity_data)
    registrar.draft_filing("EIN_APPLICATION", entity_data)

    # 7. Vault Test (Logic Check)
    try:
        vault = IdentityVault("INVALID_TOKEN")
        vault.retrieve_identity("tax_id.json")
    except Exception as e:
        print(f"Vault Security Test: {e}")

    # 8. Save Audit Artifact
    audit_brief = {
        "source_brief": brief.get("EQUILIBRIUM_VIEW")[:50] + "...",
        "ledger_state": {
            "burn_forecast_monthly": burn_update['forecast_burn'],
            "burn_uncertainty": burn_update['uncertainty'],
            "aura_reserve": ledger.aura_reserve
        },
        "execution_plan": plan,
        "roi_analysis": {
            "score": roi,
            "decision": "APPROVED" if roi > 1.2 else "VETOED"
        },
        "credit_memo_path": memo_path
    }

    output_path = "memory/treasury/audit_001.json"
    with open(output_path, 'w') as f:
        json.dump(audit_brief, f, indent=2)

    print(f"Financial Audit Complete. Saved to {output_path}")

if __name__ == "__main__":
    run_financial_audit()
