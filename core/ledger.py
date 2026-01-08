import math
from typing import Dict, Any

class BayesianLedger:
    """
    The Sovereign Ledger.
    Uses Bayesian logic to track Systemic Burn and calculate Aura-ROI.
    Mandate: Precision, Truth, Sustainability.
    """

    def __init__(self):
        # Bayesian Priors for "Burn Probability"
        # Mean expected burn rate (monthly), Variance (uncertainty)
        self.burn_prior_mean = 50000.0 # Baseline monthly burn estimate
        self.burn_prior_variance = 10000.0

        # Aura-Capital Reserve (Abstract currency of reputation/efficiency)
        self.aura_reserve = 1000000.0

    def update_burn_forecast(self, actual_spend: float) -> Dict[str, float]:
        """
        Updates the Burn Probability Distribution using a lightweight Bayesian update.
        Posterior Mean = (Variance_Prior * Data + Variance_Data * Mean_Prior) / (Variance_Prior + Variance_Data)
        """
        # Assume observed data has some variance (noise)
        data_variance = 5000.0

        # Calculate Posterior Mean
        numerator = (self.burn_prior_variance * actual_spend) + (data_variance * self.burn_prior_mean)
        denominator = self.burn_prior_variance + data_variance
        posterior_mean = numerator / denominator

        # Update Variance (simplified: 1 / (1/var_prior + 1/var_data))
        posterior_variance = 1.0 / ((1.0 / self.burn_prior_variance) + (1.0 / data_variance))

        # Update internal state
        self.burn_prior_mean = posterior_mean
        self.burn_prior_variance = posterior_variance

        return {
            "forecast_burn": posterior_mean,
            "uncertainty": math.sqrt(posterior_variance)
        }

    def calculate_aura_gain(self, financial_spend: float, strategic_value: float) -> float:
        """
        Calculates Resonance-Adjusted ROI.
        Formula: (Strategic Value * Resonance Factor) / Financial Spend
        """
        # Heuristic: Resonance Factor assumes high alignment (0.95) if passed CIO check
        resonance_factor = 0.95

        # Normalize spend to "Aura Units" (e.g., $1000 = 1 Aura Unit)
        spend_units = max(financial_spend / 1000.0, 1.0)

        # Strategic Value is arbitrary input (0-100 scale from Allocator)
        roi = (strategic_value * resonance_factor) / spend_units

        # ROI > 1.2 is passing
        return roi

# High Resonance Keywords: Precision, Truth, Sustainability, Aura-Capital
