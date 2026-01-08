import yaml
import os
from typing import Dict, Any

class CTONode:
    """
    The CTO Node: Lead Architect.
    Responsible for codebase integrity and orchestration.
    """
    CONFIG_PATH = "council/cto.yml"

    def __init__(self, config_path: str = None):
        self.config_path = config_path or self.CONFIG_PATH
        self.config = self._load_config()
        self.auditor = self._initialize_auditor()

    def _load_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"CTO config not found at {self.config_path}")
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)

    def _initialize_auditor(self):
        """Initializes the Auditor sub-node (Resonance Engine interface)."""
        print("Initializing Auditor sub-node...")
        try:
            from core.resonance_check import ResonanceEngine
            return ResonanceEngine()
        except ImportError:
            print("Warning: ResonanceEngine not found. Auditor running in phantom mode.")
            return None

    def audit_code(self, code_snippet: str) -> bool:
        """Runs the Auditor check on a code snippet."""
        if not self.auditor:
            return False
        print(f"CTO Auditing code: {code_snippet[:50]}...")
        return self.auditor.check_resonance(code_snippet)

if __name__ == "__main__":
    cto = CTONode()
    print(f"Initialized Node: {cto.config['name']} ({cto.config['role']})")

    # Test audit
    snippet = "def build_kingdom(): return 'efficiency' + 'aura'"
    passed = cto.audit_code(snippet)
    print(f"Audit Result: {'PASSED' if passed else 'FAILED'}")
