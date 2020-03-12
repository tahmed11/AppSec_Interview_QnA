### SQL injection:
Use prepared statement PDO

	<?php 
	 $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
	$stmt = $conn ->prepare("Select id,name from products where size=?");
	$stmt->bindParam(':size',$size);
	$stmt->execute()
	?>
	
	Vuln code:
	<? Php
	$query="select id, name from products where size ="$size";
	$result=odbc_exec($conn,$query);
	?>


### XSS:
Vuln code:

if( array_key_exists( "name", $_GET ) && $_GET[ 'name' ] != NULL ) {
	// Feedback for end user
	$html .= '<pre>Hello ' . $_GET[ 'name' ] . '</pre>';
}
Remediation:
$name = htmlspecialchars( $_GET[ 'name' ] ); 

### XXE:
Libxml_disable_entity_loader(true)


### PHP Object injection:
In order to successfully exploit a PHP Object Injection vulnerability two conditions must be met:
	• The application must have a class which implements a PHP magic method (such as __wakeup or __destruct) that can be used to carry out malicious attacks, or to start a “POP chain”.
	• All of the classes used during the attack must be declared when the vulnerable unserialize() is being called, otherwise object autoloading must be supported for such classes.

The most common fix is to replace the usage of serialize and unserialize with json_encode and json_decode. 

Note: PHP 7 and higher support an option for “allowed_classes” in unserialize(), this is a good way to prevent people from injecting unexpected objects,

From <https://pagely.com/blog/object-injection-vulnerabilities-in-php/> 


