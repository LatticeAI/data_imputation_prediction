from tensorci import TensorCI


def get_prediction():
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
  if data.get('ok'):
    print('Got Prediction: ', data.get('prediction'))
  else:
    print('Prediction responded with error: ', data.get('error'))


if __name__ == '__main__':
  get_prediction()