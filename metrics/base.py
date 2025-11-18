from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from evalprompt.core.types import MetricResult


class Metric(ABC):
    # Name used to identify the metric in results and registries
    name: str

    @abstractmethod
    def compute(
        self,
        predicted: Any,
        expected: Any,
        context: Optional[Dict[str, Any]] = None,
    ) -> MetricResult:
        # Computes the metric value comparing predicted vs expected
        raise NotImplementedError
