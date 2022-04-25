import json
from elasticsearch import Elasticsearch


class SearchClient:
    def __init__(self, URI):
        self.es = Elasticsearch(URI)

    def get_or_create_index(self, index_name):
        if not self.es.indices.exists(index=index_name):
            return self.es.indices.create(index=index_name)
    
    def ingest_data(self, index_name, data):
        self.es.index(index=index_name, body=data)

    def search_data(self, index_name, query):
        search_object = {'query': {'match': {'document': query}}}
        string_query = json.dumps(search_object)
        return self.es.search(index=index_name, body=string_query)