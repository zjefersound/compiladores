class FixedContentTable:
    def __init__(self, content=None):
        self._content = set(content) if content else set()
    
    def add_item(self, item):
        self._content.add(item)
    
    def remove_item(self, item):
        self._content.discard(item)
    
    def contains(self, item):
        return item in self._content
    
    def contains_case_insensitive(self, item):
        lower_item = item.lower()
        return any(existing.lower() == lower_item for existing in self._content)
    
    def search_prefix(self, prefix):
        return [item for item in self._content if item.startswith(prefix)]
    
    def search_prefix_case_insensitive(self, prefix):
        lower_prefix = prefix.lower()
        return [item for item in self._content if item.lower().startswith(lower_prefix)]
    
    def get_all_items(self):
        return sorted(self._content)
    
    def size(self):
        return len(self._content)
