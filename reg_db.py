#!C:/Users/user/AppData/Local/Programs/Python/Python310/python.exe
print()
import cgi
import pymysql
form = cgi.FieldStorage()
cid = form.getvalue("cid")
name = form.getvalue("name")
phone = form.getvalue("phone")
address = form.getvalue("address")
gender = form.getvalue("gender")
dob = form.getvalue("dob")
height = form.getvalue("height")
nationality = form.getvalue("nationality")
offence = form.getvalue("offence")
doa = form.getvalue("doa")
place = form.getvalue("place")
officer = form.getvalue("officer")
filename = form.getvalue("filename")




def insert_vals():
    connection = pymysql.connect(host='localhost',user='root',passwd='',database='mydatabase')
    cursor = connection.cursor()
    insert = "INSERT INTO `criminal`(`cid`, `name`, `phone`, `address`, `gender`, `dob`, `height`, `nationality`, `offence`, `doa`, `place`, `officer`, `filename`) VALUES ('"+cid+"','"+name+"','"+phone+"','"+address+"','"+gender+"','"+dob+"','"+height+"','"+nationality+"','"+offence+"','"+doa+"','"+place+"','"+officer+"','"+filename+"');"
    cursor.execute(insert)
    connection.commit()
    connection.close()

insert_vals()
print('<!DOCTYPE html><html><head><style>@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@100&family=Reem+Kufi+Fun:wght@500&display=swap");body {    position: relative;    align-items: center;    /*background-image: url("./img/bgcriminal1.jpg");*/    background: url("./img/bgcriminal5.jpg") no-repeat center center fixed;     -webkit-background-size: cover;    -moz-background-size: cover;    -o-background-size: cover;    background-size: 100% 100%;    background-position: left top, right top;    background-color: white;    display: flex;    justify-content: center;    height: 100vh;    margin-bottom: 100px;  }    .form {    position: absolute;    top: 260px;    /*right: 90px;*/    background-color: #47474a;    border-radius: 20px;    box-sizing: border-box;    height: 340px;    padding: 40px;    width: 700px;  }    .title {    color: #eee;    font-family: "Reem Kufi Fun";    font-size: 30px;    font-weight: 60;    margin-top: 30px;    text-align: center;  }    .subtitle {    color: #eee;    font-family: sans-serif;    font-size: 16px;    font-weight: 600;    margin-top: 10px;  }    .input-container {    height: 50px;    position: relative;    width: 100%;  }    .ic1 {    margin-top: 40px;  }    .ic2 {    margin-top: 30px;  }    .input {    background-color: rgb(32, 32, 32);    border-radius: 12px;    border: 0;    box-sizing: border-box;    color: #eee;    font-size: 18px;    height: 100%;    outline: 0;    padding: 4px 20px 0;    width: 100%;  }    .cut {    background-color: #47474a;    border-radius: 10px;    height: 20px;    left: 20px;    position: absolute;    top: -20px;    transform: translateY(0);    transition: transform 200ms;    width: 80px;  }    .cut-short {    width: 50px;  }    .input:focus ~ .cut,  .input:not(:placeholder-shown) ~ .cut {    transform: translateY(8px);  }    .placeholder {    color: white;    font-family: "Reem Kufi Fun";    left: 20px;    line-height: 14px;    pointer-events: none;    position: absolute;    transform-origin: 0 50%;    transition: transform 200ms, color 200ms;    top: 20px;  }    .input:focus ~ .placeholder,  .input:not(:placeholder-shown) ~ .placeholder {    transform: translateY(-30px) translateX(10px) scale(0.75);  }    .input:not(:placeholder-shown) ~ .placeholder {    color: #808097;  }    .input:focus ~ .placeholder {    color: white;  }  .submit-container{    height: 50px;    position: relative;   }  .submit {    margin: 0;    position: absolute;    top: 40%;    left: 50%;    -ms-transform: translate(-50%, -50%);    transform: translate(-50%, -50%);    background-color: rgb(33, 31, 31);    border-radius: 12px;    border: 0;    box-sizing: border-box;    color: #eee;    cursor: pointer;    font-family: "Reem Kufi Fun";    font-size: 18px;    height: 50px;    margin-top: 38px;    outline: 0;    text-align: center;    width: 40%;  }    .submit:active {    background-color: rgb(43, 42, 42);  }  .link-container {    height: 200px;    position: relative;    /*border: 3px solid green;*/}  .link {    margin: 0;    position: absolute;    top: 70%;    left: 40%;    -ms-transform: translateY(-50%);    transform: translateY(-50%);}a {    color: white;    font-size: large;    font-family: "Reem Kufi Fun"}  </style></head><body><div class="form"><div class="title">Registered successfully</div><div class="link-container"><div class="link"><p><a href="dashboard.php">Go to dashboard</a></p></div></div></div></body></html>')
"""
print('<h1>Register the face successfully</h1>')
print('<a href = "dashboard.php">Go to dashboard</a>')
"""

