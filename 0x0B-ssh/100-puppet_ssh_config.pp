#!usr/bin/pup

file{ '/etc/ssh/ssh_config':
    content => 
    'host 54.83.175.197
        User ubuntu
        IdentityFile ~/.ssh/school 
        PasswordAuthentication no'
}