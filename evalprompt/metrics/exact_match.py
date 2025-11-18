from evalprompt.metrics.base import Metric
from evalprompt.core.types import MetricResult


class ExactMatchMetric(Metric):
    name = "exact_match"

    def compute(self, predicted, expected, context=None):
        value = 1.0 if predicted == expected else 0.0
        return MetricResult(
            metric_name=self.name,
            value=value,
            details={"predicted": predicted, "expected": expected},
        )
