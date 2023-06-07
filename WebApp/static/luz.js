function luz() {
  var element = document.body;
  var headd = document.getElementsByTagName("h1");
  var div = document.getElementsByTagName("div");
  
  for (var i = 0; i < headd.length; i++) {
    headd[i].classList.toggle("h1white-mode")
  }
  for (var i = 0; i < div.length; i++) {
    div[i].classList.toggle("div-white")
  }
  element.classList.toggle("white-mode")

} 