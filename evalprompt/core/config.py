"""Evaluation configuration object for EvalPrompt."""
class EvaluationConfig:
    """Configuration object that defines how an evaluation should be executed."""

    def __init__(self, metrics=None, judge=None, batch_size=1, max_examples=None):
        """
        Initializes the evaluation settings.

        Args:
            metrics: List of metric instances to apply during evaluation.
            judge: Optional judge instance used for model based scoring.
            batch_size: Number of rendered inputs processed per model call.
            max_examples: Optional limit on the number of dataset examples to evaluate.
        """
        self.metrics = metrics or []
        self.judge = judge
        self.batch_size = batch_size
        self.max_examples = max_examples
