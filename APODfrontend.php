<!DOCTYPE html>
<html>
<body>

<?php
$servername = "localhost";
$username = "";
$password = "";
$dbname = "";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
$mysqli = mysqli_connect($servername, $username, $password, $dbname);


if (!$mysqli)
{
   echo 'Connection failed<br>';
   echo 'Error number: ' . mysqli_connect_errno() . '<br>';
   echo 'Error message: ' . mysqli_connect_error() . '<br>';
   die();
}
echo 'Successfully connected!<br>';


$sql = "SELECT id, title, url FROM apod";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
      echo "id: " . $row["id"]. " - title: " . $row["title"]. "picture: " . $row["url"] . "<br>";
    }
  } else {
    echo "0 results";
  }


?>

</body>
</html>
