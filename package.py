#datetime package
import datetime 
year = datetime.datetime.now().year
print(year)
#datetime without subpackage
from datetime import datetime
year = datetime.now().year
print(year)