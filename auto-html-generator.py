import os
movies_list=[]
index_tags=""
movies_list = os.listdir("movies")

for i in movies_list:
    each_tag = f"""
    <div class="sm:w-1/2 mb-10 px-4">
              <div class="rounded-lg h-64 overflow-hidden">
                <video class="object-cover object-center h-full w-full" controls src="movies/{i}"></video>
              </div>
              <h5 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3" >{i[:-4]}</h5>
            </div>"""
    index_tags+=each_tag

index_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pavan WebServer</title>
    <script src="script.js"></script>
    <link rel="icon" type="image/x-icon" href="movieICON.jpg">

</head>
<body>
    <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto">
          <div class="flex flex-col text-center w-full mb-20">
            <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">Pavan's Movie FileServer</h1>
            <p class="lg:w-2/3 mx-auto leading-relaxed text-base">All Movies and Web-Series at one place Anywhere , Anytime</p>
          </div>
          
      </section>

      <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto">
          <div class="flex flex-wrap -mx-4 -mb-10 text-center">
            {index_tags}
          </div>
        </div>
      </section>
</body>
</html>"""
open("index.html","w").write(index_html)
# os.system("rm movies_dir.txt")