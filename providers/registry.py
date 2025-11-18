from typing import Dict, Type

from evalprompt.providers.base import ModelProvider


class ProviderRegistry:
    # Holds registered model provider classes
    def __init__(self) -> None:
        self._providers: Dict[str, Type[ModelProvider]] = {}

    def register(self, name: str, provider_cls: Type[ModelProvider]) -> None:
        # Registers a provider class under a name
        self._providers[name] = provider_cls

    def get(self, name: str) -> Type[ModelProvider]:
        # Returns the provider class for a given name
        return self._providers[name]

    def available(self) -> Dict[str, Type[ModelProvider]]:
        # Returns all registered providers
        return dict(self._providers)


provider_registry = ProviderRegistry()
