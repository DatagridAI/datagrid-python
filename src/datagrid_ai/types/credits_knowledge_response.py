# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CreditsKnowledgeResponse"]


class CreditsKnowledgeResponse(BaseModel):
    consumed_for_knowledge: float
    """
    The total number of credits consumed for all learning on the knowledge including
    updates.
    """

    consumed_for_learning: float
    """The number of credits consumed whilst learning the knowledge."""
