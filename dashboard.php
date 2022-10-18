<?php
//include auth_session.php file on all user panel pages
include("auth_session.php");
?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard - Client area</title>
  <style>
    <?php include 'style1.css';?>
  </style>
</head>
<body>
    

    <div class="box">
        <form class="form" method="POST">
            <h2>Welcome <?php echo strtoupper($_SESSION['username']); ?>!</h2>

            
            <div class="login-button-container">
                <div class="login-button">
                    <div class="reg_face_button"><button type="submit" formaction="reg_face.php">Register</button></div>
                </div>
            </div>
            

            
            <div class="login-button-container">
                <div class="login-button">
                    <div class="find_button"><button type="submit" formaction="find.php">Find Criminal</button></div>
                </div>
            </div>
            
            
            <div class="link-container">
                <div class="link">
                    <p><a href="logout.php">Logout</a></p>
                </div>
            </div>
            
        </form>
    </div>
</body>
</html>