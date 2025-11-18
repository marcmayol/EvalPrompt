from typing import List, Dict, Any, Optional

from evalprompt.providers.base import ModelProvider


class MockProvider(ModelProvider):
    """
    Simple provider used for testing. It returns a fixed output for each
    input or echoes the input depending on the configuration.
    """

    def __init__(self, mode: str = "echo", fixed_output: str = "mock"):
        """
        mode: "echo" returns the input as output, "fixed" returns fixed_output
        fixed_output: constant string returned when mode is "fixed"
        """
        self.mode = mode
        self.fixed_output = fixed_output

    def generate(
        self,
        inputs: List[str],
        config: Optional[Dict[str, Any]] = None
    ) -> List[str]:
        """
        Generates outputs for a list of input strings according to the mode.
        """
        if self.mode == "fixed":
            return [self.fixed_output for _ in inputs]
        return inputs
