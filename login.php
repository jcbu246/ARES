<?php

if(isset($_GET['username']) && isset($_GET['password'])) {
    $jsonString = file_get_contents('./users/users.json');
    $jsonData = json_decode($jsonString, true);

    $userN = htmlspecialchars($_GET['username']);
    $passW = htmlspecialchars($_GET['password']);

    $found = false;
    foreach($jsonData as $user){
        header('Content-Type: application/json');
        if($user['username'] === $userN && $user['password'] === $passW) {
            $data = [
                "username" => $user['username'],
                "accessCode" => $user['accessCode'],
                "secretCode" => $user['secretCode']
            ];
            $found = true;
            echo json_encode($data);
        }
    }
    if(!$found){
        echo json_encode([]);
    }
}

?>