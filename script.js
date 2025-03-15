window.onload = function(){
    alert("به رزومه من خوش آمدید!")
};

window.addEventListener("scroll", function(){
    let header = document.querySelector("header");
    let background = document.querySelector("body");  // یا اگر background یه کلاس خاص داره از querySelector(".background") استفاده کنید
    
    if(window.scrollY > 50){
        header.style.background = "#ADD8E6";  
        background.style.background = "#FF5733"; 
    } else {
        header.style.background = "#ADD8E6";  
        background.style.background = "#F0E68C"; 
    }
});

document.addEventListener("DOMContentLoaded", function () {
    let btn = document.createElement("button");
    btn.innerText = "Contact";
    btn.style.display = "block";
    btn.style.margin = "20px auto";
    btn.style.padding = "10px";
    btn.style.background = "#007BFF";
    btn.style.color = "white";
    btn.style.border = "none";
    btn.style.borderRadius = "5px";
    btn.style.cursor = "pointer";

    document.body.appendChild(btn);

    btn.addEventListener("click", function () {
        alert("Email: Ardavan.Hoseyni@proton.me  \\ Telegram: @Arda20063");
    });
});