# library inputs
import pandas as pd

# CSVs of Zip Codes: http://federalgovernmentzipcodes.us/
# need to move these CSVs to a centralized place
lkup_zip_path = 'C:/Users/gordon-local/Google Drive/Business/Adelphi Ventures/B+M Geospatial/lookups/'
lkup_zip_full = 'free-zipcode-database.csv'
lkup_zip_prim = 'free-zipcode-database-Primary.csv'

# create data frame
def zipLookup(ztype):
  if ztype == 'all':
    return pd.read_csv(lkup_zip_path + lkup_zip_prim)
  elif ztype == 'primary':
    return pd.read_csv(lkup_zip_path + lkup_zip_full)

# look at data
df = zipLookup('primary')
df.head()

