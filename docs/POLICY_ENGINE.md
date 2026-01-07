# Policy Engine

The Policy Engine is the "superego" of AgentOS. It enforces the rules defined in `constitution.yml` and `approval_matrix.yml`.

## Mechanism

The Policy Engine is implemented as a wrapper around the Tool Gateway.

1.  **Interception**: Every request to use a tool is intercepted.
2.  **Classification**: The tool call is categorized (e.g., "send_email" -> "communications_external").
3.  **Lookup**: The category is looked up in `approval_matrix.yml`.
4.  **Enforcement**:
    - **Auto**: Log and proceed.
    - **Ask**: Pause execution, generate a request for CEO approval.
    - **Block**: Deny the action, return error to the Node.

## Constitution Checks

In addition to the matrix, the Policy Engine runs semantic checks against `constitution.yml`:
- Does this action violate "Who we serve"?
- Does it cross a "Red Line"?
- Is the risk profile acceptable?

These checks are often performed by a specialized lightweight LLM call ("ConstitutionLM") that votes on the action's alignment.
