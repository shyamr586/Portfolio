var progressbar = document.getElementById("progress-bar");
var percentage = document.getElementById("percentage");
var pageHeight = document.body.scrollHeight - window.innerHeight;
window.onscroll = function(){
    var progress = (window.pageYOffset/pageHeight) * 100;
    progressbar.style.height = progress + "%";
}

var elements;
var windowHeight;

function init() {
elements = document.querySelectorAll('.hidden');
windowHeight = window.innerHeight;
}

function checkPosition(){
    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];
        var positionFromTop = elements[i].getBoundingClientRect().top;
  
        if (positionFromTop - windowHeight <= 0) {
          element.classList.add('fade-in-element');
          element.classList.remove('hidden');
        }
        
      }
}

init()
checkPosition()

window.addEventListener("resize",init);
window.addEventListener("scroll", checkPosition);