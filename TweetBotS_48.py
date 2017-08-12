#from bs4 import BeautifulSoup
from twitter import *
#import schedule, time, sys
t=Twitter(auth=OAuth('605285251-P1F5efNk95CnHYHxyFcVLsABCW3cG3pR64jsRNZk','Qx7qTKejt5RMTbI1oajYxEQELFRczWXFgVkImiWpsqNwQ','iiRI3RZhVYRKRpGbe91ZmXgy8',
'hR40sQ7OqJ0Oq9dkCj0uhkp1sp21Ndvn5t9i4gWftKlbVeYB8K'))
tweets="Hi"
t.statuses.update(status=tweets)
