
// Contact Form
const contactForm = document.getElementById("contactForm");

if (contactForm) {

    contactForm.addEventListener("submit", function (e) {

        e.preventDefault();

        alert("Thank you! Your message has been sent successfully.");

        contactForm.reset();

    });

}

// Scroll Button

let topButton = document.getElementById("topBtn");

window.onscroll = function () {

    if(document.body.scrollTop > 200 ||
       document.documentElement.scrollTop > 200){

        topButton.style.display = "block";

    }else{

        topButton.style.display = "none";

    }

}

function topFunction(){

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

}