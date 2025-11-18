"""
Core package for the EvalPrompt library.
"""
from evalprompt.core.types import (
    PromptDefinition,
    EvalExample,
    ModelOutput,
    MetricResult,
)

from evalprompt.providers.base import ModelProvider
from evalprompt.providers.registry import provider_registry

from evalprompt.metrics.base import Metric
from evalprompt.metrics.registry import metric_registry

from evalprompt.judges.base import Judge


# Public API for EvalPrompt
__all__ = [
    "PromptDefinition",
    "EvalExample",
    "ModelOutput",
    "MetricResult",
    "ModelProvider",
    "provider_registry",
    "Metric",
    "metric_registry",
    "Judge",
]
