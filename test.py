from datetime import datetime, timedelta
import time

s = datetime.now()

time.sleep(5)

e = datetime.now()

print(e - s > timedelta(seconds=5))
