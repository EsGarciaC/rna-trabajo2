import pickle
def load_predictor():
    modelo = open("modelo/modelo_GPT_Detective.pkl","rb")
    tokenizer = open("modelo/Tokenizer.pkl", "rb")
    model = pickle.load(modelo)
    tokenizer = pickle.load(tokenizer)

    return (model, tokenizer)