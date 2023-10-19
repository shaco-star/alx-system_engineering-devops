# This Puppet manifest enables the user 'holberton' to login and open files without error by increasing the file limits.

# Ensure the 'holberton' user exists
user { 'holberton':
  ensure => present,
} ->

# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'grep -q "^holberton hard" /etc/security/limits.conf && sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf || echo "holberton hard nofile 50000" >> /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  require => User['holberton'],
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'grep -q "^holberton soft" /etc/security/limits.conf && sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf || echo "holberton soft nofile 50000" >> /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  require => User['holberton'],
}
