# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AgentGenerateResponse", "Config", "ConfigTool"]


class ConfigTool(BaseModel):
    tool: Optional[str] = None


class Config(BaseModel):
    custom_prompt: Optional[str] = None
    """Custom instructions (tone, style)"""

    prompt: Optional[str] = None
    """System instructions for the agent"""

    tools: Optional[List[ConfigTool]] = None


class AgentGenerateResponse(BaseModel):
    id: str

    claim_token: str
    """One-time token to create this agent in your account after signing up.

    Pass to `POST /agents/claim`. Expires after 7 days.
    """

    config: Config

    description: str

    emoji: str

    prompt_examples: List[str]

    title: str

    category: Optional[str] = None

    connectors: Optional[List[object]] = None
