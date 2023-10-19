# This Puppet manifest increases the amount of traffic an Nginx server can handle.


# Increase the ULIMIT of the default file in nginx
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx server
exec { 'nginx-restart':
  command     => 'nginx restart',
  path        => '/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/etc/init.d/'
}
