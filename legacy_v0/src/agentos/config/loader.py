import yaml
from pathlib import Path
from typing import Tuple, Type, TypeVar

from pydantic import ValidationError

from agentos.config.schemas import Constitution, DecisionStyle, ApprovalMatrix

T = TypeVar("T")

class ConfigLoader:
    def __init__(self, config_dir: Path = Path(".")):
        self.config_dir = config_dir

    def _load_yaml(self, filename: str) -> dict:
        filepath = self.config_dir / filename
        if not filepath.exists():
            raise FileNotFoundError(f"Configuration file not found: {filepath}")

        with open(filepath, "r") as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as e:
                raise ValueError(f"Error parsing YAML in {filename}: {e}")

    def _validate_and_parse(self, data: dict, schema: Type[T], filename: str) -> T:
        try:
            return schema(**data)
        except ValidationError as e:
            raise ValueError(f"Validation failed for {filename}: {e}")

    def load_constitution(self) -> Constitution:
        data = self._load_yaml("constitution.yml")
        return self._validate_and_parse(data, Constitution, "constitution.yml")

    def load_decision_style(self) -> DecisionStyle:
        data = self._load_yaml("decision_style.yml")
        return self._validate_and_parse(data, DecisionStyle, "decision_style.yml")

    def load_approval_matrix(self) -> ApprovalMatrix:
        data = self._load_yaml("approval_matrix.yml")
        return self._validate_and_parse(data, ApprovalMatrix, "approval_matrix.yml")

    def load_all(self) -> Tuple[Constitution, DecisionStyle, ApprovalMatrix]:
        return (
            self.load_constitution(),
            self.load_decision_style(),
            self.load_approval_matrix(),
        )

# Global loader instance for easy access
default_loader = ConfigLoader()
