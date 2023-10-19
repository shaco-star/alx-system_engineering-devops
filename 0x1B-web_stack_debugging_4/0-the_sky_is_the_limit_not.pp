# This Puppet manifest increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT in the default file
exec { 'increase-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep -q "15" /etc/default/nginx', # Ensure the sed command only runs if necessary
} ->

# Restart Nginx using service command for reliability
exec { 'restart-nginx':
  command     => 'service nginx restart',
  path        => '/usr/sbin:/usr/bin:/sbin:/bin', # Updated path to include common locations for service command
  refreshonly => true, # Ensures Nginx is only restarted if the ulimit was actually increased
}
