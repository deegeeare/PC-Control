# Local Development

## Prerequisites
- Python 3.10+
- Docker (optional for now)

## Setup

1.  **Clone**:
    ```bash
    git clone <repo>
    cd agentos
    ```

2.  **Install**:
    ```bash
    pip install -e .[dev]
    ```

3.  **Config**:
    Ensure `constitution.yml`, `decision_style.yml`, and `approval_matrix.yml` are present in the root.

## Running Tests

```bash
pytest
```

## Running the Agent (Stub)

```bash
python -m agentos
```
