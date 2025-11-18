from typing import List, Dict, Any

from evalprompt.core.types import PromptDefinition, EvalExample, ModelOutput
from evalprompt.metrics.registry import metric_registry
from evalprompt.core.types import MetricResult


class PromptEvaluator:
    """
    Minimal evaluator for running prompts against a model provider using
    a set of metric names registered in the metric registry.
    """

    def __init__(self, model_provider, metrics: List[str]):
        """
        Initializes the evaluator.
        model_provider: backend that generates outputs from input strings
        metrics: list of metric names to load from the metric registry
        """
        self.model_provider = model_provider
        self.metric_classes = [metric_registry.get(m) for m in metrics]

    def evaluate(
        self,
        prompts: List[PromptDefinition],
        dataset: List[EvalExample]
    ) -> Dict[str, Any]:
        """
        Runs each prompt over the dataset and computes metrics.
        Returns a structured result dict grouped by prompt name.
        """
        results = {"by_prompt": {}, "global": {}}

        for prompt in prompts:
            prompt_outputs = []
            metric_results = []

            rendered_inputs = [prompt.render(ex.input_data) for ex in dataset]
            model_outputs = self.model_provider.generate(rendered_inputs)

            for idx, ex in enumerate(dataset):
                output = ModelOutput(
                    prompt_name=prompt.name,
                    example_id=str(idx),
                    raw_output=model_outputs[idx],
                    metadata=ex.metadata,
                )
                prompt_outputs.append(output)

                for metric_cls in self.metric_classes:
                    metric = metric_cls()
                    metric_result = metric.compute(output.raw_output, ex.expected_output)
                    metric_results.append(metric_result)

            grouped = {}
            for m in metric_results:
                grouped.setdefault(m.metric_name, []).append(m.value)

            prompt_metrics = {
                name: sum(vals) / len(vals)
                for name, vals in grouped.items()
            }

            results["by_prompt"][prompt.name] = {
                "metrics": prompt_metrics,
                "outputs": [
                    {"id": o.example_id, "output": o.raw_output, "metadata": o.metadata}
                    for o in prompt_outputs
                ]
            }

        return results
