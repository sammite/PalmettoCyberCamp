<?php
// this is meant to be a very simple demonstration of how url parameters can be "hacked"

echo "$user_val is user privilege level\n";
if(isset($_GET['user_status'])) {

    $user_val = $_GET["user_status"];
	

        // Display a friendly message
    if ($user_val == "admin") {
        echo "<h1>Welcome back, dear admin!</h1>";
    } else {
        // Display a different message
        echo "<h1>ACCESS DENIED</h1>";
    }


    } else {
        // Display a different message
        echo "<h1>ACCESS DENIED</h1>";
    }
?>

