# Datagrid

Types:

```python
from datagrid_ai.types import Properties, ConverseResponse
```

Methods:

- <code title="post /converse">client.<a href="./src/datagrid_ai/_client.py">converse</a>(\*\*<a href="src/datagrid_ai/types/client_converse_params.py">params</a>) -> <a href="./src/datagrid_ai/types/converse_response.py">ConverseResponse</a></code>

# Knowledge

Types:

```python
from datagrid_ai.types import Knowledge, KnowledgeUpdateResponse
```

Methods:

- <code title="post /knowledge">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">create</a>(\*\*<a href="src/datagrid_ai/types/knowledge_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge.py">Knowledge</a></code>
- <code title="get /knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">retrieve</a>(knowledge_id) -> <a href="./src/datagrid_ai/types/knowledge.py">Knowledge</a></code>
- <code title="patch /knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">update</a>(knowledge_id, \*\*<a href="src/datagrid_ai/types/knowledge_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge_update_response.py">KnowledgeUpdateResponse</a></code>
- <code title="get /knowledge">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">list</a>(\*\*<a href="src/datagrid_ai/types/knowledge_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge.py">SyncCursorIDPage[Knowledge]</a></code>
- <code title="delete /knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">delete</a>(knowledge_id) -> None</code>

# Health

Methods:

- <code title="get /health">client.health.<a href="./src/datagrid_ai/resources/health.py">check_api_health</a>() -> None</code>
