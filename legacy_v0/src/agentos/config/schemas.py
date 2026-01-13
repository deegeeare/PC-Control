from typing import List, Optional, Dict, Literal, Any
from pydantic import BaseModel, Field

# --- Constitution Schema ---

class Mission(BaseModel):
    north_star: str
    who_we_serve: str
    definition_of_win: str

class RedLines(BaseModel):
    forbidden_actions: List[str]
    forbidden_domains: List[str]

class FinancialRisk(BaseModel):
    spend_without_approval_usd: float

class EscalationThresholds(BaseModel):
    legal: str
    financial: FinancialRisk
    reputation: str
    safety: str

class RiskAppetite(BaseModel):
    default_mode: Literal["conservative", "balanced", "aggressive"]
    escalation_thresholds: EscalationThresholds

class HumanInTheLoop(BaseModel):
    required_for: List[str]

class AuditLogConfig(BaseModel):
    required: bool
    retention_days: int

class Governance(BaseModel):
    human_in_the_loop: HumanInTheLoop
    audit_log: AuditLogConfig

class Constitution(BaseModel):
    version: str
    name: str
    mission: Mission
    values: List[str]
    non_negotiables: List[str]
    red_lines: RedLines
    risk_appetite: RiskAppetite
    governance: Governance
    operating_principles: List[str]


# --- Decision Style Schema ---

class CeoProfile(BaseModel):
    name: str
    role: str

class DecisionDefaults(BaseModel):
    bias: Literal["action_with_guardrails", "analysis_first"]
    time_horizon: Literal["short", "medium", "long"]
    preferred_tradeoff: str

class QuestionFormat(BaseModel):
    max_questions: int
    style: str
    must_include: List[str]

class QuestioningProtocol(BaseModel):
    ask_when: List[str]
    question_format: QuestionFormat

class DecisionFramework(BaseModel):
    required_fields: List[str]

class ApprovalLanguage(BaseModel):
    accept_phrases: List[str]
    reject_phrases: List[str]

class DecisionStyle(BaseModel):
    version: str
    name: str
    ceo_profile: CeoProfile
    decision_defaults: DecisionDefaults
    questioning_protocol: QuestioningProtocol
    decision_framework: DecisionFramework
    approval_language: ApprovalLanguage


# --- Approval Matrix Schema ---

class Level(BaseModel):
    description: str

class Levels(BaseModel):
    auto: Level
    ask: Level
    block: Level

class Thresholds(BaseModel):
    usd: float

class Rule(BaseModel):
    category: str
    level: Literal["auto", "ask", "block"]
    thresholds: Optional[Thresholds] = None

class ApprovalMatrix(BaseModel):
    version: str
    name: str
    default: Literal["auto", "ask", "block"]
    levels: Levels
    rules: List[Rule]
