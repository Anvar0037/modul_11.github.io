let tg = window.Telegram.WebApp;
tg.expand();

tg.MaibButton.textColor = "#FFFFFF"
tg.MaibButton.color = "#2cab37"

let btn1 = document.getElementById("btn1")
let btn2 = document.getElementById("btn2")
let btn3 = document.getElementById("btn3")
let btn4 = document.getElementById("btn4")

btn1.addEventListener("click", function (){
    tg.MainButton.setText("btn1 bosildi")
})