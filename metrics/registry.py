from typing import Dict, Type

from evalprompt.metrics.base import Metric


class MetricRegistry:
    # Holds registered metric classes
    def __init__(self) -> None:
        self._metrics: Dict[str, Type[Metric]] = {}

    def register(self, name: str, metric_cls: Type[Metric]) -> None:
        # Registers a metric class under a name
        self._metrics[name] = metric_cls

    def get(self, name: str) -> Type[Metric]:
        # Returns the metric class for a given name
        return self._metrics[name]

    def available(self) -> Dict[str, Type[Metric]]:
        # Returns all registered metrics
        return dict(self._metrics)


metric_registry = MetricRegistry()
