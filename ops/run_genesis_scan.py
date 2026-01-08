import json
import os
import sys

# Add root to sys.path to ensure imports work
sys.path.append(os.getcwd())

from core.signal_scout import SignalScout
from core.truth_verify import SkepticProtocol

# Mock Search Provider that returns the "Live Fire" data I just fetched
def live_fire_search_provider(query):
    query_lower = query.lower()

    # Scout Logic
    if "technical paper" in query_lower:
        return {
            "source": "HPC Wire & MIT Sloan",
            "content": "The Delegation Shift: By 2026, 40% of enterprise apps will use agentic AI. The focus is on 'Orchestration Awakening' where AI pursues goals and coordinates across workflows autonomously."
        }
    elif "market impact" in query_lower:
        return {
            "source": "Enkrypt AI & Gartner",
            "content": "Agentic AI is moving from demos to production. 15% of routine work decisions will be made autonomously by 2026. Customer service agents will handle 80% of issues."
        }
    elif "global societal" in query_lower:
        return {
            "source": "MIT Sloan",
            "content": "Tensions between Scalability vs Adaptability. The shift mirrors the internet revolution, creating new vulnerabilities while streamlining industries. 'Teammates not tools'."
        }

    # Skeptic Logic
    elif "criticism" in query_lower or "risks" in query_lower:
        return {
            "source": "ABA Banking Journal",
            "content": "Crisis Risk: 'Sleepwalking into an agentic AI crisis'. Risks include emergent behaviors, misaligned objectives, and agents colluding. 737 Max moment potential where over-reliance collides with accountability."
        }

    return {"source": "Unknown", "content": "No data found."}

def run_genesis_scan():
    print("INITIALIZING GENESIS SCAN: Agentic AI Breakthroughs 2026")

    # 1. Initialize Nodes
    scout = SignalScout(search_provider=live_fire_search_provider)
    skeptic = SkepticProtocol(search_provider=live_fire_search_provider)

    # 2. Scout Execution
    topic = "Agentic AI breakthroughs 2026"
    scout_result = scout.triangulate(topic)

    # 3. Skeptic Execution
    skeptic_result = skeptic.challenge_signal(scout_result)

    # 4. Nexus Notification Formatting
    brief = {
        "signal": scout_result['signal'],
        "resonance_score": skeptic_result['resonance_score'],
        "skeptic_note": skeptic_result['skeptic_note']['content'], # Extract content string
        "four_year_projection": "By 2030, the 'Orchestration Awakening' will fundamentally alter corporate hierarchies, replacing middle management with AI-driven autonomous workflow loops, requiring strict HITL governance to prevent the '737 Max' scenario."
    }

    # 5. Save to Memory
    output_path = "memory/intelligence_briefs/scan_001.json"
    with open(output_path, 'w') as f:
        json.dump(brief, f, indent=2)

    print(f"Scan Complete. Saved to {output_path}")
    print(json.dumps(brief, indent=2))

if __name__ == "__main__":
    run_genesis_scan()
