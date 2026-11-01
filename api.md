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

### Summaries

Types:

```python
from datagrid_ai.types.knowledge.tables import Summary
```

Methods:

- <code title="get /tables/{table_id}/summaries">client.knowledge.tables.summaries.<a href="./src/datagrid_ai/resources/knowledge/tables/summaries.py">list</a>(table_id, \*\*<a href="src/datagrid_ai/types/knowledge/tables/summary_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge/tables/summary.py">SyncCursorPage[Summary]</a></code>

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

# ConnectionProviders

Types:

```python
from datagrid_ai.types import ConnectionProvider
```

Methods:

- <code title="post /connection-providers">client.connection_providers.<a href="./src/datagrid_ai/resources/connection_providers.py">create</a>(\*\*<a href="src/datagrid_ai/types/connection_provider_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/connection_provider.py">ConnectionProvider</a></code>
- <code title="get /connection-providers/{connection_provider_id}">client.connection_providers.<a href="./src/datagrid_ai/resources/connection_providers.py">retrieve</a>(connection_provider_id) -> <a href="./src/datagrid_ai/types/connection_provider.py">ConnectionProvider</a></code>
- <code title="patch /connection-providers/{connection_provider_id}">client.connection_providers.<a href="./src/datagrid_ai/resources/connection_providers.py">update</a>(connection_provider_id, \*\*<a href="src/datagrid_ai/types/connection_provider_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/connection_provider.py">ConnectionProvider</a></code>
- <code title="get /connection-providers">client.connection_providers.<a href="./src/datagrid_ai/resources/connection_providers.py">list</a>(\*\*<a href="src/datagrid_ai/types/connection_provider_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/connection_provider.py">SyncCursorIDPage[ConnectionProvider]</a></code>
- <code title="delete /connection-providers/{connection_provider_id}">client.connection_providers.<a href="./src/datagrid_ai/resources/connection_providers.py">delete</a>(connection_provider_id) -> None</code>

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
- <code title="patch /files/{file_id}">client.files.<a href="./src/datagrid_ai/resources/files.py">update</a>(file_id, \*\*<a href="src/datagrid_ai/types/file_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/file_object.py">FileObject</a></code>
- <code title="get /files">client.files.<a href="./src/datagrid_ai/resources/files.py">list</a>(\*\*<a href="src/datagrid_ai/types/file_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/file_object.py">SyncCursorIDPage[FileObject]</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/datagrid_ai/resources/files.py">delete</a>(file_id) -> None</code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/datagrid_ai/resources/files.py">content</a>(file_id) -> BinaryAPIResponse</code>

# BatchPredictions

Types:

```python
from datagrid_ai.types import (
    BatchPrediction,
    BatchPredictionRequestCounts,
    BatchPredictionResultLine,
    ProblemDetails,
    ValidationProblemDetails,
    ValidationProblemError,
)
```

Methods:

- <code title="post /batch-predictions">client.batch_predictions.<a href="./src/datagrid_ai/resources/batch_predictions.py">create</a>(\*\*<a href="src/datagrid_ai/types/batch_prediction_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/batch_prediction.py">BatchPrediction</a></code>
- <code title="get /batch-predictions/{batch_prediction_id}">client.batch_predictions.<a href="./src/datagrid_ai/resources/batch_predictions.py">retrieve</a>(batch_prediction_id) -> <a href="./src/datagrid_ai/types/batch_prediction.py">BatchPrediction</a></code>
- <code title="get /batch-predictions">client.batch_predictions.<a href="./src/datagrid_ai/resources/batch_predictions.py">list</a>(\*\*<a href="src/datagrid_ai/types/batch_prediction_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/batch_prediction.py">SyncAfterCursorPage[BatchPrediction]</a></code>
- <code title="post /batch-predictions/{batch_prediction_id}/cancel">client.batch_predictions.<a href="./src/datagrid_ai/resources/batch_predictions.py">cancel</a>(batch_prediction_id) -> <a href="./src/datagrid_ai/types/batch_prediction.py">BatchPrediction</a></code>
- <code title="get /batch-predictions/{batch_prediction_id}/results">client.batch_predictions.<a href="./src/datagrid_ai/resources/batch_predictions.py">retrieve_results</a>(batch_prediction_id) -> <a href="./src/datagrid_ai/types/batch_prediction_result_line.py">JSONLDecoder[BatchPredictionResultLine]</a></code>

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

# Webhooks

Types:

```python
from datagrid_ai.types import (
    Webhook,
    WebhookEvent,
    WebhookCreateResponse,
    WebhookListActiveForEventResponse,
)
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/datagrid_ai/resources/webhooks.py">create</a>(\*\*<a href="src/datagrid_ai/types/webhook_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /webhooks/{webhook_id}">client.webhooks.<a href="./src/datagrid_ai/resources/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/datagrid_ai/types/webhook.py">Webhook</a></code>
- <code title="patch /webhooks/{webhook_id}">client.webhooks.<a href="./src/datagrid_ai/resources/webhooks.py">update</a>(webhook_id, \*\*<a href="src/datagrid_ai/types/webhook_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/webhook.py">Webhook</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/datagrid_ai/resources/webhooks.py">list</a>(\*\*<a href="src/datagrid_ai/types/webhook_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/webhook.py">SyncWebhookCursorPage[Webhook]</a></code>
- <code title="delete /webhooks/{webhook_id}">client.webhooks.<a href="./src/datagrid_ai/resources/webhooks.py">delete</a>(webhook_id) -> None</code>
- <code title="get /webhooks/active">client.webhooks.<a href="./src/datagrid_ai/resources/webhooks.py">list_active_for_event</a>(\*\*<a href="src/datagrid_ai/types/webhook_list_active_for_event_params.py">params</a>) -> <a href="./src/datagrid_ai/types/webhook_list_active_for_event_response.py">WebhookListActiveForEventResponse</a></code>

# Search

Types:

```python
from datagrid_ai.types import (
    AISource,
    SearchAIRequestBody,
    SearchAIResult,
    SearchResultItem,
    SearchResultResource,
    SearchResultResourceType,
    SearchTreeResult,
    SearchSearchResponse,
)
```

Methods:

- <code title="get /search">client.search.<a href="./src/datagrid_ai/resources/search.py">search</a>(\*\*<a href="src/datagrid_ai/types/search_search_params.py">params</a>) -> <a href="./src/datagrid_ai/types/search_search_response.py">SearchSearchResponse</a></code>
- <code title="post /search/ai">client.search.<a href="./src/datagrid_ai/resources/search.py">search_ai</a>(\*\*<a href="src/datagrid_ai/types/search_search_ai_params.py">params</a>) -> <a href="./src/datagrid_ai/types/search_ai_result.py">SearchAIResult</a></code>
- <code title="get /search/tree">client.search.<a href="./src/datagrid_ai/resources/search.py">search_tree</a>(\*\*<a href="src/datagrid_ai/types/search_search_tree_params.py">params</a>) -> <a href="./src/datagrid_ai/types/search_tree_result.py">SearchTreeResult</a></code>

# Skills

Types:

```python
from datagrid_ai.types import (
    BuiltinSkill,
    Skill,
    SkillDraft,
    SkillGenerateResponse,
    SkillListBuiltinsResponse,
)
```

Methods:

- <code title="post /skills">client.skills.<a href="./src/datagrid_ai/resources/skills.py">create</a>(\*\*<a href="src/datagrid_ai/types/skill_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/skill.py">Skill</a></code>
- <code title="get /skills/{skill_id}">client.skills.<a href="./src/datagrid_ai/resources/skills.py">retrieve</a>(skill_id) -> <a href="./src/datagrid_ai/types/skill.py">Skill</a></code>
- <code title="patch /skills/{skill_id}">client.skills.<a href="./src/datagrid_ai/resources/skills.py">update</a>(skill_id, \*\*<a href="src/datagrid_ai/types/skill_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/skill.py">Skill</a></code>
- <code title="get /skills">client.skills.<a href="./src/datagrid_ai/resources/skills.py">list</a>(\*\*<a href="src/datagrid_ai/types/skill_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/skill.py">SyncCursorIDPage[Skill]</a></code>
- <code title="delete /skills/{skill_id}">client.skills.<a href="./src/datagrid_ai/resources/skills.py">delete</a>(skill_id) -> None</code>
- <code title="post /skills/{skill_id}/clone">client.skills.<a href="./src/datagrid_ai/resources/skills.py">clone</a>(skill_id) -> <a href="./src/datagrid_ai/types/skill.py">Skill</a></code>
- <code title="post /skills/{skill_id}/demote">client.skills.<a href="./src/datagrid_ai/resources/skills.py">demote</a>(skill_id) -> <a href="./src/datagrid_ai/types/skill.py">Skill</a></code>
- <code title="post /skills/generate">client.skills.<a href="./src/datagrid_ai/resources/skills.py">generate</a>(\*\*<a href="src/datagrid_ai/types/skill_generate_params.py">params</a>) -> <a href="./src/datagrid_ai/types/skill_generate_response.py">SkillGenerateResponse</a></code>
- <code title="get /skills/builtin">client.skills.<a href="./src/datagrid_ai/resources/skills.py">list_builtins</a>() -> <a href="./src/datagrid_ai/types/skill_list_builtins_response.py">SkillListBuiltinsResponse</a></code>
- <code title="post /skills/builtin/{builtin_key}/override">client.skills.<a href="./src/datagrid_ai/resources/skills.py">override_builtin</a>(builtin_key) -> <a href="./src/datagrid_ai/types/skill.py">Skill</a></code>
- <code title="post /skills/{skill_id}/promote">client.skills.<a href="./src/datagrid_ai/resources/skills.py">promote</a>(skill_id) -> <a href="./src/datagrid_ai/types/skill.py">Skill</a></code>
- <code title="post /skills/builtin/{builtin_key}/reset">client.skills.<a href="./src/datagrid_ai/resources/skills.py">reset_builtin_override</a>(builtin_key) -> None</code>

# Agents

Types:

```python
from datagrid_ai.types import Agent, AgentListItem, AgentClaimResponse, AgentGenerateResponse
```

Methods:

- <code title="post /agents">client.agents.<a href="./src/datagrid_ai/resources/agents/agents.py">create</a>(\*\*<a href="src/datagrid_ai/types/agent_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agent.py">Agent</a></code>
- <code title="get /agents/{agent_id}">client.agents.<a href="./src/datagrid_ai/resources/agents/agents.py">retrieve</a>(agent_id) -> <a href="./src/datagrid_ai/types/agent.py">Agent</a></code>
- <code title="patch /agents/{agent_id}">client.agents.<a href="./src/datagrid_ai/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/datagrid_ai/types/agent_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agent.py">Agent</a></code>
- <code title="get /agents">client.agents.<a href="./src/datagrid_ai/resources/agents/agents.py">list</a>(\*\*<a href="src/datagrid_ai/types/agent_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agent_list_item.py">SyncCursorIDPage[AgentListItem]</a></code>
- <code title="delete /agents/{agent_id}">client.agents.<a href="./src/datagrid_ai/resources/agents/agents.py">delete</a>(agent_id) -> None</code>
- <code title="post /agents/claim">client.agents.<a href="./src/datagrid_ai/resources/agents/agents.py">claim</a>(\*\*<a href="src/datagrid_ai/types/agent_claim_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agent_claim_response.py">AgentClaimResponse</a></code>
- <code title="post /agents/generate">client.agents.<a href="./src/datagrid_ai/resources/agents/agents.py">generate</a>(\*\*<a href="src/datagrid_ai/types/agent_generate_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agent_generate_response.py">AgentGenerateResponse</a></code>

## Automations

Types:

```python
from datagrid_ai.types.agents import Automation
```

Methods:

- <code title="post /agents/{agent_id}/automations">client.agents.automations.<a href="./src/datagrid_ai/resources/agents/automations.py">create</a>(agent_id, \*\*<a href="src/datagrid_ai/types/agents/automation_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agents/automation.py">Automation</a></code>
- <code title="get /agents/{agent_id}/automations/{automation_id}">client.agents.automations.<a href="./src/datagrid_ai/resources/agents/automations.py">retrieve</a>(automation_id, \*, agent_id) -> <a href="./src/datagrid_ai/types/agents/automation.py">Automation</a></code>
- <code title="patch /agents/{agent_id}/automations/{automation_id}">client.agents.automations.<a href="./src/datagrid_ai/resources/agents/automations.py">update</a>(automation_id, \*, agent_id, \*\*<a href="src/datagrid_ai/types/agents/automation_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agents/automation.py">Automation</a></code>
- <code title="get /agents/{agent_id}/automations">client.agents.automations.<a href="./src/datagrid_ai/resources/agents/automations.py">list</a>(agent_id, \*\*<a href="src/datagrid_ai/types/agents/automation_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agents/automation.py">SyncCursorIDPage[Automation]</a></code>
- <code title="delete /agents/{agent_id}/automations/{automation_id}">client.agents.automations.<a href="./src/datagrid_ai/resources/agents/automations.py">delete</a>(automation_id, \*, agent_id) -> None</code>

## EventTriggers

Types:

```python
from datagrid_ai.types.agents import (
    AgentEventTrigger,
    EventTriggerCreateResponse,
    EventTriggerUpdateResponse,
    EventTriggerListResponse,
)
```

Methods:

- <code title="post /agents/{agent_id}/event-triggers">client.agents.event_triggers.<a href="./src/datagrid_ai/resources/agents/event_triggers.py">create</a>(agent_id, \*\*<a href="src/datagrid_ai/types/agents/event_trigger_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agents/event_trigger_create_response.py">EventTriggerCreateResponse</a></code>
- <code title="patch /agents/{agent_id}/event-triggers/{trigger_id}">client.agents.event_triggers.<a href="./src/datagrid_ai/resources/agents/event_triggers.py">update</a>(trigger_id, \*, agent_id, \*\*<a href="src/datagrid_ai/types/agents/event_trigger_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/agents/event_trigger_update_response.py">EventTriggerUpdateResponse</a></code>
- <code title="get /agents/{agent_id}/event-triggers">client.agents.event_triggers.<a href="./src/datagrid_ai/resources/agents/event_triggers.py">list</a>(agent_id) -> <a href="./src/datagrid_ai/types/agents/event_trigger_list_response.py">EventTriggerListResponse</a></code>
- <code title="delete /agents/{agent_id}/event-triggers/{trigger_id}">client.agents.event_triggers.<a href="./src/datagrid_ai/resources/agents/event_triggers.py">delete</a>(trigger_id, \*, agent_id) -> None</code>

# Channels

Types:

```python
from datagrid_ai.types import (
    Channel,
    ChannelMember,
    ChannelMessage,
    ChannelThread,
    ChannelAddMembersResponse,
)
```

Methods:

- <code title="post /channels">client.channels.<a href="./src/datagrid_ai/resources/channels.py">create</a>(\*\*<a href="src/datagrid_ai/types/channel_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel.py">Channel</a></code>
- <code title="get /channels/{channel_id}">client.channels.<a href="./src/datagrid_ai/resources/channels.py">retrieve</a>(channel_id) -> <a href="./src/datagrid_ai/types/channel.py">Channel</a></code>
- <code title="patch /channels/{channel_id}">client.channels.<a href="./src/datagrid_ai/resources/channels.py">update</a>(channel_id, \*\*<a href="src/datagrid_ai/types/channel_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel.py">Channel</a></code>
- <code title="get /channels">client.channels.<a href="./src/datagrid_ai/resources/channels.py">list</a>(\*\*<a href="src/datagrid_ai/types/channel_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel.py">SyncCursorIDPage[Channel]</a></code>
- <code title="post /channels/{channel_id}/members">client.channels.<a href="./src/datagrid_ai/resources/channels.py">add_members</a>(channel_id, \*\*<a href="src/datagrid_ai/types/channel_add_members_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel_add_members_response.py">ChannelAddMembersResponse</a></code>
- <code title="post /channels/{channel_id}/messages/{message_id}/reactions">client.channels.<a href="./src/datagrid_ai/resources/channels.py">add_reaction</a>(message_id, \*, channel_id, \*\*<a href="src/datagrid_ai/types/channel_add_reaction_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel_message.py">ChannelMessage</a></code>
- <code title="post /channels/{channel_id}/messages">client.channels.<a href="./src/datagrid_ai/resources/channels.py">create_message</a>(channel_id, \*\*<a href="src/datagrid_ai/types/channel_create_message_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel_message.py">ChannelMessage</a></code>
- <code title="post /channels/{channel_id}/messages/{message_id}/threads">client.channels.<a href="./src/datagrid_ai/resources/channels.py">create_thread</a>(message_id, \*, channel_id) -> <a href="./src/datagrid_ai/types/channel_thread.py">ChannelThread</a></code>
- <code title="post /channels/{channel_id}/threads/{thread_id}/messages">client.channels.<a href="./src/datagrid_ai/resources/channels.py">create_thread_message</a>(thread_id, \*, channel_id, \*\*<a href="src/datagrid_ai/types/channel_create_thread_message_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel_message.py">ChannelMessage</a></code>
- <code title="get /channels/{channel_id}/members">client.channels.<a href="./src/datagrid_ai/resources/channels.py">list_members</a>(channel_id, \*\*<a href="src/datagrid_ai/types/channel_list_members_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel_member.py">SyncCursorIDPage[ChannelMember]</a></code>
- <code title="get /channels/{channel_id}/messages">client.channels.<a href="./src/datagrid_ai/resources/channels.py">list_messages</a>(channel_id, \*\*<a href="src/datagrid_ai/types/channel_list_messages_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel_message.py">SyncCursorIDPage[ChannelMessage]</a></code>
- <code title="get /channels/{channel_id}/threads/{thread_id}/messages">client.channels.<a href="./src/datagrid_ai/resources/channels.py">list_thread_messages</a>(thread_id, \*, channel_id, \*\*<a href="src/datagrid_ai/types/channel_list_thread_messages_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel_message.py">SyncCursorIDPage[ChannelMessage]</a></code>
- <code title="get /channels/{channel_id}/threads">client.channels.<a href="./src/datagrid_ai/resources/channels.py">list_threads</a>(channel_id, \*\*<a href="src/datagrid_ai/types/channel_list_threads_params.py">params</a>) -> <a href="./src/datagrid_ai/types/channel_thread.py">SyncCursorIDPage[ChannelThread]</a></code>
- <code title="delete /channels/{channel_id}/members/{member_id}">client.channels.<a href="./src/datagrid_ai/resources/channels.py">remove_member</a>(member_id, \*, channel_id) -> None</code>
- <code title="delete /channels/{channel_id}/messages/{message_id}/reactions/{reaction}">client.channels.<a href="./src/datagrid_ai/resources/channels.py">remove_reaction</a>(reaction, \*, channel_id, message_id) -> <a href="./src/datagrid_ai/types/channel_message.py">ChannelMessage</a></code>
- <code title="get /channels/{channel_id}/threads/{thread_id}">client.channels.<a href="./src/datagrid_ai/resources/channels.py">retrieve_thread</a>(thread_id, \*, channel_id) -> <a href="./src/datagrid_ai/types/channel_thread.py">ChannelThread</a></code>

# Identity

Types:

```python
from datagrid_ai.types import Identity, IdentityProcore, IdentityTeamspace
```

Methods:

- <code title="get /identity">client.identity.<a href="./src/datagrid_ai/resources/identity.py">retrieve</a>() -> <a href="./src/datagrid_ai/types/identity.py">Identity</a></code>

# Procore

Types:

```python
from datagrid_ai.types import ProcoreCompany, ProcoreCompanyList, ProcoreProject, ProcoreProjectList
```

Methods:

- <code title="get /procore/companies">client.procore.<a href="./src/datagrid_ai/resources/procore.py">list_companies</a>(\*\*<a href="src/datagrid_ai/types/procore_list_companies_params.py">params</a>) -> <a href="./src/datagrid_ai/types/procore_company_list.py">ProcoreCompanyList</a></code>
- <code title="get /procore/companies/{company_id}/projects">client.procore.<a href="./src/datagrid_ai/resources/procore.py">list_projects</a>(company_id, \*\*<a href="src/datagrid_ai/types/procore_list_projects_params.py">params</a>) -> <a href="./src/datagrid_ai/types/procore_project_list.py">ProcoreProjectList</a></code>

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

# Models

Types:

```python
from datagrid_ai.types import Model, ModelListResponse
```

Methods:

- <code title="get /models">client.models.<a href="./src/datagrid_ai/resources/models.py">list</a>() -> <a href="./src/datagrid_ai/types/model_list_response.py">ModelListResponse</a></code>

# Memory

## User

Types:

```python
from datagrid_ai.types.memory import UserMemory, UserCreateResponse, UserListResponse
```

Methods:

- <code title="post /user-memories">client.memory.user.<a href="./src/datagrid_ai/resources/memory/user.py">create</a>(\*\*<a href="src/datagrid_ai/types/memory/user_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/memory/user_create_response.py">UserCreateResponse</a></code>
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

## McpServers

Types:

```python
from datagrid_ai.types.organization import (
    CreateMcpServerRequest,
    HandleMcpOAuthCallbackRequest,
    HandleMcpOAuthCallbackResponse,
    ListMcpServersResponse,
    McpServer,
    StartMcpOAuthRequest,
    StartMcpOAuthResponse,
    UpdateMcpServerRequest,
)
```

Methods:

- <code title="post /organization/mcp-servers">client.organization.mcp_servers.<a href="./src/datagrid_ai/resources/organization/mcp_servers.py">create</a>(\*\*<a href="src/datagrid_ai/types/organization/mcp_server_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/mcp_server.py">McpServer</a></code>
- <code title="get /organization/mcp-servers/{server_id}">client.organization.mcp_servers.<a href="./src/datagrid_ai/resources/organization/mcp_servers.py">retrieve</a>(server_id) -> <a href="./src/datagrid_ai/types/organization/mcp_server.py">McpServer</a></code>
- <code title="patch /organization/mcp-servers/{server_id}">client.organization.mcp_servers.<a href="./src/datagrid_ai/resources/organization/mcp_servers.py">update</a>(server_id, \*\*<a href="src/datagrid_ai/types/organization/mcp_server_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/mcp_server.py">McpServer</a></code>
- <code title="get /organization/mcp-servers">client.organization.mcp_servers.<a href="./src/datagrid_ai/resources/organization/mcp_servers.py">list</a>() -> <a href="./src/datagrid_ai/types/organization/list_mcp_servers_response.py">ListMcpServersResponse</a></code>
- <code title="delete /organization/mcp-servers/{server_id}">client.organization.mcp_servers.<a href="./src/datagrid_ai/resources/organization/mcp_servers.py">delete</a>(server_id) -> None</code>
- <code title="post /organization/mcp-servers/{server_id}/oauth-callback">client.organization.mcp_servers.<a href="./src/datagrid_ai/resources/organization/mcp_servers.py">handle_oauth_callback</a>(server_id, \*\*<a href="src/datagrid_ai/types/organization/mcp_server_handle_oauth_callback_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/handle_mcp_oauth_callback_response.py">HandleMcpOAuthCallbackResponse</a></code>
- <code title="post /organization/mcp-servers/{server_id}/start-oauth">client.organization.mcp_servers.<a href="./src/datagrid_ai/resources/organization/mcp_servers.py">start_oauth</a>(server_id, \*\*<a href="src/datagrid_ai/types/organization/mcp_server_start_oauth_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/start_mcp_oauth_response.py">StartMcpOAuthResponse</a></code>

## Credits

Types:

```python
from datagrid_ai.types.organization import CreditsReport
```

Methods:

- <code title="get /organization/credits">client.organization.credits.<a href="./src/datagrid_ai/resources/organization/credits.py">get</a>() -> <a href="./src/datagrid_ai/types/organization/credits_report.py">CreditsReport</a></code>

## Reports

### UserCreditsConsumption

Types:

```python
from datagrid_ai.types.organization.reports import UserCreditConsumption, UserCreditConsumptionList
```

Methods:

- <code title="get /organization/reports/user-credits-consumption">client.organization.reports.user_credits_consumption.<a href="./src/datagrid_ai/resources/organization/reports/user_credits_consumption.py">list</a>(\*\*<a href="src/datagrid_ai/types/organization/reports/user_credits_consumption_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/reports/user_credit_consumption_list.py">UserCreditConsumptionList</a></code>

### ConsumptionBreakdown

Types:

```python
from datagrid_ai.types.organization.reports import ConsumptionBreakdown, ConsumptionBreakdownList
```

Methods:

- <code title="get /organization/reports/consumption-breakdown">client.organization.reports.consumption_breakdown.<a href="./src/datagrid_ai/resources/organization/reports/consumption_breakdown.py">list</a>(\*\*<a href="src/datagrid_ai/types/organization/reports/consumption_breakdown_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/organization/reports/consumption_breakdown_list.py">ConsumptionBreakdownList</a></code>

# Conversations

Types:

```python
from datagrid_ai.types import Conversation, ConversationSortField
```

Methods:

- <code title="post /conversations">client.conversations.<a href="./src/datagrid_ai/resources/conversations/conversations.py">create</a>(\*\*<a href="src/datagrid_ai/types/conversation_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/conversation.py">Conversation</a></code>
- <code title="get /conversations/{conversation_id}">client.conversations.<a href="./src/datagrid_ai/resources/conversations/conversations.py">retrieve</a>(conversation_id) -> <a href="./src/datagrid_ai/types/conversation.py">Conversation</a></code>
- <code title="patch /conversations/{conversation_id}">client.conversations.<a href="./src/datagrid_ai/resources/conversations/conversations.py">update</a>(conversation_id, \*\*<a href="src/datagrid_ai/types/conversation_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/conversation.py">Conversation</a></code>
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
- <code title="post /conversations/{conversation_id}/messages/{message_id}">client.conversations.messages.<a href="./src/datagrid_ai/resources/conversations/messages.py">submit_feedback</a>(message_id, \*, conversation_id, \*\*<a href="src/datagrid_ai/types/conversations/message_submit_feedback_params.py">params</a>) -> None</code>

# DataViews

Types:

```python
from datagrid_ai.types import DataView, DataViewCreateResponse, DataViewListResponse
```

Methods:

- <code title="post /data-views">client.data_views.<a href="./src/datagrid_ai/resources/data_views/data_views.py">create</a>(\*\*<a href="src/datagrid_ai/types/data_view_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/data_view_create_response.py">DataViewCreateResponse</a></code>
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

## Converse

Types:

```python
from datagrid_ai.types.beta import BetaConverseRequest
```

Methods:

- <code title="post /beta/converse">client.beta.converse.<a href="./src/datagrid_ai/resources/beta/converse.py">converse</a>(\*\*<a href="src/datagrid_ai/types/beta/converse_converse_params.py">params</a>) -> <a href="./src/datagrid_ai/types/converse_response.py">ConverseResponse</a></code>

## Rewrite

Types:

```python
from datagrid_ai.types.beta import RewriteRequest, RewriteResponse
```

Methods:

- <code title="post /beta/rewrite">client.beta.rewrite.<a href="./src/datagrid_ai/resources/beta/rewrite.py">rewrite_text</a>(\*\*<a href="src/datagrid_ai/types/beta/rewrite_rewrite_text_params.py">params</a>) -> <a href="./src/datagrid_ai/types/beta/rewrite_response.py">RewriteResponse</a></code>

# Voice

Types:

```python
from datagrid_ai.types import VoiceSessionRequest, VoiceSessionResponse, VoiceWebsocketMessage
```

Methods:

- <code title="post /voice">client.voice.<a href="./src/datagrid_ai/resources/voice/voice.py">start_session</a>(\*\*<a href="src/datagrid_ai/types/voice_start_session_params.py">params</a>) -> <a href="./src/datagrid_ai/types/voice_session_response.py">VoiceSessionResponse</a></code>

## OrchestratorTasks

Types:

```python
from datagrid_ai.types.voice import VoiceOrchestratorTask, VoiceOrchestratorTaskList
```

Methods:

- <code title="get /voice-orchestrator/tasks/{task_id}">client.voice.orchestrator_tasks.<a href="./src/datagrid_ai/resources/voice/orchestrator_tasks.py">retrieve</a>(task_id) -> <a href="./src/datagrid_ai/types/voice/voice_orchestrator_task.py">VoiceOrchestratorTask</a></code>
- <code title="get /voice-orchestrator/tasks">client.voice.orchestrator_tasks.<a href="./src/datagrid_ai/resources/voice/orchestrator_tasks.py">list</a>(\*\*<a href="src/datagrid_ai/types/voice/orchestrator_task_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/voice/voice_orchestrator_task_list.py">VoiceOrchestratorTaskList</a></code>
- <code title="patch /voice-orchestrator/tasks/{task_id}/acknowledge">client.voice.orchestrator_tasks.<a href="./src/datagrid_ai/resources/voice/orchestrator_tasks.py">acknowledge</a>(task_id) -> <a href="./src/datagrid_ai/types/voice/voice_orchestrator_task.py">VoiceOrchestratorTask</a></code>
- <code title="patch /voice-orchestrator/tasks/{task_id}/cancel">client.voice.orchestrator_tasks.<a href="./src/datagrid_ai/resources/voice/orchestrator_tasks.py">cancel</a>(task_id) -> <a href="./src/datagrid_ai/types/voice/voice_orchestrator_task.py">VoiceOrchestratorTask</a></code>
