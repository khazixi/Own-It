import abc
import dataclasses


@dataclasses.dataclass
class BaseRental(abc.ABC):
    """
    Abstract Base Class
    """
    name: str
    type: str
    owner: str = dataclasses.field(init=False, default=None)
    position: int
    rent: list[int] = dataclasses.field(default_factory=list)
    price: int
    monopoly: bool = dataclasses.field(init=False, default=False)

    @classmethod
    @abc.abstractmethod
    def from_json(cls):
        """
        Takes the data from the json file and creates the dataclass
        """
        pass
