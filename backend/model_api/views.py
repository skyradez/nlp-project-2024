from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
from .utils.singleton_model import SingletonModel


@api_view(['POST'])
def predict_model(request, *args, **kwargs):
    sentence = request.data.get('sentence')
    model_instance = SingletonModel.get_instance()
    prediction = model_instance.predict(np.array([sentence]))
    print('Prediction:', str(prediction[0][0] * 100) + "%")
    
    
    return Response({
        "code": 200,
        "status": "OK",
        "data": {
            "sentence": "{:.2f}%".format(prediction[0][0] * 100)
        }
    })
