from flask import Flask, render_template, request, jsonify
from keras.utils.data_utils import pad_sequences
from loader import load_predictor
from json import dumps

app = Flask(__name__)

model, tokenizer = load_predictor()
max_len = 1000
trunc_type = "post" 
padding_type = "post"

testTexts = ["El miedo como recurso en el cine y su evolución El miedo es una de las emociones más explotadas en el cine. A pesar de tratarse de una sensación desagradable, muchas personas la encuentran sumamente adictiva. Esto se debe a su increíble capacidad para desligarnos de la rutina, pero al mismo tiempo, su potencial para producir una expectativa irracional hacia peligros o amenazas que no son reales. Tomando todo esto en consideración, resulta muy interesante analizar su evolución a través de la historia. La primera emoción que sintieron las personas al ver una película fue el miedo. Esto quedó registrado en el año 1896, cuando los hermanos Lumière anunciaron el estreno de la cinta que tenía como nombre “Llegada del tren a la estación de La Ciotat”, que es considerada la primera pieza cinematográfica. Al tratarse de una novedad, no tardó en atraer la atención del público francés, que no estaba acostumbrado a ver una pantalla con imágenes en movimiento. Sin embargo, su reacción ante la aparición del tren que se acercaba a ellos fueron una serie gritos y sobresaltos. Nadie, en ese entonces, estaba preparado para ver cómo un vehículo de grandes proporciones se aproximaba a ellos, dando la sensación de que iban a ser atropellados. Muchos sintieron un miedo sin precedentes y salieron despavoridos. De este modo, y de una manera casual, se estableció una de las reglas más importantes del cine de terror. Me refiero al hecho de que los espectadores deben sentirse amenazados, permitiendo que sientan miedo y experimenten otras sensaciones afines. No obstante, recién en el año 1910 apareció la primera película que tenía como objetivo principal asustar al público. Se trataba de una producción en blanco y negro que contaba la historia del monstruo creado por el doctor Frankenstein, una de los personajes más emblemáticos de la literatura gótica. El encargado de dirigir este film fue el estadounidense J. Searle Dawley, que logró crear un ambiente tétrico a pesar de las limitaciones tecnológicas del momento. Los primeros planos de la criatura, el uso de claroscuros y una banda sonora adecuada, fueron suficientes para que los espectadores se adentraran en un mundo de espanto. Esto fue esencial para sentar las bases del género de terror, que luego sería consolidado por un grupo de cineastas alemanes que se encargaron de incorporar características propias del expresionismo de su país. La película más representativa de esta escuela es “Nosferatu” de 1922, que está inspirada en el personaje de Drácula creado por Bram Stoker. Casi medio siglo después, Alfred Hitchcock revolucionó por completo el género. Atrás quedaron las criaturas malévolas y las amenazas visibles, en cambio, para que los espectadores se sintieran atemorizados se empezó a utilizar el suspenso. De esta forma, las personas podían explorar sus propios miedos, un recurso que antes solo era utilizado en la literatura. Actualmente, las películas de cine buscan provocar miedo mezclando el suspenso y la presencia de seres sobrenaturales. También existe una fuerte demanda por elementos más impactantes, pero no cabe duda que lo más efectivo sigue siendo lo clásico, pues nada se compara con sentir un terror personalizado que solo nosotros podemos entender.", 
             "El transporte público es un servicio esencial en la mayoría de las ciudades del mundo. Se trata de una red de transporte de pasajeros que abarca diferentes medios, como autobuses, trenes, tranvías, metro y taxis, entre otros. El transporte público es una necesidad para muchas personas, ya sea para ir a trabajar, a la escuela o para realizar actividades diarias. El transporte público ofrece muchas ventajas para la sociedad. En primer lugar, es una forma sostenible de transporte que reduce la cantidad de vehículos en la carretera, lo que disminuye la contaminación y mejora la calidad del aire. También ayuda a reducir la congestión del tráfico y el tiempo de viaje, lo que a su vez reduce el estrés en los usuarios. Además, el transporte público es una forma económica de viajar. A menudo, los precios son más bajos en comparación con los costos de poseer y mantener un vehículo personal. Esto puede ser especialmente beneficioso para personas con bajos ingresos que necesitan transporte diario. Otro beneficio del transporte público es que promueve la inclusión social y la igualdad de acceso. El transporte público puede conectar a personas de diferentes áreas, facilitando la movilidad de aquellos que no tienen un vehículo propio. Esto es particularmente importante en áreas rurales o en zonas urbanas donde el acceso al transporte puede ser limitado. Sin embargo, el transporte público también presenta algunos desafíos y limitaciones. Uno de los mayores desafíos es la falta de financiación y la falta de mantenimiento y actualización adecuados. Esto puede llevar a problemas como la falta de seguridad, la falta de comodidad y el envejecimiento de los vehículos y las infraestructuras. Además, el transporte público puede ser limitado en términos de rutas y horarios. Esto puede ser especialmente difícil para personas que necesitan viajar a lugares específicos fuera de las rutas de transporte público. Además, los horarios limitados pueden dificultar la flexibilidad para las personas que necesitan realizar actividades diarias fuera del horario laboral. También hay preocupaciones de seguridad al utilizar el transporte público. El crimen puede ser un problema en algunas áreas, lo que puede disuadir a algunas personas de utilizar el transporte público. Además, la posibilidad de accidentes o averías mecánicas también puede ser una preocupación. A pesar de estos desafíos, el transporte público sigue siendo un servicio vital para muchas personas. Para mejorar el transporte público, se necesitan inversiones en financiamiento y actualizaciones de infraestructura, así como esfuerzos para aumentar la seguridad y la comodidad. Además, se deben desarrollar nuevas tecnologías para mejorar la eficiencia y la accesibilidad. En resumen, el transporte público es un servicio esencial para la sociedad, que ofrece muchos beneficios como la sostenibilidad, la economía y la inclusión social. A pesar de los desafíos y limitaciones, el transporte público sigue siendo una necesidad para muchas personas. Por lo tanto, es importante seguir trabajando en mejoras para garantizar que este servicio vital siga siendo una opción viable y efectiva para el transporte de pasajeros."
             ]

@app.route('/')
def index():
    # testText_sequence = tokenizer.texts_to_sequences(testTexts)
    # testText_padded = pad_sequences(testText_sequence, maxlen=max_len, padding=padding_type, truncating=trunc_type)
    # labels = model.predict(testText_padded)
    # return str(labels)
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def prediccion():
    if request.method == 'POST':
        json_input = request.get_json(silent=True)
        #print({"payload": predecir(json_input)[0][0]})
        return jsonify({"payload": str(predecir(json_input)[0][0])})

def predecir(texto):
    text_list = [texto]
    text_sequence = tokenizer.texts_to_sequences(text_list)
    text_padded = pad_sequences(text_sequence, maxlen=max_len, padding=padding_type, truncating=trunc_type)
    labels = model.predict(text_padded)
    return labels

if __name__ == '__main__':
    app.run()