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
Multiple clients exists, e.g., 
https://putty.org/
PuTTY is an SSH and telnet client, developed originally by Simon Tatham for the Windows platform.

### Linux & Mac 
Part of most installations. Otherwise simple installation via respective package manager.
```
sudo apt-get install openssh-client
```

## Is a SSH server running on a given port?
To test if an SSH server is running at a given IP or domain name we can use telnet to access port `22` (standard port of SSH). 
```
telnet gate.biologie.hu-berlin.de 22
```

## Information on SSH
The `man` files provide great information on the `ssh` and `scp` command.
```
man ssh
man scp
```

## Access to your itb files
Only information needed is the IP address (or DNS name of computer in network) of your computer.
This can be found easily via
```
ifconfig -a
```
or similar command on mac and windows.

In a first step we will access the `itbgate` computer. This is your gateway to the ITB computers. If you are not within the Humboldt network you have to use the humboldt VPN (via your email and password).

```bash
# ssh on itbgate
ssh <itbusername>@gate.biologie.hu-berlin.de
ssh koenig@gate.biologie.hu-berlin.de
```
Once we are on the gate computer we can already see our files (shared directories).
```
ls
```
In a second step we jump to the final computer, in this case my desktop computer 
in Inv110.
```
ssh <localusername>@<IP>
ssh mkoenig@172.30.10.12
```

## Debugging
If there are `ssh` issues most of the time
- your permissions on the files are wrong!
- you try to do something which is forbidden
- the port is not accessible, SSH server not running, or SSH server is very strict (only connections from certain subnets, ... see above forbidden).

Helpful information is available via the `-v` flag
```
ssh -v koenig@gate.biologie.hu-berlin.de
```

## SSH files in `$HOME/.ssh`
SSH has a few key files which are all located in the `$HOME/.ssh` directory:
- `known_hosts`: remote hosts which are known via their fingerprint
- `authorized_keys`: public keys which have access (via the corresponding private key)
- `id_rsa` and `id_rsa.pub`: private and public key pair. The public key is distributed to the `authorized_keys` file one wants to have access to 

## SSH config file
SSH allows to define generic SSH config & aliases via `.ssh/config`.
```bash
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
# add the public key to the remote server
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

## Executing commands via SSH
Executing command on remote computer. One can add commands directly at the end of the SSH command.
For instance display your files before running a scp command.
```
ssh itbgate ls
```
Multiple commands can be separated via `;`:
```
ssh itbgate ls; pwd
```
If commands require an interactive shell it can be enabled with the `-t` parameter
```
ssh itbgate top
ssh -t itbgate top
```

A local script can be executed against a remote machine via a simple `stdin` redirection.
```bash
# list contents
ls
# print working directory
pwd
# print hostname
hostname
```
Run the script
```
cat script.sh
ssh itbgate < scripts.sh
```

## SSH tunnels and ProxyCommand
Tunneling through SSH tunnels (jumping over nodes)
```
Host itbprime1
     User mkoenig
     Hostname 172.30.10.12
     ProxyCommand ssh -W %h:%p itbgate   
```

## X-forwarding
Using graphical programs from remote computer.
On the client side, the `-X` (capital X) option to ssh enables X11 forwarding. 
You can make this the default (for all connections or for a specific conection) with `ForwardX11 yes` in `~/.ssh/config`.
```
ssh -X itbdesktop gedit 
```

## Accessing your public github key
Simple setup of virtual machines and remote servers for SSH access
```
curl https://github.com/matthiaskoenig.keys >> $HOME/.ssh/authorized_keys
```

## Tools working on top of `scp`
Large ecosystem of tools and workflows on top of SSH. Examples are `scp`, `rsync` or `ansible` (configuration tool). To seamlessly work with these tools one must setup SSH correctly.

### `scp` - copying files
scp copies files between hosts on a network.  It uses ssh(1) for data transfer, and uses the same authentication and provides the same security as ssh(1).  scp will ask for passwords or passphrases if they are needed for authentication.

Directly works via `ssh`, so all `config` settings and key pairs from SSH can be used directly with scp.
```
man scp
cat > testfile
scp testfile itbgate:testfile
```

### `rsync` - easy way to synchronize folders between clients
rsync - a fast, versatile, remote (and local) file-copying tool

## Reverse SSH tunnels
`-R` flag
You can share your local file system with a remote location (it is basically SSH reverse).

## Piping data over SSH
Unix stream piping is one of the most powerful and widely-used techniques in everyday work with *nix systems. It allows you to transform data received on stdin and output the result to stdout, chaining a series of commands together. This simple approach allows for very powerful transformations and the speedup of many everyday tasks.

One common task is the copying of large file sets between servers. This can be done in many ways, perhaps using scp with the recursive flag, rsync or netcat - but I want to show you how to do this using data pipes.
```
tar -cz /var/www/ | ssh root@10.7.1.10 'cat -> ./www.tar.gz'
```

