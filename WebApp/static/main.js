function obtenerResultados() {
  // Obtener el texto del ensayo
  var ensayo = document.getElementById("ensayo").value;
  if (!ensayo){
    alert("Por favor ingresa un ensayo")
  }else{
  // Enviar el texto del ensayo al JavaScript para procesarlo
  procesarEnsayo(ensayo);
  //console.log(ensayo);
  }
}

function procesarEnsayo(ensayo) {
  // Realizar las acciones necesarias con el texto del ensayo
  var porcentajeHumano;
  var cuerpoFiltrado = ensayo.replace(/"|'/g, "`").replace(/\\/g, "").replace(/\n/g, ' ').replace(/  +/g, ' '); 
  console.log(cuerpoFiltrado)
  // Obtener el porcentaje humano
  const url = window.location.href + "predict";
    (async () => {
      const rawResponse = await fetch(url, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: '"' + cuerpoFiltrado + '"'
      });
      //const content = rawResponse;
      const content = await rawResponse.json();
      porcentajeHumano = parseFloat(content["payload"]);    
      console.log(porcentajeHumano);
      // Conclusión del detective
      console.log(porcentajeHumano);
      var texto = `El score de su texto es ${Math.round(porcentajeHumano*100)}%`;
      
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
        })();

 
  
}





