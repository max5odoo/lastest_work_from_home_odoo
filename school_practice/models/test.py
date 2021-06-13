from datetime import datetime, timedelta
from dateutil.relativedelta import *

date = datetime.now()
print(date)
# 2018-09-24 13:24:04.007620manthan


date = date + relativedelta(months=+1)
print(date)
# 2019-03-24 13:24:04.007620
