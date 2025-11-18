"""
Data classes used across the EvalPrompt evaluation pipeline.
"""
from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class PromptDefinition:
    """
    Definition of a named prompt template that can be rendered with variables.
    Stores the template string and optional metadata.
    """

    name: str
    template: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    def render(self, variables: Dict[str, Any]) -> str:
        """
        Render the prompt template using the provided variables.

        Parameters:
            variables: Dictionary of values to be injected into the template.

        Returns:
            A formatted string with all variables replaced in the template.
        """
        return self.template.format(**variables)


@dataclass
class EvalExample:
    """
    Represents an evaluation example containing input data and an optional expected output.
    """

    input_data: Dict[str, Any]
    expected_output: Optional[Any] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ModelOutput:
    """
    Represents the output produced by a model for a specific prompt and example.
    """

    prompt_name: str
    example_id: str
    raw_output: Any
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MetricResult:
    """
    Represents the result of applying a metric to a prediction, including the metric name,
    its value, and optional details.
    """

    metric_name: str
    value: float
    details: Dict[str, Any] = field(default_factory=dict)
