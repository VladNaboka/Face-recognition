import face_recognition

photos = ["img/2019061304241233.jpg", "img/5067185.jpg", "img/772bc3e00e6dcddff606bee4a0fbf8b8.jpg",
          "img/Enshtein.jpg", "img/52_main-1000x_.jpg",
          "img/da86dd17bb6b51448b0c08611c2e99c1.jpg", "img/pravda-li-eto-skazal-ejnshtejn-test-dlya-eruditov.jpg"]

def faces_determine(imgMain, otherFeces, nums):
    imgM = face_recognition.load_image_file(imgMain)
    img_encod = face_recognition.face_encodings(imgM)[0]

    imgOth = face_recognition.load_image_file(otherFeces)
    imgOth_encod = face_recognition.face_encodings(imgOth)[nums]
    result = face_recognition.compare_faces([img_encod], imgOth_encod)
    print(result)

for i in range(0, len(photos)):
    f = face_recognition.load_image_file(photos[i])
    loc = face_recognition.face_locations(f)
    faces_determine("img/Kassym-Jomart_Tokayev_(2020-02-01).jpg", photos[i], len(loc) - 1)


