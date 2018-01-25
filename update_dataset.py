from tensorci import TensorCI


def update_dataset():
  client = TensorCI()

  # Define new records to add to the dataset
  new_entries = [
    {
      'name': 'Tyler',
      'email': 'tyler@gmail.com'
    },
    {
      'name': 'Sam',
      'email': 'sam@gmail.com'
    }
  ]

  # Update the dataset
  resp = client.update_dataset(records=new_entries)

  # Parse the response
  data = resp.json()

  # Print the response
  if not data.get('update_error'):
    print('Dataset successfully updated.')


if __name__ == '__main__':
  update_dataset()