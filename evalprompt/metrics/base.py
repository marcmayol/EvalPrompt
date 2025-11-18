"""Base class for defining evaluation metrics in EvalPrompt."""
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from evalprompt.core.types import MetricResult


class Metric(ABC):
    """
    Base abstract class for all metric implementations.
    Each metric must define a unique name and implement the compute method.
    """

    name: str

    @abstractmethod
    def compute(
        self,
        predicted: Any,
        expected: Any,
        context: Optional[Dict[str, Any]] = None,
    ) -> MetricResult:
        """
        Compute the value of the metric by comparing the predicted output with the expected one.

        Parameters:
            predicted: The model output to evaluate.
            expected: The reference or ground truth value.
            context: Optional additional data that may be useful for the computation.

        Returns:
            MetricResult containing the numerical value of the metric and additional metadata.
        """
        raise NotImplementedError
