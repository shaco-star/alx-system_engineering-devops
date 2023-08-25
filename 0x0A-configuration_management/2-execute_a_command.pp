#kill a process named killmenow
exec { 'kill-killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin',
}
