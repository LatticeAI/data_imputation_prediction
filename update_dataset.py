from tensorci_client import TensorCI

client = TensorCI()

# Define new records to add to the dataset
new_entries = [
  {
    'orig': 'DXB',
    'dest': 'SFO',
    'name': 'Kelly Smart',
    'occupation': 'Awesome Data Scientist',
    'salary': '100,000,000,000',
    'date': '02/03/18',
    'price': '1000.00'
  },
  {
    'orig': 'DXB',
    'dest': 'SFO',
    'name': 'John Cole',
    'occupation': 'Transformation Project Lead',
    'salary': '100,000,000,000',
    'date': '02/03/18',
    'price': '2000.00'
  }
]

# Update the dataset
resp = client.update_dataset(records=new_entries)

# Parse the response
data = resp.json()

# Print the response
if data.get('ok') is True:
  print(data.get('message'))
else:
 print(data.get('error'))