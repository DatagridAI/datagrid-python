# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SearchTreeResult", "Credits", "CountsByDisplayType", "DisplayItem", "DisplayItemChannelData"]


class Credits(BaseModel):
    """Credit consumption for this search.

    When present, `consumed` reflects the actual variable cost of the retrieval work performed for this request. `null` when the billing write fails or the request is aborted before billing completes.
    """

    consumed: float
    """The number of credits consumed by the operation."""


class CountsByDisplayType(BaseModel):
    """Result counts per display type across the entire result pool."""

    channels: int
    """Number of name-matched channel results."""

    datasets: int
    """Number of dataset results: tables, data records, and name-matched datasets."""

    documents: int
    """
    Number of document results: non-image files and standalone pages (multiple
    matched pages of one file count as a single file).
    """

    images: int
    """Number of image results: files with an `image/*` media type."""


class DisplayItemChannelData(BaseModel):
    """Channel membership and visibility details for channel search results."""

    agent_count: int
    """Number of AI/agent members."""

    channel_type: str
    """One of `channel`, `directMessage`, or `chats`."""

    is_joined: bool
    """Whether the requesting user is a member of this channel."""

    is_private: bool
    """Whether the channel is private."""

    participant_count: int
    """Total number of members (people + agents)."""

    people_count: int
    """Number of human members."""


class DisplayItem(BaseModel):
    """One search result card with no structural children.

    Items arrive in ranked page order; each corresponds to exactly one rendered result.
    """

    id: str
    """
    Stable identifier of the result (document id for retrieval results, entity id
    for dataset/channel supplements).
    """

    display_type: Literal["dataset", "document", "image", "channel"]
    """
    Product-facing grouping of one result card, aligned with the result tabs in the
    Datagrid web app. Derived from the card's structure and media type: tables and
    records are `dataset`, files with an `image/*` media type are `image`, other
    files and pages are `document`, and channels are `channel`.
    """

    kind: Literal["record", "file", "page", "dataset", "channel"]
    """
    The kind of result card: a data record, a file, a single file page, a dataset,
    or a channel.
    """

    object: Literal["search_display_item"]
    """The object type, always `search_display_item`."""

    table_id: str
    """Identifier of the table this result belongs to."""

    body: Optional[str] = None
    """Card body text (matched content snippet)."""

    channel_data: Optional[DisplayItemChannelData] = None
    """Channel membership and visibility details for channel search results."""

    created_at: Optional[str] = None
    """When the underlying item was created."""

    data_lake_item_id: Optional[str] = None
    """Identifier of the data-lake item backing the file."""

    dataset_name: Optional[str] = None
    """Name of the dataset this result belongs to."""

    emoji: Optional[str] = None
    """Emoji icon of the dataset or channel."""

    file_uri: Optional[str] = None
    """Datagrid file URI for file/page media, used to resolve thumbnails and viewers."""

    media_type: Optional[str] = None
    """Media type of the file (e.g. `application/pdf`, `image/png`)."""

    navigation_item_id: Optional[str] = None
    """Identifier of the navigation item for the dataset or channel."""

    page_number: Optional[int] = None
    """1-based page number within the source document, for `page` items."""

    page_url: Optional[str] = None
    """Datagrid file URI scoped to this page, for `page` items."""

    score: Optional[float] = None
    """Relevance score of the result, between 0 and 1."""

    table_fingerprint: Optional[str] = None
    """Fingerprint of the table, used to build dataset URLs."""

    table_name: Optional[str] = None
    """Name of the table this result belongs to."""

    title: Optional[str] = None
    """Card title."""

    total_pages: Optional[int] = None
    """Total number of pages in the source document."""

    updated_at: Optional[str] = None
    """When the underlying item was last updated."""

    url: Optional[str] = None
    """
    Resolved navigation target: a trusted source deep link when available, otherwise
    the dataset URL in the Datagrid web app.
    """


class SearchTreeResult(BaseModel):
    """
    Hierarchical search results grouped by source (datasets, files, pages) with navigation items.
    """

    credits: Optional[Credits] = None
    """Credit consumption for this search.

    When present, `consumed` reflects the actual variable cost of the retrieval work
    performed for this request. `null` when the billing write fails or the request
    is aborted before billing completes.
    """

    data: List[object]
    """Tree nodes representing search results grouped by source.

    Each node contains the matched content, metadata, score, and child nodes for
    hierarchical display.
    """

    has_more: bool
    """Whether more results are available beyond this page.

    Use the `next` cursor to fetch additional results.
    """

    nav_items: List[object]
    """
    Navigation items providing quick links to the datasets, tables, and files that
    matched the query. Each item includes a name, emoji, URL, and type.
    """

    object: Literal["search_tree"]
    """The object type, always `search_tree`."""

    query: str
    """The original search query."""

    counts_by_display_type: Optional[CountsByDisplayType] = None
    """Result counts per display type across the entire result pool."""

    display_items: Optional[List[DisplayItem]] = None
    """
    Canonical ordered result cards for this page — one item per result, in ranked
    order with pinned dataset/channel supplements first. Render these directly
    instead of traversing `data`. Only present when paginated search is enabled for
    the teamspace (Gen Search phase 3).
    """

    next: Optional[str] = None
    """Pagination cursor (numeric offset as string).

    Pass this value as the `next` query parameter to `/search/tree` to fetch the
    next page.
    """

    total_count: Optional[int] = None
    """
    Total number of grouped results in the ranked result pool across all pages
    (capped by the retrieval pool limit). Only present when paginated search is
    enabled for the teamspace (Gen Search phase 3).
    """
