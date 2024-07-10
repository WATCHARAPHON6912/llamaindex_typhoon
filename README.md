# llamaindex_typhoon

### install  
```sh
pip install git+https://github.com/WATCHARAPHON6912/llamaindex_typhoon.git
```
### example
```python
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,ServiceContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llamaindex_typhoon import Typhoon

embed_model=HuggingFaceEmbedding(model_name='kornwtp/SCT-KD-model-XLMR')
documents=SimpleDirectoryReader("data").load_data()
llm=Typhoon(model="typhoon-v1.5x-70b-instruct",api_key="you_api_key")

service_context=ServiceContext.from_defaults(
    chunk_size=1024,
    llm=llm,
    embed_model=embed_model,
)
index=VectorStoreIndex.from_documents(documents,service_context=service_context)
query_engine = index.as_query_engine(streaming=True)
streaming_response = query_engine.query("you_prompt")
# streaming_response.print_response_stream()
response_txt = ""
for text in streaming_response.response_gen:
    print(text, end="", flush=True)
    response_txt += text
streaming_response.response_txt = response_txt
```
#### MilvusVectorStore create
```python

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llamaindex_typhoon import Typhoon
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.core import Document
documents = SimpleDirectoryReader("data").load_data()
embed_model = HuggingFaceEmbedding(model_name="kornwtp/SCT-KD-model-XLMR")

Settings.embed_model = embed_model
Settings.llm = Typhoon(model="typhoon-v1.5x-70b-instruct",api_key="you_api_key")
vector_store = MilvusVectorStore(
    uri="./milvus.db", dim=768, overwrite=True
)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
# index = VectorStoreIndex.from_documents(storage_context=storage_context,show_progress=True)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context,
    show_progress=True
)
query_engine = index.as_query_engine(streaming=True)

streaming_response = query_engine.query("you_prompt")
# streaming_response.print_response_stream()
response_txt = ""
for text in streaming_response.response_gen:
    print(text, end="", flush=True)
    response_txt += text
streaming_response.response_txt = response_txt
```
#### MilvusVectorStore read
```python

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llamaindex_typhoon import Typhoon
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.core import Document

Settings.embed_model = HuggingFaceEmbedding(model_name="kornwtp/SCT-KD-model-XLMR")
Settings.llm = Typhoon(model="typhoon-v1.5x-70b-instruct",api_key="you_api_key")


vector_store = MilvusVectorStore(
    uri="milvus.db", dim=768
)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    [Document(text="ค้นหาหมายเลข")],
    storage_context,
)
query_engine = index.as_query_engine(streaming=True)

streaming_response = query_engine.query("you_prompt")
# streaming_response.print_response_stream()
response_txt = ""
for text in streaming_response.response_gen:
    print(text, end="", flush=True)
    response_txt += text
streaming_response.response_txt = response_txt
```
