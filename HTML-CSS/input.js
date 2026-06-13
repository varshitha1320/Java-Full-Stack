function greet_afternoon(){
    let text = document.getElementById("greet");
    text.innerHTML = "Good Afternoon";  
}
function change_color(){
    let colour= document.getElementById("cat");
    colour.style.backgroundColor = "Black";
}
function Turn_on(){
    let light = document.getElementById("light");
    light.src = "C:\\Java-Full-Stack\\HTML-CSS\\New folder\\bulb.jpg";
}
function Turn_off(){
    let light = document.getElementById("light");
    light.src = "C:\\Java-Full-Stack\\HTML-CSS\\New folder\\bulb_ off.jpg";
}