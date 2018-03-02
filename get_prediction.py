from tensorci_client import TensorCI

client = TensorCI()

incomplete_record = {
  'AGE': 40,
  'CLASS': 'BUSINESS'
}

for i in range(20):
  complete_record = client.predict(data=incomplete_record)
  print('Got prediction {}'.format(i + 1))