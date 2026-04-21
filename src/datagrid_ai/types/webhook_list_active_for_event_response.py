# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookListActiveForEventResponse"]


class WebhookListActiveForEventResponse(BaseModel):
    data: List[Webhook]
    """An array containing active webhook subscriptions for the requested event."""

    object: Literal["list"]
