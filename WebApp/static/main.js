function obtenerResultados() {
  // Obtener el texto del ensayo
  var ensayo = document.getElementById("ensayo").value;
  
  // Enviar el texto del ensayo al JavaScript para procesarlo
  procesarEnsayo(ensayo);
  console.log(ensayo);
}

function procesarEnsayo(ensayo) {
  // Realizar las acciones necesarias con el texto del ensayo
  
  // Obtener el porcentaje humano
  const url = window.location.href+"predict";
    (async () => {
      const rawResponse = await fetch(url, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: ensayo
      });
      const content = await rawResponse.json();
    
      console.log(content);
    })();

  // PONER AQUÍ CONSULTA AL MODELO
  var porcentajeHumano = 0.45687;

  // Conclusión del detective
  var texto = `Su texto es ${Math.round(porcentajeHumano*100)}% hecho por un humano`;
  
  // Mostrar u ocultar las imágenes según el valor de porcentajeHumano
  var imagen1 = document.getElementById("Imagen1");
  var imagen2 = document.getElementById("Imagen2");
  var imagen3 = document.getElementById("Imagen3");
  var imagen4 = document.getElementById("Imagen4");
  
  if (porcentajeHumano < 0.4) {
    imagen1.style.display = "block";
    imagen2.style.display = "none";
    imagen3.style.display = "none";
    imagen4.style.display = "none";
  } else if (porcentajeHumano >= 0.4 && porcentajeHumano < 0.6) {
    imagen1.style.display = "none";
    imagen2.style.display = "block";
    imagen3.style.display = "none";
    imagen4.style.display = "none";
  } else if (porcentajeHumano >= 0.6 && porcentajeHumano < 0.75) {
    imagen1.style.display = "none";
    imagen2.style.display = "none";
    imagen3.style.display = "block";
    imagen4.style.display = "none";
  } else {
    imagen1.style.display = "none";
    imagen2.style.display = "none";
    imagen3.style.display = "none";
    imagen4.style.display = "block";
  }
  
  var divTexto = document.getElementById("divTexto");
  var outputText = document.getElementById("outputText");
  outputText.textContent = texto;
  divTexto.style.display = "block";
  
}





