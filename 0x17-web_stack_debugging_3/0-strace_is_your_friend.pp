# automated puppet file fix that figures out why Apache is returning 500 error

exec { 'wordpress_fix':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
