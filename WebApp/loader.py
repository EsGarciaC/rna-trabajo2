import pickle
from keras.models import load_model
def load_predictor():
    model = load_model('modelo')
    tokenizer = open("modelo/Tokenizer.pkl", "rb")
    tokenizer = pickle.load(tokenizer)

    return (model, tokenizer)