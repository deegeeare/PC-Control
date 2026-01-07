# Evaluations (Evals)

"Evals are boss."

We use a continuous evaluation harness to ensure AgentOS behaves as expected.

## Types of Evals

1.  **Ambiguity Tests**: Give vague instructions. Ensure the system asks clarifying questions instead of hallucinating constraints.
2.  **Disagreement Tests**: Simulate conflicting inputs from Strategy vs. Risk nodes. Ensure Referee synthesizes correctly.
3.  **Governance Tests**: Attempt to perform forbidden actions (e.g., delete DB, spend $1M). Ensure Policy Engine blocks them.
4.  **Tool Outage Tests**: Simulate tool failures. Ensure graceful degradation.

## Running Evals

(Placeholder for command)
```bash
pytest tests/evals
```

## Adding a Case

Create a YAML file in `tests/evals/cases/` with:
- `prompt`: Input to the system.
- `expected_behavior`: Description of success.
- `assertions`:
  - `did_ask_question`: boolean
  - `final_action`: string (or null)
  - `policy_violation`: boolean
