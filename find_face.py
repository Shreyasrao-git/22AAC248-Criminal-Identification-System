#!C:/Users/user/AppData/Local/Programs/Python/Python310/python.exe
print()
#Importing required libraries
import face_recognition as fr
import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import pymysql
import cgi
import pymysql
form = cgi.FieldStorage()
#filename = form.getvalue("filename")
filename = "rishithfound.jpeg"




#Declaring global variables
global present
present=[]

#Using tkinter to take target image input
Tk().withdraw()
#load_image=askopenfilename()

#Loading the target image and getting encodings of all indivisual faces in it
target_image = fr.load_image_file("F:/Criminal/finding/"+filename)
target_encoding = fr.face_encodings(target_image)

#Encodings of individual faces from individual images
def encode_faces(folder):
    list_people_encodings = []
    for filename in os.listdir(folder):
        known_image = fr.load_image_file(f'{folder}{filename}')
        known_encoding = fr.face_encodings(known_image)[0]
        list_people_encodings.append((known_encoding, filename))
    return list_people_encodings

#Finding the faces in the group photo
def find_target_face():
    face_location=fr.face_locations(target_image)
    for person in encode_faces('img2/'):
        encoded_face=person[0]
        filename=person[1]
        is_target_face=fr.compare_faces(encoded_face, target_encoding,tolerance=0.55)
        #print(f'{is_target_face} {filename}')
        if face_location:
            face_number=0
            for location in face_location:
                if is_target_face[face_number]:
                    label=filename
                    present.append(label)
                face_number+=1

#Creating a frame/box around the target face
def create_frame(location, label):
    top, right, bottom, left = location
    cv.rectangle(target_image, (left,top), (right, bottom),(255,0,0),2)
    cv.rectangle(target_image, (left, bottom+20), (right, bottom), (255, 0, 0), cv.FILLED)
    cv.putText(target_image,label,(left+3,bottom+14),cv.FONT_HERSHEY_DUPLEX,0.4,(255,255,255),1)

#Converting the bgr image to rgb
def render_image():
    rgb_img = cv.cvtColor(target_image, cv.COLOR_BGR2RGB)
    cv.imshow('Final Image', rgb_img)
    cv.waitKey(0)



#Calling the functions
find_target_face()

def get_info(file):
    connection = pymysql.connect(host='localhost',user='root',passwd='',database='mydatabase')
    cursor = connection.cursor()

    select = "SELECT `cid`, `name`, `phone`, `address`, `gender`, `dob`, `height`, `nationality`, `offence`, `doa`, `place`, `officer`, `filename` FROM `criminal` WHERE filename='"+file+"';"
    cursor.execute(select)
    final=cursor.fetchall()
    connection.commit()
    connection.close()
    return final

#print(present)
final = get_info(present[0])
k=list(final[0])
side_headings=['cid', 'name', 'phone', 'address', 'gender', 'dob', 'height', 'nationality', 'offence', 'doa', 'place', 'officer', 'filename']
#print(k)
n=len(k)
print('<!DOCTYPE html><html><head>  <style>@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@100&family=Reem+Kufi+Fun:wght@500&display=swap");body {    position: relative;    align-items: center;    /*background-image: url("./img/bgcriminal1.jpg");*/    background: url("./img/bgcriminal5.jpg") no-repeat center center fixed;     -webkit-background-size: cover;    -moz-background-size: cover;    -o-background-size: cover;    background-size: 100% 100%;    background-position: left top, right top;    background-color: white;    display: flex;    justify-content: center;    height: 100vh;    margin-bottom: 100px;  }  .form {    position: absolute;    top: 40px;    /*right: 90px;*/    background-color: #47474a;    border-radius: 20px;    box-sizing: border-box;    height: 1300px;    padding: 40px;    width: 700px;  }  .title {    color: #eee;    font-family: "Reem Kufi Fun";    font-size: 30px;    font-weight: 60;    margin-top: 20px;    text-align: center;  }  .input-container {    height: 50px;    position: relative;    width: 100%;  }    .ic1 {    margin-top: 320px;    margin-left: 195px;  }    .ic2 {    margin-top: 0px;    margin-left: 195px;  }  .ic3{    margin-top: 40px;    margin-left: 185px;  }  img{    border-radius: 25px;  }  .ptext{    color: white;    font-family: "Reem Kufi Fun";    font-size: 22px;    left: 20px;    line-height: 14px;    pointer-events: none;    position: absolute;    transform-origin: 0 50%;    transition: transform 200ms, color 200ms;    top: 20px;  }  p {  text-align:center;   vertical-align: middle;  display: table-cell;   }.link-container {    height: 200px;    position: relative;    /*border: 3px solid green;*/}  .link {    margin: 0;    position: absolute;    top: 40%;    left: 39%;    -ms-transform: translateY(-50%);    transform: translateY(-50%);}a {    color: white;    font-size: larger;    font-family: "Reem Kufi Fun";} </style></head><body>  <div class="form">    <div class="title">Criminal Details</div>')
db_image = "img2/"
print('<div class="input-container ic3">')
print('<img src="'+db_image+k[12]+'" width=250 height=380>')
print('</div>')
print('<div class="input-container ic1">')
print('<p class="ptext"><b>'+side_headings[0]+'</b>:&nbsp;'+k[0]+'</p>')
print('</div>')

#print('<img src="'+db_image+k[12]+'" height="400" width="300">')
#print('<img src="img/rishith.jpeg">')

for i in range(1,n-1):
    print('<div class="input-container ic2">')
    print('<p class="ptext"><b>'+side_headings[i]+'</b>:&nbsp;'+k[i]+'</p>')
    print('</div>')
print('<div class="link-container">    <div class="link">        <a href="dashboard.php">Go to dashboard</a>    </div>  </div><br><br><br><br><br><br><br><br>')
print('</body>')
print('</html>')



















