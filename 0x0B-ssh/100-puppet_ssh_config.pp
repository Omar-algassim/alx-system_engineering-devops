#!usr/bin/pup

file{ 'root/.ssh/ssh_config':
    content => 'host ubuntu@98.98.98.98
     IdentityFile ~/.ssh/school 
     BatchMode yes'
}