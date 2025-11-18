from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class ModelProvider(ABC):
    # Base interface for any model backend that can generate text
    @abstractmethod
    def generate(
        self,
        inputs: List[str],
        config: Optional[Dict[str, Any]] = None,
    ) -> List[str]:
        # Should return one output string per input string
        raise NotImplementedError
