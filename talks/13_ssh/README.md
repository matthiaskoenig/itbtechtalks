# Secure Shell (SSH)
 `ssh` (SSH client) is a program for logging into a remote machine and for executing commands on a remote machine.  It is intended to provide secure
     encrypted communications between two untrusted hosts over an insecure network.
     X11 connections, arbitrary TCP ports and UNIX-domain sockets can also be for‐
     warded over the secure channel.

     ssh connects and logs into the specified hostname (with optional user name).
     The user must prove his/her identity to the remote machine using one of sev‐
     eral methods (see below).

## Installation
### Windows



Linux 

## Information on SSH
The `man` files provide great information on the `ssh` and `scp` command.
```
man ssh
man ss


## Access to your itb files
Only information needed is the IP address (or DNS name of computer in network) of your computer.
```
ifconfig -a
```

First one jumps on the itbgate computer
```bash
# ssh on itbgate
ssh <itbusername>@gate.biologie.hu-berlin.de
ssh koenig@gate.biologie.hu-berlin.de
```
and than on the machine you want access to
```
ssh <localusername>@<IP>
ssh mkoenig@172.30.10.12
```

## SSH files in `.ssh`
- `known_hosts`: remote hosts which are known via their fingerprint
- `authorized_keys`: public keys which have access (via the corresponding private key)
- `id_rsa` and `id_rsa.pub`: private and public key pair. The public key is distributed to the `authorized_keys` file one wants to have access to 

## SSH config file
SSH allows to define generic SSH config & aliases via `.ssh/config`.
```
Host itbgate
     User koenig
     Hostname gate.biologie.hu-berlin.de
```

## ssh - passwordless (login via key pairs) 
Access via key files & ssh-copy-id
ssh-agent to manage keys
To get access we create a key pair and deploy the public key to the computer we want access to:
```bash
# create new key
man ssh-keygen
ssh-keygen -t rsa -b 4096 -f itb
# store in SSH agent
man ssh-add
ssh-add itb
#
man ssh-copy-id
ssh-copy-id -i itb.pub itbgate
```
We can now access the itbgate without password via our keys.
If we delete the `authorized_keys` or remove our host computer from it we can no longer access the server.
```
ssh itbgate
cd .ssh
less authorized_keys
rm authorized_keys
exit
```
No we can't login, but have to redeploy the keys.
```
ssh itbgate
ssh-copy-id -i itb.pub itbgate
```

The SSH agent

# Executing command via SSH
executing command on remote computer





# SSH tunnels and ProxyCommand
Tunneling through SSH tunnels (jumping over nodes)
```

```

# X-forwarding
Using graphical programs from remote computer.


# Accessing your public github key
Simple setup of virtual machines and remote servers for SSH access
```
curl https://github.com/matthiaskoenig.keys >> $HOME/.ssh/authorized_keys
```


## Tools working on top of `scp`
# `scp` - copying files
scp copies files between hosts on a network.  It uses ssh(1) for data transfer, and uses the same authentication and provides the same security as ssh(1).  scp will ask for passwords or passphrases if they are needed for authentication.

Directly works via `ssh`, so all `config` settings and key pairs from SSH can be used directly with scp.
```
man scp

```


Tools on top of SSH (scp, rsync, ...)



