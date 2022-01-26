var elements;
var windowHeight;

function init() {
elements = document.querySelectorAll('.hidden');
windowHeight = window.innerHeight;
}

function checkPosition(){
    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];
        var positionFromTop = elements[i].getBoundingClientRect().top + 200;
  
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

document.addEventListener("DOMContentLoaded", ()=>{
    anime.timeline({

    }).add({
        targets: '.cover',
        left: ['-100%','100%'],
        easing: 'easeOutExpo',
        duration: 2000,
        delay: (el,i)=>i*200+i%2*500,
    })
    .add({
      targets: '.text',
      top: ["75%", "50%"],
      opacity: [0,1],
      easing: 'easeOutExpo',
      duration: 1200,
      offset: '-=1600'
    })
})

var progressbar = document.getElementById("progress-bar");
var percentage = document.getElementById("percentage");
var pageHeight = document.body.scrollHeight - window.innerHeight;
window.onscroll = function(){
  var progress = (window.pageYOffset/pageHeight) * 100;
  progressbar.style.height = progress + "%";
}