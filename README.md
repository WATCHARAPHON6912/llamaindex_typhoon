# llamaindex_typhoon

### install  
```sh
pip install git+https://github.com/WATCHARAPHON6912/llamaindex_typhoon.git
```
### example
```python
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,ServiceContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llamaindexTyphoon import Typhoon

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
