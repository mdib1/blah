from googleads import dfp
from googleads import oauth2

def main(client):
  # Initialize appropriate service.
  inventory_service = client.GetService('InventoryService', version='v201505')
  statement = dfp.FilterStatement()

  # Get ad units by statement.
  while True:
    response = inventory_service.getAdUnitsByStatement(
        statement.ToStatement())
    if 'results' in response:
      # Display results.
      for ad_unit in response['results']:
        print ('Ad unit with ID \'%s\' and name \'%s\' was found.'
               % (ad_unit['id'], ad_unit['name']))
      statement.offset += dfp.SUGGESTED_PAGE_LIMIT
    else:
      break

  print '\nNumber of results found: %s' % response['totalResultSetSize']

if __name__ == '__main__':
	yaml_path = r"G:\GitHub\blah\googleads.yaml"
	dfp_client = dfp.DfpClient.LoadFromStorage(path=yaml_path)
	main(dfp_client)

	