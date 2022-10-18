<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Registration</title>
  <style>
    <?php include 'style.css';?>
  </style>
</head>
<body>
<?php
    require('db.php');
    // When form submitted, insert values into the database.
    if (isset($_REQUEST['username'])) {
        // removes backslashes
        $username = stripslashes($_REQUEST['username']);
        //escapes special characters in a string
        $username = mysqli_real_escape_string($con, $username);
        $email    = stripslashes($_REQUEST['email']);
        $email    = mysqli_real_escape_string($con, $email);
        $password = stripslashes($_REQUEST['password']);
        $password = mysqli_real_escape_string($con, $password);
        $create_datetime = date("Y-m-d H:i:s");
        $query    = "INSERT into `users` (username, password, email, create_datetime)
                     VALUES ('$username', '" . md5($password) . "', '$email', '$create_datetime')";
        $result   = mysqli_query($con, $query);
        if ($result) {
            echo "<div class='box'>
            <div class='form'>
            <h2>You have registered successfully.</h2><br/>
            <div class='link-container'>
                  <div class='link'>
                    <p><a href='login.php'>Click here to Login</a></p>
                  </div>
            </div>
            </div>
            </div>";
        } else {
            echo "<div class='form'>
                  <h3>Required fields are missing.</h3><br/>
                  <p class='link'>Click here to <a href='registration.php'>registration</a> again.</p>
                  </div>";
        }
    } else {
?>
    
    <div class="box">
        
        <form class="form" method="post" name="login">
            <h2>Registration</h2>
            <div class="inputBox">
                <input type="text" class="login-input" name="username" placeholder="Username" autofocus="true"/>
                <span>Username</span>
                <i></i>
            </div>

            <div class="inputBox">
                <input type="text" class="login-input" name="email" placeholder="Email" autofocus="true"/>
                <span>Email id</span>
                <i></i>
            </div>

            <div class="inputBox">
                <input type="password" class="login-input" name="password" placeholder="Password"/>
                <span>Password</span>
                <i></i>
            </div>
            <div class="login-button-container">
                <div class="login-button">
                    <input type="submit" value="Register" name="submit" class="login-button">
                </div>
            </div>
            <div class="link-container">
                <div class="link">
                    <p><a href="login.php">Click to login</a></p>
                </div>
            </div>
            
        </form>
    </div>
<?php
    }
?>
</body>
</html>