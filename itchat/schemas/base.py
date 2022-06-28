import typing
import dataclasses

if typing.TYPE_CHECKING:
    from itchat.client import Client

class APIObject:
    client: "Client" = None
    
    def __post_init__(self) -> None:
        for field in dataclasses.fields(self):
            origin = typing.get_origin(field.type)
            
            data = getattr(self, field.name)
            
            if origin is list and (classes := typing.get_args(field.type)):
                value = [
                    classes[0](data) for data in data
                ]
            else:
                value = field.type(data)
                
            setattr(self, field.name, value)
    
    @classmethod
    def set_client(cls, client: "Client"):
        "Set the client of the APIObject."
        cls.client = client
        
    @classmethod
    def form_dict(cls, data: dict):
        "Form the dict of the APIObject."
        return cls(**data)