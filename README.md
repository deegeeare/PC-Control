# AgentOS

AgentOS is a multi-nodal AI council built to help the CEO run a business. It is not one monolithic agent. It is multiple specialized nodes working in parallel with intentional overlap, plus a referee layer.

## Core Principles

*   **Nodes not monoliths**: Break thinking into specialized agents: Strategy, Finance, Ops, Risk, Red Team, Research, and a CEO Chief of Staff.
*   **Overlap by design**: At least two nodes must cover key decisions from different angles to prevent blind spots.
*   **Referee node**: Synthesizes outputs, detects contradictions, produces a one page CEO brief, and generates the minimal question set needed to proceed.
*   **Ask not guess**: If constraints are missing, the system must stop and ask the CEO targeted questions.
*   **Policy gated execution**: No tool action can execute unless the policy engine approves it per constitution + approval matrix.
*   **Audit everything**: Every step logged with task id, node id, inputs, outputs, policy checks, tool calls.
*   **Evals are boss**: Continuous eval suite to prevent drift. Include ambiguity tests, disagreement tests, tool outage tests, governance tests.

## Getting Started

See `docs/LOCAL_DEV.md` for instructions on how to set up and run the system.

## Documentation

*   [Architecture](docs/ARCHITECTURE.md)
*   [Node Contracts](docs/NODE_CONTRACTS.md)
*   [Policy Engine](docs/POLICY_ENGINE.md)
*   [Evals](docs/EVALS.md)
