alias ctrlnocaps="setxkbmap -option 'ctrl:nocaps'"
alias ping-lan="echo 192.168.1.{1..254} | xargs -n1 -P0 ping -c1 | grep \"bytes from\""
alias mount-samsung="sshfs raspberrypi:/mnt/samsung /mnt/samsung"
alias mount-motog="jmtpfs /mnt/motog"
