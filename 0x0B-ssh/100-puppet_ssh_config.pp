#!usr/bin/pup

file{ 'home/ubuntu/.ssh/ssh_config':
    content => 
    'host ubuntu@54.83.175.197
        IdentityFile ~/.ssh/school 
        PasswordAuthentication no'
}