# coding: utf-8

import sys
import os

template_html = '''
<html>
<head>
    <meta charset="UTF-8">
    <script language="javascript" type="text/javascript" src="p5/p5.js"></script>

    <!--
    <script language="javascript" type="text/javascript" src="libs/dat.gui.min.js"></script>
      -->

    <!-- uncomment lines below to include extra p5 libraries -->
    <!-- <script language="javascript" src="../addons/p5.dom.js"></script> -->
    <!-- <script language="javascript" src="../addons/p5.sound.js"></script> -->

    <!--
    <script language="javascript" type="text/javascript" src="libs/easing.js"></script>
    <script language="javascript" type="text/javascript" src="libs/utils.js"></script>
      -->
    <script language="javascript" type="text/javascript" src="%s"></script>

    <!-- this line removes any default padding and style. you might only need one of these values set. -->
    <style>
body { padding: 0; margin: 0; }
#gui { position: absolute; top: 0px; left: 400px; }
    </style>
</head>
<body>
    <div id="p5jscanvas"></div>
</body>
</html>
'''.lstrip()

template_js = '''
"use strict";

function setup() {
    createCanvas(400, 400).parent("p5jscanvas");
}

function draw() {
    background(255);
}
'''.lstrip()


def create_file(name):
    html = name + ".html"
    js = name + ".js"

    for file in [html, js]:
        if os.path.exists(file):
            print("file already exists:", file)
            return

    with open(html, "w") as fout:
        fout.write(template_html % (name + ".js"))

    with open(js, "w") as fout:
        fout.write(template_js)

    print("create sketch:", name)


def main():
    if len(sys.argv) != 2:
        print("usage:")
        print("$ python create-p5js.py sketch-name")
        exit(0)

    name = sys.argv[1]
    create_file(name)


if __name__ == "__main__":
    main()
