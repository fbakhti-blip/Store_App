import sqlite3

from model import Sample


class SampleRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, sample):
        self.connect()
        self.cursor.execute("insert into samples (name,description) values (?,?)",
                            [sample.name, sample.description])
        sample.id = self.cursor.lastrowid
        self.connection.commit()
        return sample

    def update(self, sample):
        self.connect()
        self.cursor.execute("update samples set name=?,description=? where id=?",
                            [sample.name, sample.description, sample.sample_id])
        self.connection.commit()
        self.disconnect()
        return sample

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from samples where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from samples")
        sample_list =  [Sample(*sample) for sample in self.cursor.fetchall()]
        self.disconnect()
        return sample_list


    def find_by_id(self, sample_id):
        self.connect()
        self.cursor.execute("select * from samples where id=?", [sample_id])
        sample = self.cursor.fetchone()
        self.disconnect()
        if sample:
            return Sample(*sample)
        return None
