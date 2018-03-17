from tensorci_client import TensorCI

client = TensorCI()

incomplete_record = {
  'AGE': 50,
  'CLASS': 'BUSINESS'
}

complete_record = client.predict(data=incomplete_record)

print(complete_record)