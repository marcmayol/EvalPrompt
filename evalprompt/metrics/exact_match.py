from evalprompt.metrics.base import Metric
from evalprompt.core.types import MetricResult


class ExactMatchMetric(Metric):
    """
    Metric that checks whether the predicted output exactly matches
    the expected output. Returns 1.0 for an exact match, otherwise 0.0.
    """

    name = "exact_match"

    def compute(self, predicted, expected, context=None):
        """
        Computes the exact match score.
        predicted: model output
        expected: expected output from the dataset
        context: optional metadata for future extensions
        """
        value = 1.0 if predicted == expected else 0.0
        return MetricResult(
            metric_name=self.name,
            value=value,
            details={"predicted": predicted, "expected": expected},
        )
