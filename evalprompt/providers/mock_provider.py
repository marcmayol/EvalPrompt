"""Mock provider used for deterministic testing in EvalPrompt."""

class MockProvider:
    """Mock model provider used for testing the evaluation pipeline."""

    def generate(self, inputs, config=None):
        """
        Returns the input as output, enabling deterministic testing without external models.

        Args:
            inputs: List of input strings to echo back.
            config: Optional provider specific configuration.

        Returns:
            A list of outputs identical to the provided inputs.
        """
        return inputs
