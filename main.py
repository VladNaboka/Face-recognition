import time
import face_recognition
import glob

start_time = time.time()
# photosPolitic = ["img/Politic/03-25.jpg", "img/Politic/190766-image.jpg", "img/Politic/0003_1.jpg", "img/Politic/5.jpg",
#           "img/Politic/5f23b0b6-7f9b-4761-bedf-c6f5b98eb622.jpeg", "img/Politic/007.jpg", "img/Politic/003.jpg",
#           "img/Politic/613f28471f50a019041769.jpg", "img/Politic/8u5a1773.jpg", "img/Politic/20509_1634211740_lg.jpg",
#           "img/Politic/31242eec61bc29f7200a5010f34e4b06.jpg", "img/Politic/190766-image.jpg",
#           "img/Politic/6050706d589e6915332607.jpg", "img/Politic/1553830786_article_b.jpeg",
#           "img/Politic/201902251157119.jpg", "img/Politic/_aps7jBSn200.jpg",
#           "img/Politic/ALI_5096.jpg", "img/Politic/Askar_mamin_2.jpg", "img/Politic/Askar_Mamin_official_portrait.jpg",
#           "img/Politic/c7a41bc5044dfddcf17aedae4e563939.jpg", "img/Politic/fba7baf8b87f33a5.jpeg",
#           "img/Politic/murz2676-1080.jpg", "img/Politic/murz2767.jpg",
#           "img/Politic/murz9188-1080.jpg","img/Politic/photo_497.jpg",
#           "img/Politic/photo_289209.jpg", "img/Politic/photo_396208.jpeg", "img/Politic/sayn_1.jpg",
#           "img/Politic/sha-0851-1080.jpg", "img/Politic/а1.jpg",
#             "img/Politic/1580279340.jpg", "img/Politic/1586929160.jpg",
#             "img/Politic/boz.jpg", "img/Politic/img-20191218-wa0024.jpg", "img/Politic/photo-2019-12-19-19-50-03.jpg",
#                 "img/Politic/Others/0FBB7F82-55B3-4413-AA3E-6F8D3D9E2927_cx33_cy22_cw34_w1200_r1.jpg",
#                 "img/Politic/Others/93D6D633-AE83-41F8-B1CD-861EE61E07F2_cx39_cy9_cw42_w1200_r1.jpg",
#                 "img/Politic/Others/367d7104-58db-47e0-abb9-3586eb679e24_tv_w1200_r1.jpg",
#                 "img/Politic/Others/479BF7A8-A5C3-423B-9EDF-AFEC6EDDFD20_cx30_cy9_cw59_w1200_r1.jpg",
#                 "img/Politic/Others/1098ADC0-09A5-4258-B418-CFFD0CE3A133_cx18_cy7_cw57_w1200_r1.jpg",
#                 "img/Politic/Others/a9e138a4-3e4d-4ef4-9e76-7c50262ed5e2_tv_w1200_r1.jpg",
#                 "img/Politic/Others/a50002e3-4f09-484d-95f9-a95c2b15a5b8_tv_w1200_r1.jpg",
#                 "img/Politic/Others/c5055b25-61a5-42e9-a6f6-5dafa4a4bf06_tv_w1200_r1.jpg",
#                 "img/Politic/Others/d91288fd-d142-40fe-a2ae-aa28f9f31136_tv_w1200_r1.jpg",
#                 "img/Politic/Others/E7828876-2F91-473D-9943-6D9DAA25F2AD_cx0_cy18_cw0_w1200_r1.jpg"]

# photosMedia = ["img/Media/5f439da932891166202853.jpg", "img/Media/3_4c2f6b27.jpg", "img/Media/10.jpg",
#                "img/Media/60e5c04bc5ac7468782889.jpg", "img/Media/60e25943f5fb88ab0c91ac1a7a0d666c.jpg"]
# photosMedia = list(paths.list_images('Media'))
photosMedia = glob.glob('img/Media/*.jpg')
photosPolitic = glob.glob('img/Politic/*.jpg' or 'img/Politic/*.jpeg')
photosBlog = glob.glob('img/Bloger/*.jpg' or 'img/Bloger/*.jpeg' or 'img/Bloger/*.png')

def faces_determine(imgMain, otherFeces, nums):
    imgM = face_recognition.load_image_file(imgMain)
    img_encod = face_recognition.face_encodings(imgM)[0]

    imgOth = face_recognition.load_image_file(otherFeces)
    imgOth_encod = face_recognition.face_encodings(imgOth)[nums]
    result = face_recognition.compare_faces([img_encod], imgOth_encod)
    print(result)

start_timeP = time.time()
scoreP = 0
print("Politic: ")
for i in range(0, len(photosPolitic)):
    f = face_recognition.load_image_file(photosPolitic[i])
    loc = face_recognition.face_locations(f)
    scoreP += 1
    print(scoreP, end=' ')
    faces_determine("img/Politic/201902251157119.jpg", photosPolitic[i], len(loc) - 1)
print(round(time.time() - start_timeP, 2))

start_timeM = time.time()
scoreM = 0
print("Media: ")
for i in range(len(photosMedia)):
    f = face_recognition.load_image_file(photosMedia[i])
    loc = face_recognition.face_locations(f)
    scoreM += 1
    print(scoreM, end=' ')
    faces_determine("img/Media/news_full15761195693e6a2b976bff9d222d414aa4160a2869.jpg", photosMedia[i], len(loc) - 1)
print(round(time.time() - start_timeM, 2))

start_timeB = time.time()
scoreB = 0
print("Bloger: ")
for i in range(len(photosBlog)):
    f = face_recognition.load_image_file(photosBlog[i])
    loc = face_recognition.face_locations(f)
    scoreB += 1
    print(scoreB, end=' ')
    faces_determine("img/Bloger/maxresdefault.jpg", photosBlog[i], len(loc) - 1)
print(round(time.time() - start_timeB, 2))

print("Общее время работы программы: " + f"{round(time.time() - start_time, 2)}")