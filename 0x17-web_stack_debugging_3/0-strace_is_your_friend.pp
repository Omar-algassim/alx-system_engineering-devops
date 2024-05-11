# change the setting file word press
exec { "change path":
    command => "sudo sed -i "s/.phpp/.php" /var/www/html/wp-settings.php",
    provider => shell,
}