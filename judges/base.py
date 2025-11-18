from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from evalprompt.core.types import MetricResult


class Judge(ABC):
    # Base interface for components that evaluate model outputs
    name: str

    @abstractmethod
    def judge_single(
        self,
        input_data: Dict[str, Any],
        prompt_name: str,
        output: Any,
        expected_output: Optional[Any] = None,
    ) -> MetricResult:
        # Evaluates a single output for a given prompt and example
        raise NotImplementedError

    @abstractmethod
    def judge_pair(
        self,
        input_data: Dict[str, Any],
        prompt_a: str,
        output_a: Any,
        prompt_b: str,
        output_b: Any,
        expected_output: Optional[Any] = None,
    ) -> MetricResult:
        # Compares two outputs and decides which one is better
        raise NotImplementedError
