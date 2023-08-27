# Puppet rule to create ssh config file
class { 'ssh::client':
  options => {
    'IdentityFile' => '~/.ssh/school',
    'IdentitiesOnly' => 'yes',
    'PasswordAuthentication' => 'no',
  },
}
