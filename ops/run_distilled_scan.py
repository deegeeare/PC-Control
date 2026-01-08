import json
import os
import sys

# Add root to sys.path
sys.path.append(os.getcwd())

from core.omni_scout import OmniScout
from core.bias_neutralizer import ArbiterOfDissent

# Mock Search Provider for "Live Fire" data (Energy Grid)
def energy_live_fire_provider(query):
    query_lower = query.lower()

    if "global energy grid" in query_lower or "resilience" in query_lower:
        return {
            "source": "World Economic Forum & Deloitte",
            "content": "AI is rewiring power demand. Peak power demand could increase 26% by 2035 due to data centers. Access to power is now the leading factor in data center site selection. 2026 will see intense competition for grid connections."
        }

    if "risks" in query_lower or "failure modes" in query_lower:
        return {
            "source": "WEF & Deloitte Risks",
            "content": "The AI energy surge is turning power into the new bottleneck. The grid is already stretched thin. Market volatility and supply chain hurdles pose risks. Failure to secure resilient low-carbon power will disadvantage nations."
        }

    return {"content": "No data", "source": "None"}

def run_distilled_scan():
    print("INITIALIZING OMNI-SCOUT DISTILLATION: Energy Grid 2026")

    # 1. Initialize Nodes
    omni = OmniScout(search_provider=energy_live_fire_provider)
    arbiter = ArbiterOfDissent(search_provider=energy_live_fire_provider)

    # 2. Omni-Scout Scan
    topic = "Global Energy Grid Resilience & AI Power Demand 2026"
    scout_result = omni.scan(topic)

    # 3. Conflict Loop & Neutralization
    arbiter_result = arbiter.neutralize_bias(scout_result)

    # 4. CEO & Team Directives (Strategic Generation Mock)
    ceo_actions = [
        "Authorize 'Project Dynamo': Secure direct PPAs with SMR (Small Modular Reactor) vendors.",
        "Pivot infrastructure portfolio to 'Power-First' site selection criteria.",
        "Approve R&D budget for proprietary grid-balancing AI models."
    ]

    team_directives = {
        "CTO": "Audit internal compute efficiency to lower MW/Workload ratio.",
        "CFO": "Hedge energy price volatility for 2027-2030 contracts.",
        "CMO": "Position 'Green AI' as a core brand pillar to offset consumption narratives."
    }

    # 5. Format Brief
    brief = {
        "HARD_FACTS": arbiter_result['HARD_FACTS'],
        "EQUILIBRIUM_VIEW": arbiter_result['EQUILIBRIUM_VIEW'],
        "CEO_KEY_ACTIONS": ceo_actions,
        "TEAM_DIRECTIVES": team_directives
    }

    # 6. Save Artifact
    output_path = "memory/intelligence_briefs/distilled_brief_001.json"
    with open(output_path, 'w') as f:
        json.dump(brief, f, indent=2)

    print(f"Distillation Complete. Saved to {output_path}")
    print(json.dumps(brief, indent=2))

if __name__ == "__main__":
    run_distilled_scan()
