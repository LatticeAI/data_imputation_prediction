from tensorci import TensorCI

client = TensorCI()

unseen_features = {
  'name': 'Gary',
  'email': 'gary@gmail.com'
}

# Make the prediction
resp = client.predict(features=unseen_features)

# Parse the prediction
data = resp.json()

# Print the prediction
print('Got Prediction:  {}'.format(data.get('prediction')))