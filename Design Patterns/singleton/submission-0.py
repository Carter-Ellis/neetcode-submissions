class Singleton:
    singleton_instance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if (cls.singleton_instance is None):
            cls.singleton_instance = super().__new__(cls)
        return cls.singleton_instance
    def getValue(self) -> str:
        return self.value
    def setValue(self, value: str):
        self.value = value