# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VoiceSessionResponse"]


class VoiceSessionResponse(BaseModel):
    agent_id: str
    """The resolved agent ID.

    If no agent was specified in the request, this is the default agent.
    """

    object: Literal["voice.session"]
    """Object type discriminator."""

    start_message: builtins.object
    """Ready-made JSON message to send as the first WebSocket frame after connecting.

    Contains `type: "start"` and a `payload` with all session parameters.
    """

    url: str
    """WebSocket URL to connect to.

    Includes the authentication token as a query parameter.
    """
