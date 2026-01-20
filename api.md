# Datagrid

Types:

```python
from datagrid_ai.types import ConverseResponse, Properties
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
)
```

Methods:

- <code title="post /knowledge">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge/knowledge.py">create</a>(\*\*<a href="src/datagrid_ai/types/knowledge_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge/knowledge.py">Knowledge</a></code>
- <code title="get /knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge/knowledge.py">retrieve</a>(knowledge_id) -> <a href="./src/datagrid_ai/types/knowledge/knowledge.py">Knowledge</a></code>
- <code title="patch /knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge/knowledge.py">update</a>(knowledge_id, \*\*<a href="src/datagrid_ai/types/knowledge_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge/knowledge.py">Knowledge</a></code>
- <code title="get /knowledge">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge/knowledge.py">list</a>(\*\*<a href="src/datagrid_ai/types/knowledge_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge/knowledge.py">SyncCursorIDPage[Knowledge]</a></code>
- <code title="delete /knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge/knowledge.py">delete</a>(knowledge_id) -> None</code>
- <code title="post /knowledge/connect">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge/knowledge.py">connect</a>(\*\*<a href="src/datagrid_ai/types/knowledge_connect_params.py">params</a>) -> <a href="./src/datagrid_ai/types/redirect_url_response.py">RedirectURLResponse</a></code>
- <code title="post /knowledge/{knowledge_id}/reindex">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge/knowledge.py">reindex</a>(knowledge_id) -> None</code>

## Tables

Types:

```python
from datagrid_ai.types.knowledge import Table
```

Methods:

- <code title="get /tables/{table_id}">client.knowledge.tables.<a href="./src/datagrid_ai/resources/knowledge/tables/tables.py">retrieve</a>(table_id) -> <a href="./src/datagrid_ai/types/knowledge/table.py">Table</a></code>
- <code title="get /tables">client.knowledge.tables.<a href="./src/datagrid_ai/resources/knowledge/tables/tables.py">list</a>(\*\*<a href="src/datagrid_ai/types/knowledge/table_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge/table.py">SyncCursorIDPage[Table]</a></code>

### Records

Types:

```python
from datagrid_ai.types.knowledge.tables import Record
```

Methods:

- <code title="get /tables/{table_id}/records">client.knowledge.tables.records.<a href="./src/datagrid_ai/resources/knowledge/tables/records.py">list</a>(table_id, \*\*<a href="src/datagrid_ai/types/knowledge/tables/record_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge/tables/record.py">SyncCursorPage[Record]</a></code>

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
from datagrid_ai.types import (
    SearchResultItem,
    SearchResultResource,
    SearchResultResourceType,
    SearchSearchResponse,
)
```

Methods:

- <code title="get /search">client.search.<a href="./src/datagrid_ai/resources/search.py">search</a>(\*\*<a href="src/datagrid_ai/types/search_search_params.py">params</a>) -> <a href="./src/datagrid_ai/types/search_search_response.py">SearchSearchResponse</a></code>

# Agents

Types:

```python
from datagrid_ai.types import Agent
```

Methods:

- <code title="post /agents">client.agents.<a href="./src/datagrid_ai/resources/agents.py">create</a>(\*\*<a href="src/datagrid_ai/types/agent_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agent.py">Agent</a></code>
- <code title="get /agents/{agent_id}">client.agents.<a href="./src/datagrid_ai/resources/agents.py">retrieve</a>(agent_id) -> <a href="./src/datagrid_ai/types/agent.py">Agent</a></code>
- <code title="patch /agents/{agent_id}">client.agents.<a href="./src/datagrid_ai/resources/agents.py">update</a>(agent_id, \*\*<a href="src/datagrid_ai/types/agent_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agent.py">Agent</a></code>
- <code title="get /agents">client.agents.<a href="./src/datagrid_ai/resources/agents.py">list</a>(\*\*<a href="src/datagrid_ai/types/agent_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agent.py">SyncCursorIDPage[Agent]</a></code>
- <code title="delete /agents/{agent_id}">client.agents.<a href="./src/datagrid_ai/resources/agents.py">delete</a>(agent_id) -> None</code>

# Pages

Types:

```python
from datagrid_ai.types import Page
```

Methods:

- <code title="post /pages">client.pages.<a href="./src/datagrid_ai/resources/pages.py">create</a>(\*\*<a href="src/datagrid_ai/types/page_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/page.py">Page</a></code>
- <code title="get /pages/{page_id}">client.pages.<a href="./src/datagrid_ai/resources/pages.py">retrieve</a>(page_id) -> <a href="./src/datagrid_ai/types/page.py">Page</a></code>
- <code title="patch /pages/{page_id}">client.pages.<a href="./src/datagrid_ai/resources/pages.py">update</a>(page_id, \*\*<a href="src/datagrid_ai/types/page_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/page.py">Page</a></code>
- <code title="get /pages">client.pages.<a href="./src/datagrid_ai/resources/pages.py">list</a>(\*\*<a href="src/datagrid_ai/types/page_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/page.py">SyncCursorIDPage[Page]</a></code>
- <code title="delete /pages/{page_id}">client.pages.<a href="./src/datagrid_ai/resources/pages.py">delete</a>(page_id) -> None</code>

# Tools

Types:

```python
from datagrid_ai.types import Tool, ToolDef, ToolName
```

Methods:

- <code title="get /tools/{tool_name}">client.tools.<a href="./src/datagrid_ai/resources/tools.py">retrieve</a>(tool_name) -> <a href="./src/datagrid_ai/types/tool_def.py">ToolDef</a></code>
- <code title="get /tools">client.tools.<a href="./src/datagrid_ai/resources/tools.py">list</a>(\*\*<a href="src/datagrid_ai/types/tool_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/tool_def.py">SyncCursorNamePage[ToolDef]</a></code>

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

# Organization

## Users

Types:

```python
from datagrid_ai.types.organization import OrganizationUser
```

Methods:

- <code title="get /organization/users/{user_id}">client.organization.users.<a href="./src/datagrid_ai/resources/organization/users.py">retrieve</a>(user_id) -> <a href="./src/datagrid_ai/types/organization/organization_user.py">OrganizationUser</a></code>
- <code title="patch /organization/users/{user_id}">client.organization.users.<a href="./src/datagrid_ai/resources/organization/users.py">update</a>(user_id, \*\*<a href="src/datagrid_ai/types/organization/user_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/organization_user.py">OrganizationUser</a></code>
- <code title="get /organization/users">client.organization.users.<a href="./src/datagrid_ai/resources/organization/users.py">list</a>(\*\*<a href="src/datagrid_ai/types/organization/user_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/organization_user.py">SyncCursorIDPage[OrganizationUser]</a></code>

## Teamspaces

Types:

```python
from datagrid_ai.types.organization import Teamspace
```

Methods:

- <code title="post /organization/teamspaces">client.organization.teamspaces.<a href="./src/datagrid_ai/resources/organization/teamspaces/teamspaces.py">create</a>(\*\*<a href="src/datagrid_ai/types/organization/teamspace_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/teamspace.py">Teamspace</a></code>
- <code title="get /organization/teamspaces/{teamspace_id}">client.organization.teamspaces.<a href="./src/datagrid_ai/resources/organization/teamspaces/teamspaces.py">retrieve</a>(teamspace_id) -> <a href="./src/datagrid_ai/types/organization/teamspace.py">Teamspace</a></code>
- <code title="get /organization/teamspaces">client.organization.teamspaces.<a href="./src/datagrid_ai/resources/organization/teamspaces/teamspaces.py">list</a>(\*\*<a href="src/datagrid_ai/types/organization/teamspace_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/teamspace.py">SyncCursorIDPage[Teamspace]</a></code>
- <code title="patch /organization/teamspaces/{teamspace_id}">client.organization.teamspaces.<a href="./src/datagrid_ai/resources/organization/teamspaces/teamspaces.py">patch</a>(teamspace_id, \*\*<a href="src/datagrid_ai/types/organization/teamspace_patch_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/teamspace.py">Teamspace</a></code>

### Invites

Types:

```python
from datagrid_ai.types.organization.teamspaces import TeamspaceInvite
```

Methods:

- <code title="post /organization/teamspaces/{teamspace_id}/invites">client.organization.teamspaces.invites.<a href="./src/datagrid_ai/resources/organization/teamspaces/invites.py">create</a>(teamspace_id, \*\*<a href="src/datagrid_ai/types/organization/teamspaces/invite_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/teamspaces/teamspace_invite.py">TeamspaceInvite</a></code>
- <code title="get /organization/teamspaces/{teamspace_id}/invites/{invite_id}">client.organization.teamspaces.invites.<a href="./src/datagrid_ai/resources/organization/teamspaces/invites.py">retrieve</a>(invite_id, \*, teamspace_id) -> <a href="./src/datagrid_ai/types/organization/teamspaces/teamspace_invite.py">TeamspaceInvite</a></code>
- <code title="get /organization/teamspaces/{teamspace_id}/invites">client.organization.teamspaces.invites.<a href="./src/datagrid_ai/resources/organization/teamspaces/invites.py">list</a>(teamspace_id, \*\*<a href="src/datagrid_ai/types/organization/teamspaces/invite_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/teamspaces/teamspace_invite.py">SyncCursorIDPage[TeamspaceInvite]</a></code>
- <code title="delete /organization/teamspaces/{teamspace_id}/invites/{invite_id}">client.organization.teamspaces.invites.<a href="./src/datagrid_ai/resources/organization/teamspaces/invites.py">delete</a>(invite_id, \*, teamspace_id) -> None</code>

### Users

Types:

```python
from datagrid_ai.types.organization.teamspaces import TeamspaceUser
```

Methods:

- <code title="get /organization/teamspaces/{teamspace_id}/users/{user_id}">client.organization.teamspaces.users.<a href="./src/datagrid_ai/resources/organization/teamspaces/users.py">retrieve</a>(user_id, \*, teamspace_id) -> <a href="./src/datagrid_ai/types/organization/teamspaces/teamspace_user.py">TeamspaceUser</a></code>
- <code title="patch /organization/teamspaces/{teamspace_id}/users/{user_id}">client.organization.teamspaces.users.<a href="./src/datagrid_ai/resources/organization/teamspaces/users.py">update</a>(user_id, \*, teamspace_id, \*\*<a href="src/datagrid_ai/types/organization/teamspaces/user_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/teamspaces/teamspace_user.py">TeamspaceUser</a></code>
- <code title="get /organization/teamspaces/{teamspace_id}/users">client.organization.teamspaces.users.<a href="./src/datagrid_ai/resources/organization/teamspaces/users.py">list</a>(teamspace_id, \*\*<a href="src/datagrid_ai/types/organization/teamspaces/user_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/teamspaces/teamspace_user.py">SyncCursorIDPage[TeamspaceUser]</a></code>
- <code title="delete /organization/teamspaces/{teamspace_id}/users/{user_id}">client.organization.teamspaces.users.<a href="./src/datagrid_ai/resources/organization/teamspaces/users.py">delete</a>(user_id, \*, teamspace_id) -> None</code>

## Credits

Types:

```python
from datagrid_ai.types.organization import CreditsReport
```

Methods:

- <code title="get /organization/credits">client.organization.credits.<a href="./src/datagrid_ai/resources/organization/credits.py">get</a>() -> <a href="./src/datagrid_ai/types/organization/credits_report.py">CreditsReport</a></code>

# Conversations

Types:

```python
from datagrid_ai.types import Conversation
```

Methods:

- <code title="post /conversations">client.conversations.<a href="./src/datagrid_ai/resources/conversations/conversations.py">create</a>(\*\*<a href="src/datagrid_ai/types/conversation_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/conversation.py">Conversation</a></code>
- <code title="get /conversations/{conversation_id}">client.conversations.<a href="./src/datagrid_ai/resources/conversations/conversations.py">retrieve</a>(conversation_id) -> <a href="./src/datagrid_ai/types/conversation.py">Conversation</a></code>
- <code title="get /conversations">client.conversations.<a href="./src/datagrid_ai/resources/conversations/conversations.py">list</a>(\*\*<a href="src/datagrid_ai/types/conversation_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/conversation.py">SyncCursorIDPage[Conversation]</a></code>
- <code title="delete /conversations/{conversation_id}">client.conversations.<a href="./src/datagrid_ai/resources/conversations/conversations.py">delete</a>(conversation_id) -> None</code>

## Messages

Types:

```python
from datagrid_ai.types.conversations import Message
```

Methods:

- <code title="get /conversations/{conversation_id}/messages/{message_id}">client.conversations.messages.<a href="./src/datagrid_ai/resources/conversations/messages.py">retrieve</a>(message_id, \*, conversation_id) -> <a href="./src/datagrid_ai/types/conversations/message.py">Message</a></code>
- <code title="get /conversations/{conversation_id}/messages">client.conversations.messages.<a href="./src/datagrid_ai/resources/conversations/messages.py">list</a>(conversation_id, \*\*<a href="src/datagrid_ai/types/conversations/message_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/conversations/message.py">SyncCursorIDPage[Message]</a></code>

# DataViews

Types:

```python
from datagrid_ai.types import DataView, DataViewListResponse
```

Methods:

- <code title="post /data-views">client.data_views.<a href="./src/datagrid_ai/resources/data_views/data_views.py">create</a>(\*\*<a href="src/datagrid_ai/types/data_view_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/data_view.py">DataView</a></code>
- <code title="get /data-views">client.data_views.<a href="./src/datagrid_ai/resources/data_views/data_views.py">list</a>(\*\*<a href="src/datagrid_ai/types/data_view_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/data_view_list_response.py">DataViewListResponse</a></code>
- <code title="delete /data-views/{data_view_id}">client.data_views.<a href="./src/datagrid_ai/resources/data_views/data_views.py">delete</a>(data_view_id) -> None</code>

## ServiceAccounts

Types:

```python
from datagrid_ai.types.data_views import (
    ServiceAccount,
    ServiceAccountCredentials,
    ServiceAccountListResponse,
)
```

Methods:

- <code title="post /data-views/service-accounts">client.data_views.service_accounts.<a href="./src/datagrid_ai/resources/data_views/service_accounts.py">create</a>(\*\*<a href="src/datagrid_ai/types/data_views/service_account_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/data_views/service_account.py">ServiceAccount</a></code>
- <code title="get /data-views/service-accounts">client.data_views.service_accounts.<a href="./src/datagrid_ai/resources/data_views/service_accounts.py">list</a>(\*\*<a href="src/datagrid_ai/types/data_views/service_account_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/data_views/service_account_list_response.py">ServiceAccountListResponse</a></code>
- <code title="delete /data-views/service-accounts/{service_account_id}">client.data_views.service_accounts.<a href="./src/datagrid_ai/resources/data_views/service_accounts.py">delete</a>(service_account_id) -> None</code>
- <code title="get /data-views/service-accounts/{service_account_id}/credentials">client.data_views.service_accounts.<a href="./src/datagrid_ai/resources/data_views/service_accounts.py">credentials</a>(service_account_id) -> <a href="./src/datagrid_ai/types/data_views/service_account_credentials.py">ServiceAccountCredentials</a></code>

# Beta

## Rewrite

Types:

```python
from datagrid_ai.types.beta import RewriteRequest, RewriteResponse
```

Methods:

- <code title="post /beta/rewrite">client.beta.rewrite.<a href="./src/datagrid_ai/resources/beta/rewrite.py">rewrite_text</a>(\*\*<a href="src/datagrid_ai/types/beta/rewrite_rewrite_text_params.py">params</a>) -> <a href="./src/datagrid_ai/types/beta/rewrite_response.py">RewriteResponse</a></code>
