<?php
$host="localhost";
$user="root";
$pass=" ";
$database="db1";
$connection=Mysqli_connect($host,$user,$pass,$database);
if($connection){
	echo "successfully connected<br>";
}
else{
	die("could not connect");
}
$sql="INSERT INTO contact(name,email,phone) VALUES('John','john@gmail.com','12345')";
mysqli_query($connection,$sqli);
mysqli_close($connection);