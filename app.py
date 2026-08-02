import streamlit as st
import streamlit.components.v1 as components

st.title("❤️")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    background: black;
    overflow: hidden;
}
canvas {
    display: block;
    margin: auto;
}
</style>
</head>

<body>

<canvas id="canvas"></canvas>

<script>
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

canvas.width = 600;
canvas.height = 600;

let colors = [
    "red",
    "orange",
    "yellow",
    "lime",
    "cyan",
    "blue",
    "purple"
];

let t = 0;

function draw() {

    ctx.fillStyle = "black";
    ctx.fillRect(0,0,600,600);

    let cx = 300;
    let cy = 300;

    for(let i=0;i<120;i++){

        let angle = i * Math.PI * 2 / 120;

        let x = 16 * Math.pow(Math.sin(angle),3);
        let y = -(13*Math.cos(angle)
        -5*Math.cos(2*angle)
        -2*Math.cos(3*angle)
        -Math.cos(4*angle));

        x *= 15;
        y *= 15;

        ctx.beginPath();
        ctx.moveTo(cx,cy-40);
        ctx.lineTo(cx+x,cy+y);

        ctx.strokeStyle = colors[(i+Math.floor(t/10)) % colors.length];
        ctx.stroke();
    }

    t++;

    requestAnimationFrame(draw);
}

draw();

</script>

</body>
</html>
"""

components.html(html_code, height=650)
