from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class PromptDefinition:
    # Represents a named prompt template that can be rendered with variables
    name: str
    template: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    def render(self, variables: Dict[str, Any]) -> str:
        return self.template.format(**variables)


@dataclass
class EvalExample:
    # Represents a single evaluation case with input data and optional expected output
    input_data: Dict[str, Any]
    expected_output: Optional[Any] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ModelOutput:
    # Represents the model output generated for a specific prompt and example
    prompt_name: str
    example_id: str
    raw_output: Any
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MetricResult:
    # Represents the result of applying a metric to a prediction
    metric_name: str
    value: float
    details: Dict[str, Any] = field(default_factory=dict)
