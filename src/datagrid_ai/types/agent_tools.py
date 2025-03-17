# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AgentTools"]

AgentTools: TypeAlias = Literal[
    "calendar",
    "schedule_recurring_message_tool",
    "data_classification",
    "data_extraction",
    "schema_info",
    "table_info",
    "connect_data",
    "create_dataset",
    "download_data",
    "data_analysis",
    "image_detection",
    "agent_memory",
    "pdf_extraction",
    "semantic_search",
    "company_prospect_researcher",
    "people_prospect_researcher",
    "web_search",
    "fetch_url",
]
