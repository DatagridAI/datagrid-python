# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .webhook import Webhook

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(Webhook):
    """The `webhook` object represents an outbound webhook subscription."""

    secret: str
    """The signing secret shown only when creating a webhook."""
