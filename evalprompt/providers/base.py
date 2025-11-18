from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class ModelProvider(ABC):
    """
    Base interface for any model backend capable of generating text.
    Implementations must define how inputs are processed and how outputs are produced.
    """

    @abstractmethod
    def generate(
        self,
        inputs: List[str],
        config: Optional[Dict[str, Any]] = None,
    ) -> List[str]:
        """
        Generate text outputs for the given list of input strings.

        Parameters:
            inputs: List of input strings to process.
            config: Optional configuration dictionary for model parameters.

        Returns:
            A list of output strings, one for each input.
        """
        raise NotImplementedError
