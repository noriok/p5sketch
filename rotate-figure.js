"use strict";

function setup() {
    createCanvas(400, 400).parent("p5jscanvas");

    rectMode(CENTER);
    noFill();
}

function drawRect(x, y, w, h, angle) {
    push();
    translate(x, y);
    rotate(angle); // clockwise
    rect(0, 0, w, h);
    pop();
}

function draw() {
    background(255);

    let angle = frameCount / 100;
    drawRect(width / 2, height / 2, 80, 80, angle);
    drawRect(mouseX, mouseY, 50, 100, angle);
}
