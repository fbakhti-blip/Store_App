class Sample:
    def __init__(self, sample_id, name, description):
        self.sample_id = sample_id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.sample_id, self.name, self.description))


