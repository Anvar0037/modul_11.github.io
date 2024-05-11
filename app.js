let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#2cab37"

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");

let item = ""

btn1.addEventListener("click", function (){
    tg.MainButton.setText("Burger bosildi");
    item = " Nomi- Burger ," +
        "Narxi- 5$";

    tg.MainButton.show();
}
);

btn2.addEventListener("click", function (){
    tg.MainButton.setText("Hot-Dog bosildi");
    item = " Nomi- Hot-Dog ," +
        "Narxi- 2.48$";
    tg.MainButton.show();
}
);
btn3.addEventListener("click", function (){
    tg.MainButton.setText("Pizza bosildi");
    item = " Nomi- Pizza ," +
        "Narxi- 3.99$";

    tg.MainButton.show();
}
);
btn4.addEventListener("click", function (){
    tg.MainButton.setText("Lavash bosildi");
    item = " Nomi- Lavash ," +
        "Narxi- 5$";
    tg.MainButton.show();
}
);


Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item)
});