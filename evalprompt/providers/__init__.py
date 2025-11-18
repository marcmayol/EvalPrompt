"""
Provider interfaces and loading utilities for EvalPrompt.
"""
from evalprompt.providers.registry import provider_registry
from evalprompt.providers.mock import MockProvider

provider_registry.register("mock", MockProvider)
