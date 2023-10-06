from flask import Flask, request, render_template_string
import shlex
import subprocess
import requests

app = Flask(__name__)

@app.route('/')
def index():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Super Pretty Web Application</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                overflow: hidden;
                animation: rainbow 10s linear infinite;
            }

            @keyframes rainbow {
                0% {
                    background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
                }
                100% {
                    background: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
                }
            }
        </style>
    </head>
    <body>
        <h1 style="font-family: cursive; font-size: 4em; text-align: center; margin-top: 100px;">
            {super pretty web application, which is not so super duper secure}
        </h1>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/exploit', methods=['GET', 'POST'])
def exploit():
    if request.method == 'GET':
        cmd = request.args.get('cmd')
        print(cmd)
        cmd = shlex.split(cmd)
        process = subprocess.Popen(cmd, stdout = subprocess.PIPE)
        output, err = process.communicate()

        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Super Pretty Web Application</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    overflow: hidden;
                    animation: rainbow 10s linear infinite;
                }

                @keyframes rainbow {
                    0% {
                        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
                    }
                    100% {
                        background: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
                    }
                }
            </style>
        </head>
        <body>
            <h1 style="font-family: cursive; font-size: 4em; text-align: center; margin-top: 100px;">
                $ {{output}}
            </h1>
        </body>
        </html>
        """


        return render_template_string(html_content, output=output.decode('utf-8'))

