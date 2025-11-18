"""
Metric utilities and registry for EvalPrompt.
"""
from evalprompt.metrics.registry import metric_registry
from evalprompt.metrics.exact_match import ExactMatchMetric

metric_registry.register("exact_match", ExactMatchMetric)
