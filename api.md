# Knowledge

Types:

```python
from datagrid_ai.types import Knowledge, KnowledgeUpdateResponse
```

Methods:

- <code title="post /v1/knowledge">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">create</a>(\*\*<a href="src/datagrid_ai/types/knowledge_create_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge.py">Knowledge</a></code>
- <code title="get /v1/knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">retrieve</a>(knowledge_id) -> <a href="./src/datagrid_ai/types/knowledge.py">Knowledge</a></code>
- <code title="patch /v1/knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">update</a>(knowledge_id, \*\*<a href="src/datagrid_ai/types/knowledge_update_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge_update_response.py">KnowledgeUpdateResponse</a></code>
- <code title="get /v1/knowledge">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">list</a>(\*\*<a href="src/datagrid_ai/types/knowledge_list_params.py">params</a>) -> <a href="./src/datagrid_ai/types/knowledge.py">SyncCursorIDPage[Knowledge]</a></code>
- <code title="delete /v1/knowledge/{knowledge_id}">client.knowledge.<a href="./src/datagrid_ai/resources/knowledge.py">delete</a>(knowledge_id) -> None</code>
