# Datagrid

Types:

```python
from datagrid_ai.types import AgentTools, Properties, ConverseResponse
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

# Search

Types:

```python
from datagrid_ai.types import SearchResultItem, SearchResultResource, SearchResultResourceType
```

Methods:

- <code title="get /search">client.search.<a href="./src/datagrid_ai/resources/search.py">search</a>(\*\*<a href="src/datagrid_ai/types/search_search_params.py">params</a>) -> <a href="./src/datagrid_ai/types/search_result_item.py">SyncCursorPage[SearchResultItem]</a></code>
