from os import listdir
from os.path import getmtime

name = input("Enter name: ")

images = {}

for file in listdir(f"sources/{name}"):
    images[getmtime(f"sources/{name}/{file}")] = file


sorted_images = [images[timestamp] for timestamp in sorted(images.keys())]

img_tags = ""
for file in sorted_images:
    img_tags += f'        <img src="sources/{name}/{file}" loading="lazy">\n'

html = """<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <title>{{title}}</title>

    <style>
      body {
        margin: 0;
        padding-top: 10rem;
        padding-bottom: 10rem;

        background-color: black;
      }

      #images {
        width: 100%;

        display: flex;
        flex-direction: column;
        align-items: center;
      }

      img {
        width: 100%;
        max-width: 2500px;
      }
    </style>
  </head>
  <body>
    <div id="images">
{{img_tags}}
    </div>
  </body>
</html>""".replace(
    "{{title}}", name
).replace(
    "{{img_tags}}", img_tags
)

with open(f"{name}.html", "w") as f:
    f.write(html)
