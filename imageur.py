import pyimgur


"""
Authorization: Client-ID YOUR_CLIENT_ID
client =
client secret = 

Exemplo 1----
CLIENT_ID = ""
im = pyimgur.Imgur(CLIENT_ID)
image = im.get_image('S1jmapR')
print(image.title) # Cat Ying & Yang
print(image.link)


exemplo 2 ----
CLIENT_ID = "Your_applications_client_id"
PATH = "A Filepath to an image on your computer"
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.size)
print(uploaded_image.type)



"""
CLIENT_ID = ""
PATH = "a.jpg"
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="Yasmin | Pyimageupload")
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.size)
print(uploaded_image.type)