from abc import ABC,abstractmethod
class ChannelBase(ABC):
    def __init__(self,channel_id,owner_id,name,category,status):
        self.channel_id=channel_id
        self.owner_id=owner_id
        self.name=name
        self.category=category
        self.status=status

    @abstractmethod
    def chechk_monetization_eligibility(self):
        ...

    

class PersonalChhannel(ChannelBase):
    ...

class BrandChannel(ChannelBase):
    ...

class KidsChannel(ChannelBase):
    ...