from typing import Dict, Any, List

class ArbiterOfDissent:
    """
    The Arbiter of Dissent.
    Initiates a Conflict Loop to neutralize bias and find Equilibrium.
    Mandate: Ensure the Kingdom operates on Truth, Efficiency, and Aura.
    """

    def __init__(self, search_provider=None):
        self.search_provider = search_provider

    def neutralize_bias(self, signal_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Synthesizes the Signal (Bull) and Counter-Signal (Bear) into an Equilibrium View.
        This process ensures the 'Probable' outweighs the 'Possible', maintaining high resonance.
        """
        signal_content = signal_data.get('signal_content', '')
        print(f"Arbiter initiating Conflict Loop for: {signal_content[:50]}...")

        # 1. Fetch Counter-Signal (Bear) to challenge the Aura
        counter_query = f"risks challenges failure modes of {signal_data.get('topic', '')}"
        counter_data = self._fetch_counter_signal(counter_query)

        # 2. Extract Hard Facts (Heuristic extraction for Efficiency)
        hard_facts = self._extract_hard_facts(signal_content, counter_data['content'])

        # 3. Synthesize Equilibrium View (The Golden Mean)
        equilibrium_view = self._synthesize(signal_content, counter_data['content'])

        return {
            "HARD_FACTS": hard_facts,
            "EQUILIBRIUM_VIEW": equilibrium_view,
            "BEAR_SOURCE": counter_data['source']
        }

    def _fetch_counter_signal(self, query: str) -> Dict[str, str]:
        if self.search_provider:
            return self.search_provider(query)
        return {"content": "No counter-data found.", "source": "None"}

    def _extract_hard_facts(self, text_a: str, text_b: str) -> List[str]:
        """
        Extracts sentences containing numbers or dates (Simple Heuristic).
        """
        facts = []
        combined = text_a + " " + text_b
        for sentence in combined.split('.'):
            # Check for digits as a proxy for quantitative data
            if any(char.isdigit() for char in sentence):
                clean_sent = sentence.strip()
                if len(clean_sent) > 10:
                    facts.append(clean_sent)
        return facts[:5] # Return top 5

    def _synthesize(self, bull: str, bear: str) -> str:
        """
        Removes emotional bias and combines views.
        """
        # In a real LLM, this would be a prompt.
        # Here we construct a template.
        return (
            f"While the expansion vector suggests {bull[:50]}..., "
            f"structural constraints indicate {bear[:50]}... "
            "Equilibrium requires balancing rapid infrastructure deployment with grid stability protocols."
        )
