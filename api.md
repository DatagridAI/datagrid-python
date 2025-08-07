# Datagrid

Types:

```python
from datagrid_ai.types import AgentToolItem, AgentTools, Properties, ConverseResponse
```

Methods:

- <code title="post /converse">client.<a href="./src/datagrid_ai/_client.py">converse</a>(\*\*<a href="src/datagrid_ai/types/client_converse_params.py">params</a>) -> <a href="./src/datagrid_ai/types/converse_response.py">ConverseResponse</a></code>

# Knowledge

Types:

```python
from datagrid_ai.types import (
    AttachmentMetadata,
    Knowledge,
    KnowledgeMetadata,
    MessageMetadata,
    RowMetadata,
    TableMetadata,
    KnowledgeUpdateResponse,
)
```

Methods:

- <code title="post /knowledge">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">create</a>(\*\*<a href="src/datagrid_ai/types/knowledge_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge.py">Knowledge</a></code>
- <code title="get /knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">retrieve</a>(knowledge_id) -> <a href="./src/datagrid_ai/types/knowledge.py">Knowledge</a></code>
- <code title="patch /knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">update</a>(knowledge_id, \*\*<a href="src/datagrid_ai/types/knowledge_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge_update_response.py">KnowledgeUpdateResponse</a></code>
- <code title="get /knowledge">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">list</a>(\*\*<a href="src/datagrid_ai/types/knowledge_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge.py">SyncCursorIDPage[Knowledge]</a></code>
- <code title="delete /knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">delete</a>(knowledge_id) -> None</code>
- <code title="post /knowledge/connect">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">connect</a>(\*\*<a href="src/datagrid_ai/types/knowledge_connect_params.py">params</a>) -> <a href="./src/datagrid_ai/types/redirect_url_response.py">RedirectURLResponse</a></code>

# Connections

Types:

```python
from datagrid_ai.types import Connection, RedirectURLResponse
```

Methods:

- <code title="post /connections">client.connections.<a href="./src/datagrid_ai/resources/connections.py">create</a>(\*\*<a href="src/datagrid_ai/types/connection_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/redirect_url_response.py">RedirectURLResponse</a></code>
- <code title="get /connections/{connection_id}">client.connections.<a href="./src/datagrid_ai/resources/connections.py">retrieve</a>(connection_id) -> <a href="./src/datagrid_ai/types/connection.py">Connection</a></code>
- <code title="patch /connections/{connection_id}">client.connections.<a href="./src/datagrid_ai/resources/connections.py">update</a>(connection_id, \*\*<a href="src/datagrid_ai/types/connection_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/connection.py">Connection</a></code>
- <code title="get /connections">client.connections.<a href="./src/datagrid_ai/resources/connections.py">list</a>(\*\*<a href="src/datagrid_ai/types/connection_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/connection.py">SyncCursorIDPage[Connection]</a></code>
- <code title="delete /connections/{connection_id}">client.connections.<a href="./src/datagrid_ai/resources/connections.py">delete</a>(connection_id) -> None</code>

# Connectors

Types:

```python
from datagrid_ai.types import Connector
```

Methods:

- <code title="get /connectors">client.connectors.<a href="./src/datagrid_ai/resources/connectors.py">list</a>(\*\*<a href="src/datagrid_ai/types/connector_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/connector.py">SyncCursorIDPage[Connector]</a></code>

# Files

Types:

```python
from datagrid_ai.types import FileObject
```

Methods:

- <code title="post /files">client.files.<a href="./src/datagrid_ai/resources/files.py">create</a>(\*\*<a href="src/datagrid_ai/types/file_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/file_object.py">FileObject</a></code>
- <code title="get /files/{file_id}">client.files.<a href="./src/datagrid_ai/resources/files.py">retrieve</a>(file_id) -> <a href="./src/datagrid_ai/types/file_object.py">FileObject</a></code>
- <code title="get /files">client.files.<a href="./src/datagrid_ai/resources/files.py">list</a>(\*\*<a href="src/datagrid_ai/types/file_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/file_object.py">SyncCursorIDPage[FileObject]</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/datagrid_ai/resources/files.py">delete</a>(file_id) -> None</code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/datagrid_ai/resources/files.py">content</a>(file_id) -> BinaryAPIResponse</code>

# Secrets

Types:

```python
from datagrid_ai.types import Secret
```

Methods:

- <code title="post /secrets">client.secrets.<a href="./src/datagrid_ai/resources/secrets.py">create</a>(\*\*<a href="src/datagrid_ai/types/secret_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/secret.py">Secret</a></code>
- <code title="get /secrets/{secret_id}">client.secrets.<a href="./src/datagrid_ai/resources/secrets.py">retrieve</a>(secret_id) -> <a href="./src/datagrid_ai/types/secret.py">Secret</a></code>
- <code title="get /secrets">client.secrets.<a href="./src/datagrid_ai/resources/secrets.py">list</a>(\*\*<a href="src/datagrid_ai/types/secret_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/secret.py">SyncCursorIDPage[Secret]</a></code>
- <code title="delete /secrets/{secret_id}">client.secrets.<a href="./src/datagrid_ai/resources/secrets.py">delete</a>(secret_id) -> None</code>

# Search

Types:

```python
from datagrid_ai.types import SearchResultItem, SearchResultResource, SearchResultResourceType
```

Methods:

- <code title="get /search">client.search.<a href="./src/datagrid_ai/resources/search.py">search</a>(\*\*<a href="src/datagrid_ai/types/search_search_params.py">params</a>) -> <a href="./src/datagrid_ai/types/search_result_item.py">SyncCursorPage[SearchResultItem]</a></code>

# Organization

## Teamspaces

Types:

```python
from datagrid_ai.types.organization import Teamspace
```

Methods:

- <code title="post /organization/teamspaces">client.organization.teamspaces.<a href="./src/datagrid_ai/resources/organization/teamspaces.py">create</a>(\*\*<a href="src/datagrid_ai/types/organization/teamspace_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/teamspace.py">Teamspace</a></code>
- <code title="get /organization/teamspaces/{teamspace_id}">client.organization.teamspaces.<a href="./src/datagrid_ai/resources/organization/teamspaces.py">retrieve</a>(teamspace_id) -> <a href="./src/datagrid_ai/types/organization/teamspace.py">Teamspace</a></code>
- <code title="get /organization/teamspaces">client.organization.teamspaces.<a href="./src/datagrid_ai/resources/organization/teamspaces.py">list</a>(\*\*<a href="src/datagrid_ai/types/organization/teamspace_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/teamspace.py">SyncCursorIDPage[Teamspace]</a></code>
- <code title="patch /organization/teamspaces/{teamspace_id}">client.organization.teamspaces.<a href="./src/datagrid_ai/resources/organization/teamspaces.py">patch</a>(teamspace_id, \*\*<a href="src/datagrid_ai/types/organization/teamspace_patch_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/teamspace.py">Teamspace</a></code>

## Credits

Types:

```python
from datagrid_ai.types.organization import CreditsReport
```

Methods:

- <code title="get /organization/credits">client.organization.credits.<a href="./src/datagrid_ai/resources/organization/credits.py">get</a>() -> <a href="./src/datagrid_ai/types/organization/credits_report.py">CreditsReport</a></code>

# Memory

## User

Types:

```python
from datagrid_ai.types.memory import UserMemory, UserListResponse
```

Methods:

- <code title="post /user-memories">client.memory.user.<a href="./src/datagrid_ai/resources/memory/user.py">create</a>(\*\*<a href="src/datagrid_ai/types/memory/user_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/memory/user_memory.py">UserMemory</a></code>
- <code title="get /user-memories">client.memory.user.<a href="./src/datagrid_ai/resources/memory/user.py">list</a>(\*\*<a href="src/datagrid_ai/types/memory/user_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/memory/user_list_response.py">UserListResponse</a></code>
- <code title="delete /user-memories/{user_memory_id}">client.memory.user.<a href="./src/datagrid_ai/resources/memory/user.py">delete</a>(user_memory_id) -> None</code>

# IFrameEvents

Types:

```python
from datagrid_ai.types import (
    ConnectionPayload,
    ErrorPayload,
    IFrameEvent,
    IFrameEventType,
    KnowledgeCreatedPayload,
    ResizePayload,
)
```
