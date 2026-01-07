# Node Contracts

Every node in AgentOS must adhere to a strict interface. This allows the orchestrator to swap, mock, or parallelize nodes without changes to the core logic.

## Interface

### Input
Each node receives a JSON object containing:
- `task_id`: Unique correlation ID.
- `global_context`: The original CEO request and constraints.
- `upstream_artifacts`: Outputs from dependencies (if any).
- `config`: Node-specific configuration.

### Output
Each node must return:
- `status`: success | failure | needs_clarification.
- `thought_trace`: Reasoning steps (for audit).
- `artifacts`: Structured data (dictionaries, lists, text) representing the node's work.
- `tool_calls`: List of tool invocations (if any).

## Template

```python
class BaseNode:
    def run(self, context: NodeContext) -> NodeResult:
        """
        Execute the node's logic.
        """
        pass
```

## Standard Nodes

- **Chief of Staff**: Router and final synthesizer.
- **Strategy**: Long-term alignment checker.
- **Finance**: Budget and ROI analysis.
- **Risk**: Downside protection and legal compliance.
- **Ops**: Feasibility and execution planning.
