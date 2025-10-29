from repository import SampleRepository


class SampleService:
    sample_repository = SampleRepository()

    @classmethod
    def save(cls, sample):
        return cls.sample_repository.save(sample)

    @classmethod
    def update(cls, sample):
        sample_result = cls.sample_repository.find_by_id(sample.sample_id)
        if sample_result:
            return cls.sample_repository.update(sample)
        else:
            raise Exception("Sample Not Found !!!")

    @classmethod
    def delete(cls, sample_id):
        sample = cls.sample_repository.find_by_id(sample_id)
        if sample:
            cls.sample_repository.delete(sample_id)
            return sample
        else:
            raise Exception("Sample Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.sample_repository.find_all()

    @classmethod
    def find_by_id(cls, sample_id):
        sample = cls.sample_repository.find_by_id(sample_id)
        if sample:
            return sample
        else:
            raise Exception("Sample Not Found !!!")
