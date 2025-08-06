# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .knowledge import Knowledge
from .redirect_url_response import RedirectURLResponse

__all__ = ["KnowledgeCreateResponse"]

KnowledgeCreateResponse: TypeAlias = Union[Knowledge, RedirectURLResponse]
