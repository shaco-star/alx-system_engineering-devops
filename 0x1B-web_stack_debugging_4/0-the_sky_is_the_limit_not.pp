# This Puppet manifest increases the amount of traffic an Nginx server can handle.


# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'test -f /etc/default/nginx && sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  require => Package['nginx'],
} ->

# Restart Nginx
exec { 'nginx-restart':
  command     => 'nginx restart',
  path        => '/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/etc/init.d/',
  refreshonly => true,
  subscribe   => Exec['fix--for-nginx'],
}
