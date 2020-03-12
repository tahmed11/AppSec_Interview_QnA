
### Basic linux question:
#### TCP
   TCP Flags: SYN, ACK, RST, FIN, PSH, URG
   TCP handshake
      host A:SYN
      host B: SYN-ACK            
      host C: SYN
   End TCP connection:
      host A: FIN
      host B: FIN-ACK            
      host C: ACK
      
 #### Port numbers: 
   Kerberos - 88, syslogin- 514, FTP-20/21, SMTP-25, RDP-3389, IMAP-143, POP3-110, Telnet-23, SSH-22, SNMP-161, LDAP-389,
   DNS-53, SMB-445, 135-139
   
#### Ipv4 number of address: 2^32 
8.8.8.8 => 8 bits 4*8 = 32

#### Ipv6 number of address: 2^128

#### Subnet calculate: 
/22 or how many hosts in /22
2^32-22 = 2^10 (1024) hosts
192.x.x.x/22 => 1024 hosts

#### Unix vs linux
| Unix | Linux | 
|--- | --- |
|Proprietory | Open Source |
|Ex: MacOs, HP-UX, AIS, BSD, etc | Ubuntu, Fedora, CentOS, RedHat |
|Unix is not portable | Can be booted from USB stick |
|Unix is complete OS | Linux is mainly the kernel, everything else GUI + Utilities comes from distribution such as ubuntu, redhat,etc|

#### Redhat vs debian 
Main difference package manager.
Redhat yum -> rpm package manager
Debian apt -> deb package manager

### Encryption
#### Symmetric vs Asymmetric 
#### Diffie Hellman
Generate a shared secret in public for later symmetric encryption
#### RSA
Pregnerated public/private key pair to agree on a symmetric encryption

#### SSL handshake [One-way]
1. SSL Client sends "client hello" to server.
2. SSL Server responds with "Server hello" with list of cipher suites and server certificate
3. Client verify server certificate and chose the stronger cipher suite supported
4. Client key exchange: Send secret key encrypted with server public key.
5. Exchange message with encrypted shared secret key. 

		d. Digital signature
		e. HMAC 
	3. DNS
		a. How does dns works 
		b. Cname
		c. A and AAAA record 
		d. PTR record
		e. DNS SOA record
		f. When does DNS uses TCP and UDP
		g. How to do a DNS zone transfer 
	4. Linux command: 
		a. Show logged in user
		b. Change password
		c. List of all open files and processes that opened them
		d. Show firewall config in Linux
		e. How to switch user 
		f. What is sudo
		g. Show cpuinfo, meminfo
		h. Find a file in Linux 
		i. Search for a string in linux
		j. Show list of openports 
		k. How to block IP in Linux machine (tbc)
		l. Nohup
		m. Count the number of lines returned
		n. Parse string with delimiters
	5. Windows question:
		a. Show current logged in user
		b. Show windows system information
		c. Show list of all running processes
		d.  show list of all local users in the computer
		e. Show info about a user
		f. Find out all processes names and ports 
		g. Search for a file with name "proof.txt"
		h. Search for a string in a file
		i. Run a program as another user 
		j. Find file/folder permissions
		k.  find "mystring" in files 
		l. Show list of current installed patches 
		m. Find the name of the current domain 
		n. Process Vs thread 
		
	6. Tracer route 
	7. Ping 
	8. HTTP status codes: 
		a. Client error
		b. Client success
		c. Informational
		d. Redirection 
		e. Server error 
	9. Long answer: 
		a. Stack based buffer overflow 
		b. Threat modelling technique 
		c. OpenID connect
		d. Oauth 2.0
		e. SAML
		f. Kerberos
		g. NTLM 
	10. Google dorks: 
		a. How to narrow search to a site 
		b. How to find specific string in URL
		c. How to return only certain specific file format
		d. How to return text found in body 
#### Buffer overflow: 
		a. ESP register 
		b. EIP register 
		c. Mitigation of buffer overflow 
		d. Egghunter 
		e. Stack canary 
		f. Direction of stack 

There are different kind of buffer overflow vulnerabilities like stack based, heap based. Stack based are the most simplistic ones. As the name suggests stack based buffer overflow occurs due to overwrite of buffer space in memory. The below C program is vulnerable to buffer overflow. The main function call a vulnerable function. The vulnerable function takes 10 character strings as input parameter. Inside the function we use a vulnerable parameter to a fixed size buffer of 10 character size. When the main function calls the vulnerable function few things happen to the stack. First the parameter of the vulnerable function  will be pushed to the stack, then the return address of the main function will be saved on the stack. Once the function finish executing, stack pointer will return to this address to continue program execution. 


Vulnerable program:
void main(int argc, char *argv[]):
	{
	vuln_function(argv[1])
	return 0
	}
void vuln_function(char *str):
{
char buff[10];
strcpy(buff,str);
}
	12. Risk
		a. Define vulnerability
		b. Define risk 
		c. Define threat 
		d. Define Control 
	13. Container security - TBC
	14. Appsec
	15. CORS
	16. Same origin policy
	17. CSRF example
	18. CSRF prevention other than CSRF token
	19. HTTP flags: 
		a. HTTP only
		b. Secure flag
		c. CSP flag 
		d. HSTS flag
		e. X-Frame options
	20. OWASP Top 10:
		a. Types of SQL injection
		b. Type of XSS
		c. What is DOM based XSS
		d. XML external entities injection
		e. Deserialization 
