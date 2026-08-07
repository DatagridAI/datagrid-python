# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentGenerateParams"]


class AgentGenerateParams(TypedDict, total=False):
    prompt: Required[str]
    """Natural language description of the agent you want.

    e.g. "I want an agent that helps my sales team answer product questions and
    draft follow-up emails."
    """
