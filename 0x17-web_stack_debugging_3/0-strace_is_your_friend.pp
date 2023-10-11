# Fixing the 500 Apache error
exec { 'fix_typo_in_wordpress':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  onlyif  => 'test -f /var/www/html/wp-settings.php && grep -q phpp /var/www/html/wp-settings.php',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
}
