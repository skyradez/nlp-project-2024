import os
import tensorflow as tf

current_dir = os.getcwd()
relative_model_path = 'toxic_prediction' 

class SingletonModel:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls._load_model()
        return cls._instance

    @classmethod
    def _load_model(cls):
        model_path = os.path.join(current_dir, relative_model_path)
        return tf.keras.models.load_model(model_path)