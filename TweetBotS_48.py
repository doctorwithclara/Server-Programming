#from bs4 import BeautifulSoup
from twitter import *
#import schedule, time, sys
t=Twitter(auth=OAuth('605285251-P1F5efNk95CnHYHxyFcVLsABCW3cG3pR64js****','Qx7qTKejt5RMTbI1oajYxEQELFRczWXFgVkImiWps****','iiRI3RZhVYRKRpGbe91Zm****',
'hR40sQ7OqJ0Oq9dkCj0uhkp1sp21Ndvn5t9i4gWftKlbVe****'))
tweets="Hi"
t.statuses.update(status=tweets)
