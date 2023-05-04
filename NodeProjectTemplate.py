import os
import subprocess


# create project directory
os.mkdir('ExpressApp')

# navigate to project directory
os.chdir('ExpressApp')

# initialize npm
subprocess.run(["npm", "init", "-y"])

# install express
subprocess.run(["npm", "install", "express"])

# create app.js file with basic Express code
with open("app.js", "w") as file:
    file.write("const express = require('express');\n\n")
    file.write("const app = express();\n\n")
    file.write("app.get('/', (req, res) => {\n")
    file.write("  res.send('Hello World!');\n")
    file.write("});\n\n")
    file.write("app.listen(3000, () => {\n")
    file.write("  console.log('App listening on port 3000!');\n")
    file.write("});\n")