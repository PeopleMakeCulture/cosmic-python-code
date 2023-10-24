from model import Batch
from abc import ABC, abstractmethod


# Q: What is this Abstract Repository we are inheriting from?
# A: Oh it's a thing that we defined, using Abstract Base Classes
# NOTE: AbsRepo is pedagogical - SARepo should work without it
class AbstractRepository(ABC):
    @abstractmethod
    def add(self, batch: Batch) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, ref) -> Batch:
        raise NotImplementedError


class SqlAlchemyRepository():
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, ref):
        return self.session.query(Batch).filter_by(ref=ref).one()

    def list(self):
        return self.session.query(Batch).all()
