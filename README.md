<p align="center">
  <img src="assets/logo.png" alt="EvalPrompt Logo" width="200">
</p>
# EvalPrompt

EvalPrompt is a modular and extensible library designed to evaluate LLM prompts with automatic metrics, judges, and provider backends. The goal is to offer a clean, scalable architecture that supports multiple model providers through a flexible plugin system.

This document reflects the completion of **Phase 1**, which establishes the core foundations of the project.

## Project Status

**Current phase:** Phase 1 completed

**State:** Base architecture implemented with full lint compliance, unit test structure, and foundational interfaces.

## What Phase 1 Includes

Phase 1 establishes the essential building blocks that will support all future development phases. The following components are now completed:

### 1. Minimal but solid package structure

A clean, modular layout with clear separation of responsibilities.

### 2. Core data models

Fully implemented data classes for prompts, examples, model outputs, and metric results.

### 3. Abstract interfaces

* ModelProvider
* Metric
* Judge

These ensure extensibility and encapsulation across the pipeline.

### 4. Registries

* ProviderRegistry
* MetricRegistry

Both support dynamic extension and plugin-based loading in future phases.

### 5. Minimal evaluator (Route A)

A simple evaluator capable of running prompts using a provider and computing metrics.

### 6. Mock provider and initial test suite

A basic mock provider and a first unit test validate the structure and ensure the system is functional.

### 7. Code quality and linting

Pylint score: **10.00/10**

A full cleanup of imports, docstrings, formatting rules, and project configuration has been completed.

## Project Structure

```
evalprompt/
    __init__.py

    core/
        __init__.py
        evaluator.py
        types.py
        config.py

    providers/
        __init__.py
        base.py
        registry.py
        mock_provider.py

    metrics/
        __init__.py
        base.py
        registry.py
        exact_match.py

    judges/
        __init__.py
        base.py

    tests/
        test_evaluator_minimal.py
```

## Logging and Reporting Systems

EvalPrompt will soon incorporate a structured logging system and a robust reporting engine.

### Logging System (coming in Phase 2.5)

A lightweight but powerful logging layer will be introduced to:

* track evaluation runs
* debug provider outputs
* allow per module log levels
* support JSON log formatting for integrations

This logging system will be fully configurable through the central configuration object.

### Reporting Engine (coming in Phase 7)

EvalPrompt will include a built in reporting module capable of:

* generating summary reports for evaluations
* exporting results to JSON, Markdown, or HTML
* aggregating metrics across prompts and datasets
* providing pluggable report generators

These systems will form the backbone of monitoring and analysis in later phases.

## Next Steps

Phase 1 is complete. The next development phases will focus on expanding functionality and turning EvalPrompt into a powerful prompt evaluation tool.

### Upcoming phases

**Phase 2:** Plugin-based provider system using Python entry points

**Phase 3:** ExactMatch metric integrated into a full end to end evaluation

**Phase 4:** Metric system expansion (BLEU, ROUGE, semantic similarity)

**Phase 5:** Judge system and subjective evaluation mechanisms

**Phase 6:** AB testing engine

**Phase 7:** Reporting modules and result exporters

**Phase 8:** Advanced dataset handling

**Phase 9:** Optimisations and optional integrations

**Phase 10:** Full documentation and PyPI publication

EvalPrompt now has a solid, clean foundation. The next phases will build on this base to deliver advanced, production ready evaluation features.
