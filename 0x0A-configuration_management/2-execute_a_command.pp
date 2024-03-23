#!/usr/bin/pup

exec { 'kill_killmenow_proceess':
command => '/usr/bin/pkill -9 killmenow'
}