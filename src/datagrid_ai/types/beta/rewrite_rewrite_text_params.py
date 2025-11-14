# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RewriteRewriteTextParams"]


class RewriteRewriteTextParams(TypedDict, total=False):
    full_text: Required[str]
    """The full text of the document for context."""

    prompt: Required[str]
    """The prompt with instructions for rewriting the text."""

    text_to_rewrite: Required[str]
    """The text to be rewritten."""
