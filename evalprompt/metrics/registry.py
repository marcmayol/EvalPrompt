from typing import Dict, Type

from evalprompt.metrics.base import Metric


class MetricRegistry:
    """
    Registry that stores and provides access to metric classes.
    Allows registration, retrieval, and inspection of available metrics.
    """

    def __init__(self) -> None:
        """
        Initialize the registry as an empty dictionary that maps metric names to metric classes.
        """
        self._metrics: Dict[str, Type[Metric]] = {}

    def register(self, name: str, metric_cls: Type[Metric]) -> None:
        """
        Register a metric class under the given name.

        Parameters:
            name: Identifier used to store and retrieve the metric.
            metric_cls: Class implementing the Metric interface.
        """
        self._metrics[name] = metric_cls

    def get(self, name: str) -> Type[Metric]:
        """
        Retrieve a metric class by its registered name.

        Parameters:
            name: Name of the metric to retrieve.

        Returns:
            The metric class associated with the provided name.
        """
        return self._metrics[name]

    def available(self) -> Dict[str, Type[Metric]]:
        """
        Return a dictionary with all registered metric names and their corresponding classes.

        Returns:
            A dictionary mapping metric names to metric classes.
        """
        return dict(self._metrics)


metric_registry = MetricRegistry()
