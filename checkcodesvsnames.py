#!/usr/bin/python
#
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This code example gets all ad units within a network.
To create ad units, run create_ad_units.py
The LoadFromStorage method is pulling credentials and properties from a
"googleads.yaml" file. By default, it looks for this file in your home
directory. For more information, see the "Caching authentication information"
section of our README.
"""


# Import appropriate modules from the client library.
from googleads import dfp


def main(client):
  # Initialize appropriate service.
  client.network_code = 9517547
  inventory_service = client.GetService('InventoryService', version='v201605')
  statement = dfp.FilterStatement()

  # Get ad units by statement.
  while True:
    response = inventory_service.getAdUnitsByStatement(
        statement.ToStatement())
    if 'results' in response:
      # Display results.
      for ad_unit in response['results']:
        if  ad_unit['name'] != ad_unit['adUnitCode']:
          print ('ID \'%s\' | name | \'%s\' | code | \'%s\' '
                 % (ad_unit['id'], ad_unit['name'], ad_unit['adUnitCode']))   
      statement.offset += dfp.SUGGESTED_PAGE_LIMIT
    else:
      break

  print '\nNumber of results found: %s' % response['totalResultSetSize']

if __name__ == '__main__':
  # Initialize client object.
  yaml_path = r"C:\Users\OAO_NY_03-24-2016\Desktop\work\api\googleads.yaml"
  dfp_client = dfp.DfpClient.LoadFromStorage(path=yaml_path)
  main(dfp_client)