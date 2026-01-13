import math
from typing import List, Dict, Any

class VectorEngine:
    """
    Architectural Mock for Semantic Resonance.
    Uses clean cosine_similarity with a pre-defined Resonance Map.
    """

    # Pre-defined resonance map based on Constitution (Efficiency, Equilibrium, Aura)
    # Vectors are mocked as 3-dimensional for simplicity [Efficiency, Resilience, Innovation]
    RESONANCE_MAP = {
        "constitution": [0.9, 0.8, 0.5], # Baseline
        "efficiency": [1.0, 0.5, 0.5],
        "equilibrium": [0.5, 1.0, 0.5],
        "aura": [0.5, 0.5, 1.0],
        "high_resonance": [0.8, 0.8, 0.8], # Threshold vector
        "noise": [0.1, 0.1, 0.1]
    }

    def get_embedding(self, text: str) -> List[float]:
        """
        Mocks the generation of an embedding vector.
        In production, this would call an API (e.g., OpenAI, HuggingFace).
        """
        text_lower = text.lower()

        # Mock logic: If text contains resonance keywords, boost the vector
        vec = [0.1, 0.1, 0.1] # Start with noise

        if "efficiency" in text_lower or "optimized" in text_lower:
            vec[0] += 0.8
        if "resilience" in text_lower or "grid" in text_lower or "infrastructure" in text_lower:
            vec[1] += 0.8
        if "ai" in text_lower or "innovation" in text_lower or "breakthrough" in text_lower:
            vec[2] += 0.8

        # Normalize roughly to keep within 0-1 range for this mock
        return [min(x, 1.0) for x in vec]

    def cosine_similarity(self, vec_a: List[float], vec_b: List[float]) -> float:
        """Calculates cosine similarity between two vectors."""
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
        magnitude_a = math.sqrt(sum(a * a for a in vec_a))
        magnitude_b = math.sqrt(sum(b * b for b in vec_b))

        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0

        return dot_product / (magnitude_a * magnitude_b)

    def check_resonance(self, text: str) -> float:
        """Compares text against the Constitution's baseline."""
        text_vec = self.get_embedding(text)
        const_vec = self.RESONANCE_MAP["constitution"]
        return self.cosine_similarity(text_vec, const_vec)

class OmniScout:
    """
    The Omni-Source Intelligence Engine.
    Scans Market, Tech, and Macro sectors using Semantic Resonance.
    """

    def __init__(self, search_provider=None):
        self.vector_engine = VectorEngine()
        self.search_provider = search_provider

    def scan(self, topic: str) -> Dict[str, Any]:
        """
        Scans for the topic and returns a Resonance-Verified signal.
        """
        print(f"Omni-Scout scanning for: {topic}...")

        # 1. Fetch Data (mocked live-fire bridge)
        raw_data = self._fetch_data(topic)

        # 2. Semantic Resonance Check
        resonance_score = self.vector_engine.check_resonance(raw_data['content'])
        print(f"  > Resonance Score: {resonance_score:.4f}")

        return {
            "signal_content": raw_data['content'],
            "source": raw_data['source'],
            "resonance_score": resonance_score,
            "topic": topic
        }

    def _fetch_data(self, topic: str) -> Dict[str, str]:
        if self.search_provider:
            return self.search_provider(topic)
        return {"content": "No Data", "source": "None"}
