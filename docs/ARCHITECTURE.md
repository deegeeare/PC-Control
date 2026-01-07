# AgentOS Architecture

The system is designed as a multi-nodal graph rather than a linear chain.

## Layers

1.  **Interface Layer**: CLI or API that accepts the CEO's intent.
2.  **Orchestrator Layer**: Manages the graph execution, state propagation, and parallel node execution.
3.  **Node Layer**: Independent specialized agents (Strategy, Finance, Risk, etc.) that perform specific analysis or actions.
4.  **Referee Layer**: A specialized node that synthesizes divergent opinions from other nodes.
5.  **Policy Engine Layer**: A middleware that intercepts every attempt to use a tool or finalize a decision, validating it against the `constitution.yml` and `approval_matrix.yml`.
6.  **Tool Gateway**: The only path for the system to affect the outside world.
7.  **Infrastructure Layer**: Audit logging, state persistence, and observability.

## State Model

State is a directed acyclic graph (DAG) of context.
- **Global Context**: The original request, global constraints.
- **Node Context**: Private scratchpad for each node.
- **Artifacts**: Outputs from nodes (reports, decisions, code).

## Data Flow

1.  **Intent**: CEO inputs a request.
2.  **Fan-out**: Orchestrator triggers relevant nodes in parallel.
3.  **Processing**: Nodes think and act (read-only tools).
4.  **Fan-in**: Referee collects outputs.
5.  **Synthesis/Conflict**: Referee detects conflicts or missing info.
6.  **Resolution**:
    - If valid: Proposal generated.
    - If conflict/missing info: Questions generated for CEO.
7.  **Approval**: Policy Engine checks if action needs human approval.
8.  **Execution**: Tool Gateway executes if allowed.
