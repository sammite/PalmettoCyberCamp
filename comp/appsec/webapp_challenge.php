<?php
// TODO: 
// Add cookie with interesting stuff
// add different way of bypassing auth
// add hidden file

function printFlag() {
    echo "<h1>As Admin, you have permission! Flag: PCSC-PHPFLAG-PCSC\n</h1>";
	
}

function checkAdminValue($params) {
    if (isset($params['mega<>Admin']) && base64_decode($params['mega<>Admin']) === 'allThePerms') {
        printFlag();
    }
}


if(isset($_GET['admintype'])) {

	$user_val = html_entity_decode($_GET["admintype"]);
	$user_perms = $_GET["perms"];
	echo "$user_val is user privilege level\n";

    if ($user_val == "mega<>Admin") {
    	$params = [$user_val => $user_perms];
	    checkAdminValue($params);
    
    } else {
        echo "<h1>ACCESS DENIED</h1>";
    }


    } else {
        echo "<h1>ACCESS DENIED</h1>";
    }
?>

