from abc import ABC,abstractmethod
class ChannelBase(ABC):
    def __init__(self,channel_id,owner_id,name,category,status):
        self.channel_id=channel_id
        self.owner_id=owner_id
        self.name=name
        self.category=category
        self.status='active'
        self.balance=0.0
        

    @abstractmethod
    def calculate_advertising_revenue(self):
        """
        Docstring for calculate_advertising_revenue
        
        :param self: Description
        """
        pass


    

class PersonalChhannel(ChannelBase):
    def __init__(self, channel_id, owner_id, name, category, status,izlenme_sayisi):
        super().__init__(channel_id, owner_id, name, category, status)


class BrandChannel(ChannelBase):
    def __init__(self, channel_id, owner_id, name, category, status):
        super().__init__(channel_id, owner_id, name, category, status)

class KidsChannel(ChannelBase):
    def __init__(self, channel_id, owner_id, name, category, status):
        super().__init__(channel_id, owner_id, name, category, status)