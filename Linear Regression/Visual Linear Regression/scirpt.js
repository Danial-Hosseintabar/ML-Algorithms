const drawinDiv = document.getElementsByClassName("drawingDiv")[0];
let windowWidth = window.innerWidth;
let windowHeight = window.innerHeight;
let canvas = document.getElementsByClassName("canvas")[0];
let ctx = canvas.getContext("2d");

let data_x = [];
let data_y = [];
let th = [0.0, 0.0];

const drawPoint = (e) => {
    let x = e.offsetX;
    let y = e.offsetY;

    ctx.fillRect(x, y, 5, 5);
    data_x.push(x);
    data_y.push(300 - y);
    addDataToPanelDiv(x, 300 - y);
    ctx.stroke();
};

function addDataToPanelDiv(x, y) {
    document.getElementById("XValuesTable").innerHTML += "<br/>" + x;
    document.getElementById("YValuesTable").innerHTML += "<br/>" + y;
}

function reset() {
    data_x = [];
    data_y = [];
    th = [0, 0];
    canvas.setAttribute("width", "" + canvas.getBoundingClientRect().width + "px");
    canvas.setAttribute("height", "" + canvas.getBoundingClientRect().height + "px");
    document.getElementById("XValuesTable").innerHTML = "X Values :";
    document.getElementById("YValuesTable").innerHTML = "Y Values :";
    document.getElementById("result").innerHTML = "";
}

function init() {
    canvas.addEventListener("mousedown", drawPoint);
    canvas.setAttribute("width", "" + canvas.getBoundingClientRect().width + "px");
    canvas.setAttribute("height", "" + canvas.getBoundingClientRect().height + "px");
}

function gradient_descent() {
    let alpha = 0.00001;
    for (let i = 0; i < data_x.length; i++) {
        console.log(data_x[i]);
        console.log(data_y[i]);
    }
    th = [0, 0];
    let sum = [0.0, 0.0];
    for (let i = 0; i < 1000000; i++) {
        sum = [0.0, 0.0];
        for (let k = 0; k < data_x.length; k++) {
            sum[0] += (-data_y[k] + (th[0] + th[1] * data_x[k]));
            sum[1] += (-data_y[k] + (th[0] + th[1] * data_x[k])) * data_x[k];
        }
        th[0] -= alpha * sum[0];
        th[1] -= alpha * sum[1];
    }

    drawLine();
    showResult();
}

function drawLine() {
    ctx.beginPath();
    ctx.moveTo(0, 300 - th[0]);
    ctx.lineTo(300, 300 - (th[0] + th[1] * 300));
    ctx.stroke();
}

function showResult() {
    document.getElementById("result").innerHTML = "intercept = " + Math.floor(th[0] * 100) / 100 +
        "<br/>slope = " + Math.floor(th[1] * 100) / 100;
}