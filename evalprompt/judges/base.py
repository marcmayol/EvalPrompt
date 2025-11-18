from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from evalprompt.core.types import MetricResult


class Judge(ABC):
    """
    Base interface for components that evaluate model outputs.
    Each judge must define a unique name and implement the evaluation methods.
    """

    name: str

    @abstractmethod
    def judge_single(
        self,
        input_data: Dict[str, Any],
        prompt_name: str,
        output: Any,
        expected_output: Optional[Any] = None,
    ) -> MetricResult:
        """
        Evaluate a single model output against optional expected data.

        Parameters:
            input_data: Input used to generate the model output.
            prompt_name: Name of the prompt associated with the output.
            output: Model output to evaluate.
            expected_output: Optional reference output for comparison.

        Returns:
            MetricResult representing the evaluation outcome.
        """
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
        """
        Compare two model outputs and determine which one performs better.

        Parameters:
            input_data: Input used to generate the outputs.
            prompt_a: Name of the first prompt.
            output_a: First model output.
            prompt_b: Name of the second prompt.
            output_b: Second model output.
            expected_output: Optional reference output to guide the comparison.

        Returns:
            MetricResult summarizing the comparison.
        """
        raise NotImplementedError
