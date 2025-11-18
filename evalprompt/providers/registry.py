from typing import Dict, Type

from evalprompt.providers.base import ModelProvider


class ProviderRegistry:
    """
    Registry that stores and provides access to model provider classes.
    Allows registration, retrieval and inspection of available providers.
    """

    def __init__(self) -> None:
        """
        Initialize the provider registry as an empty mapping between provider names and classes.
        """
        self._providers: Dict[str, Type[ModelProvider]] = {}

    def register(self, name: str, provider_cls: Type[ModelProvider]) -> None:
        """
        Register a model provider class under the given name.

        Parameters:
            name: Identifier used to store and retrieve the provider.
            provider_cls: Class implementing the ModelProvider interface.
        """
        self._providers[name] = provider_cls

    def get(self, name: str) -> Type[ModelProvider]:
        """
        Retrieve a model provider class by its registered name.

        Parameters:
            name: Name of the provider to retrieve.

        Returns:
            The provider class associated with the provided name.
        """
        return self._providers[name]

    def available(self) -> Dict[str, Type[ModelProvider]]:
        """
        Return a dictionary containing all registered provider names and their corresponding classes.

        Returns:
            A dictionary mapping provider names to provider classes.
        """
        return dict(self._providers)


provider_registry = ProviderRegistry()
