"""Tests for the minimal evaluation flow in EvalPrompt."""
from evalprompt.core.evaluator import PromptEvaluator
from evalprompt.core.types import PromptDefinition, EvalExample
from evalprompt.providers.mock_provider import MockProvider

def test_minimal_evaluation_flow():
    """Tests the evaluation pipeline using the real evaluator and exact match metric."""
    provider = MockProvider()

    evaluator = PromptEvaluator(
        model_provider=provider,
        metrics=["exact_match"]
    )

    prompt = PromptDefinition(
        name="test_prompt",
        template="{text}"
    )

    dataset = [
        EvalExample(
            input_data={"text": "hello"},
            expected_output="hello"
        )
    ]

    results = evaluator.evaluate([prompt], dataset)

    assert "by_prompt" in results
    assert "test_prompt" in results["by_prompt"]
    assert "metrics" in results["by_prompt"]["test_prompt"]
    assert "exact_match" in results["by_prompt"]["test_prompt"]["metrics"]
    assert results["by_prompt"]["test_prompt"]["metrics"]["exact_match"] == 1.0
