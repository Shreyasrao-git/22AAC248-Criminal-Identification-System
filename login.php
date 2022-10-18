<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Form</title>
  <style>
    <?php include 'style.css';?>
  </style>
</head>
<body>
    
<?php require('db.php');
    session_start();
    // When form submitted, check and create user session.
    if (isset($_POST['username'])) {
        $username = stripslashes($_REQUEST['username']);    // removes backslashes
        $username = mysqli_real_escape_string($con, $username);
        $password = stripslashes($_REQUEST['password']);
        $password = mysqli_real_escape_string($con, $password);
        // Check user is exist in the database
        $query    = "SELECT * FROM `users` WHERE username='$username'
                     AND password='" . md5($password) . "'";
        $result = mysqli_query($con, $query) or die(mysql_error());
        $rows = mysqli_num_rows($result);
        if ($rows == 1) {
            $_SESSION['username'] = $username;
            // Redirect to user dashboard page
            header("Location: dashboard.php");
        } else {
            echo "<div class='box'>
                  <div class='form'>
                  <h2>Incorrect Username/password.</h2><br/>
                  <div class='link-container'>
                        <div class='link'>
                            <p><a href='login.php'>Login again.</a></p>
                        </div>
                  </div>
                  </div>
                  </div>";
        }
    } else {
?>
    <div class="box">
        <form class="form" method="post" name="login">
            <h2>Sign in</h2>
            <div class="inputBox">
                <input type="text" class="login-input" name="username"  placeholder="Username" autofocus="true" spellcheck="false"/>
                <span>Username</span>
                <i></i>
            </div>
            <div class="inputBox">
                <input type="password" class="login-input" name="password" placeholder="Password" spellcheck="false"/>
                <span>Password</span>
                <i></i>
            </div>
            <div class="login-button-container">
                <div class="login-button">
                    <input type="submit" value="Login" name="submit" class="login-button">
                </div>
            </div>
            <div class="link-container">
                <div class="link">
                    <p><a href="registration.php">New Registration</a></p>
                </div>
            </div>
            
        </form>
    </div>
<?php
    }
?>
</body>
</html>