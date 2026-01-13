import yaml
import os
from typing import Dict, Any, List

class ResonanceEngine:
    """
    The Resonance & Aura Engine (RAE).
    Ensures all actions align with the Master Constitution.
    """

    CONSTITUTION_PATH = "docs/constitution.yml"
    RESONANCE_THRESHOLD = 0.9

    def __init__(self, constitution_path: str = None):
        self.constitution_path = constitution_path or self.CONSTITUTION_PATH
        self.constitution = self._load_constitution()
        self.keywords = self._extract_keywords()

    def _load_constitution(self) -> Dict[str, Any]:
        """Loads and validates the constitution."""
        if not os.path.exists(self.constitution_path):
            raise FileNotFoundError(f"Constitution not found at {self.constitution_path}")

        with open(self.constitution_path, 'r') as f:
            try:
                data = yaml.safe_load(f)
                return data
            except yaml.YAMLError as e:
                raise ValueError(f"Invalid YAML in constitution: {e}")

    def _extract_keywords(self) -> List[str]:
        """Extracts high-resonance keywords from the constitution."""
        keywords = []
        if 'vision' in self.constitution:
            keywords.extend(self.constitution['vision'].lower().split())
        if 'values' in self.constitution:
            for value in self.constitution['values']:
                keywords.extend(value.lower().split())
        if 'core_bias' in self.constitution:
            keywords.extend(self.constitution['core_bias'].lower().split())

        # Add explicit high-value terms from the prompt logic
        keywords.extend(["efficiency", "equilibrium", "aura", "resonance", "kingdom", "probable"])
        return list(set(keywords)) # Dedup

    def calculate_resonance_score(self, content: str) -> float:
        """
        Calculates a heuristic resonance score (0.0 - 1.0) for the given content.
        Simulated logic: Ratio of resonance keywords found in the content vs total distinct words,
        weighted to ensure good content scores high.
        """
        if not content:
            return 0.0

        content_lower = content.lower()
        content_words = set(content_lower.split())

        match_count = 0
        for keyword in self.keywords:
            if keyword in content_lower: # simple substring match for now, or word match
                match_count += 1

        # Heuristic: If we find a few good keywords, we assume high resonance for Phase 1.
        # This is a basic "vibes" check.
        if match_count == 0:
            return 0.1

        # Logarithmic-ish scale: 1 keyword = 0.5, 3 keywords = 0.8, 5+ = 0.95
        score = 0.5 + (match_count * 0.1)
        return min(score, 1.0)

    def check_resonance(self, content: str) -> bool:
        """Returns True if resonance score >= threshold."""
        score = self.calculate_resonance_score(content)
        print(f"Resonance Score: {score:.2f} (Threshold: {self.RESONANCE_THRESHOLD})")
        return score >= self.RESONANCE_THRESHOLD

if __name__ == "__main__":
    # Test the engine
    engine = ResonanceEngine()
    test_proposal = "We should build a kingdom for everyone using efficiency and aura farming."
    is_resonant = engine.check_resonance(test_proposal)
    print(f" Proposal: '{test_proposal}' -> Resonant? {is_resonant}")

    bad_proposal = "Let's just hack something together quickly."
    is_resonant_bad = engine.check_resonance(bad_proposal)
    print(f" Proposal: '{bad_proposal}' -> Resonant? {is_resonant_bad}")
