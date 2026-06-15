# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AgentClaimResponse", "Config", "ConfigTool"]


class ConfigTool(BaseModel):
    tool: Optional[str] = None


class Config(BaseModel):
    custom_prompt: Optional[str] = None

    prompt: Optional[str] = None

    tools: Optional[List[ConfigTool]] = None


class AgentClaimResponse(BaseModel):
    id: str

    category: str

    connectors: List[object]

    description: str

    emoji: str

    prompt_examples: List[str]

    title: str

    config: Optional[Config] = None

    is_curated_template: Optional[bool] = None
