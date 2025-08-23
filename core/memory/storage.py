class label_lst:
    def __init__(self):
        self.labels = {}
    
    def get_index(self, label: str) -> int:
        if not label in self.labels:
            raise NameError("Label not found")
        return self.labels[label]
    
    def add_label(self, label: str, index: int) -> None:
        self.labels[label] = index

class variables:
    def __init__(self):
        pass
