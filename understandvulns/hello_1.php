<?php
// this is meant to be a very simple demonstration of how url parameters can be "hacked"


if(isset($_GET['user_status'])) {

    $user_val = $_GET["user_status"];
	echo "$user_val is user privilege level\n";

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

