from keras.models import model_from_json
import numpy as np
from keras import backend as K


def apiKayo(X_test):
  X_test = np.array(X_test)
  X_test = X_test.reshape((1,X_test.shape[0],X_test.shape[1]))
  
  filename = "model"
  # load json and create model
  json_file = open(filename+'.json', 'r')
  loaded_model_json = json_file.read()
  json_file.close()
  loaded_model = model_from_json(loaded_model_json)
  # load weights into new model
  loaded_model.load_weights(filename+".h5")

  predictions = loaded_model.predict(X_test)
  y_predict_category=[np.argmax(t) for t in predictions]

  K.clear_session()
  return y_predict_category