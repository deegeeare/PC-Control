import pytest
from pathlib import Path
import yaml
from copy import deepcopy
from pydantic import ValidationError

from agentos.config.loader import ConfigLoader
from agentos.config.schemas import Constitution, DecisionStyle, ApprovalMatrix

# Sample valid data
VALID_CONSTITUTION = {
    "version": "0.1",
    "name": "AgentOS Constitution",
    "mission": {
        "north_star": "NS",
        "who_we_serve": "WWS",
        "definition_of_win": "DOW"
    },
    "values": ["v1"],
    "non_negotiables": ["nn1"],
    "red_lines": {
        "forbidden_actions": ["fa1"],
        "forbidden_domains": ["fd1"]
    },
    "risk_appetite": {
        "default_mode": "balanced",
        "escalation_thresholds": {
            "legal": "always_escalate",
            "financial": {"spend_without_approval_usd": 100},
            "reputation": "always_escalate",
            "safety": "always_escalate"
        }
    },
    "governance": {
        "human_in_the_loop": {"required_for": ["a"]},
        "audit_log": {"required": True, "retention_days": 365}
    },
    "operating_principles": ["op1"]
}

VALID_DECISION_STYLE = {
    "version": "0.1",
    "name": "CEO Decision Style",
    "ceo_profile": {"name": "Test", "role": "CEO"},
    "decision_defaults": {
        "bias": "action_with_guardrails",
        "time_horizon": "long",
        "preferred_tradeoff": "durability_over_speed"
    },
    "questioning_protocol": {
        "ask_when": ["condition"],
        "question_format": {
            "max_questions": 5,
            "style": "brief",
            "must_include": ["options"]
        }
    },
    "decision_framework": {"required_fields": ["goal"]},
    "approval_language": {
        "accept_phrases": ["Yes"],
        "reject_phrases": ["No"]
    }
}

VALID_APPROVAL_MATRIX = {
    "version": "0.1",
    "name": "Approval Matrix",
    "default": "ask",
    "levels": {
        "auto": {"description": "d1"},
        "ask": {"description": "d2"},
        "block": {"description": "d3"}
    },
    "rules": [
        {"category": "cat1", "level": "ask"}
    ]
}

@pytest.fixture
def config_dir(tmp_path):
    return tmp_path

def create_yaml(path, data):
    with open(path, 'w') as f:
        yaml.dump(data, f)

def test_load_valid_constitution(config_dir):
    create_yaml(config_dir / "constitution.yml", VALID_CONSTITUTION)
    loader = ConfigLoader(config_dir)
    constitution = loader.load_constitution()
    assert isinstance(constitution, Constitution)
    assert constitution.mission.north_star == "NS"

def test_load_valid_decision_style(config_dir):
    create_yaml(config_dir / "decision_style.yml", VALID_DECISION_STYLE)
    loader = ConfigLoader(config_dir)
    ds = loader.load_decision_style()
    assert isinstance(ds, DecisionStyle)
    assert ds.decision_defaults.bias == "action_with_guardrails"

def test_load_valid_approval_matrix(config_dir):
    create_yaml(config_dir / "approval_matrix.yml", VALID_APPROVAL_MATRIX)
    loader = ConfigLoader(config_dir)
    am = loader.load_approval_matrix()
    assert isinstance(am, ApprovalMatrix)
    assert am.default == "ask"

def test_missing_file(config_dir):
    loader = ConfigLoader(config_dir)
    with pytest.raises(FileNotFoundError):
        loader.load_constitution()

def test_invalid_yaml(config_dir):
    with open(config_dir / "constitution.yml", "w") as f:
        f.write("invalid: [ yaml")
    loader = ConfigLoader(config_dir)
    with pytest.raises(ValueError, match="Error parsing YAML"):
        loader.load_constitution()

def test_validation_error_missing_field(config_dir):
    invalid_data = deepcopy(VALID_CONSTITUTION)
    del invalid_data["mission"]
    create_yaml(config_dir / "constitution.yml", invalid_data)
    loader = ConfigLoader(config_dir)
    with pytest.raises(ValueError, match="Validation failed"):
        loader.load_constitution()

def test_validation_error_invalid_enum(config_dir):
    invalid_data = deepcopy(VALID_DECISION_STYLE)
    invalid_data["decision_defaults"]["bias"] = "random_bias"
    create_yaml(config_dir / "decision_style.yml", invalid_data)
    loader = ConfigLoader(config_dir)
    with pytest.raises(ValueError, match="Validation failed"):
        loader.load_decision_style()

def test_load_all(config_dir):
    create_yaml(config_dir / "constitution.yml", VALID_CONSTITUTION)
    create_yaml(config_dir / "decision_style.yml", VALID_DECISION_STYLE)
    create_yaml(config_dir / "approval_matrix.yml", VALID_APPROVAL_MATRIX)

    loader = ConfigLoader(config_dir)
    c, d, a = loader.load_all()
    assert isinstance(c, Constitution)
    assert isinstance(d, DecisionStyle)
    assert isinstance(a, ApprovalMatrix)
