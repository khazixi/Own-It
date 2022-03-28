import dataclasses


@dataclasses.dataclass
class Owner:
    name: str
    position: int
    prop_data: dict[str, int] = dataclasses.field(default_factory=dict)
