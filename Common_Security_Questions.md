
### Basic networking question:
#### OSI model
All People Seems To Need Data Processing

| # | Layer | Protocol |
| --- | --- | --- |
| 1 | Physical| Ethernet, 802.11 a/b/g/n|
| 2 | Data | Ethernet, 802.11 a/b/g/n |
| 3 | Network | IP, ICMP, IGM, OSPF, RIP, IPSEC |
| 4 | Transport | TCP, UDP |
| 5 | Session | Sockets, SOCKS, RPC, NetBIOS, Named pipes |
| 6 | Presentation | SSL, TLS, MIME |
| 7 | Application | HTTP, Websockets |

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
| TCP | UDP | 
|--- | --- |
|Connection oriented | Connection less |
|Guaranteed transmission| No Guarantee |
|Error checking and out of order | NO error checking and no order of data received |

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

Private address range
10.0.0.0    - 10.255.255.255
172.16.0.0  - 172.31.255.255
192.168.0.0 - 192.168.255.255

#### DNS
* How does dns works 
* Cname – canonical name ex: example.com, www.example.com
* A and AAAA record – A and AAAA are type of address record map. Host to an IP address. A is ipv4 and AAAA is for ipv6. 
* PTR record – reverse of an A record. 
* DNS SOA record
*  DNS use TCP for zone transfer, UDP for name queries. 
* How to do a DNS zone transfer: 
	dig dns1.target.org -t axfr
	dnsrecon.py -a -d dns1.target.org

![alt text](https://0xpatrik.com/content/images/2018/06/takeover_basic.png)

#### Traceroute
Sends ICMP echo request packets with increasing TTL values. First packet will be of TTL value  1, so first host will return unreachable. Second packet will be of TTL value of 2 so second host will return unreachable. This process continue until destination is reached. 

#### Ping
Sends ICMP echo messages to the host. Once the host received the packets, the host responds. This way total round trip time is calculated. 

#### Unix vs linux
| Unix | Linux | 
|--- | --- |
|Proprietary | Open Source |
|Ex: MacOs, HP-UX, AIS, BSD, etc | Ubuntu, Fedora, CentOS, RedHat |
|Unix is not portable | Can be booted from USB stick |
|Unix is complete OS | Linux is mainly the kernel, everything else GUI + Utilities comes from distribution such as ubuntu, redhat, etc|

#### Redhat vs debian 
Main difference package manager.
Redhat yum -> rpm package manager
Debian apt -> deb package manager

### Encryption
#### Symmetric vs Asymmetric 
#### Diffie Hellman
Generate a shared secret in public for later symmetric encryption
#### RSA
Pre-generated public/private key pair to agree on a symmetric encryption

#### SSL handshake [One-way]
1. SSL Client sends "client hello" to server.
2. SSL Server responds with "Server hello" with list of cipher suites and server certificate
3. Client verify server certificate and chose the stronger cipher suite supported
4. Client key exchange: Send secret key encrypted with server public key.
5. Exchange message with encrypted shared secret key. 

#### Digital signature
Sign with private key, receiver verifies with public key. 

#### HMAC (Hashed based Message Authentication Code)
MAC = hash(Key | Message)
We don’t only use MAC because it is weak and subject to length extension attack, hence HMAC is used. 

HMAC Secret key => k shared between two parties. 
k => k1 and k2 
two subkeys (k1 and k2) are derived from k.
HMAC = hash(k2 | hash(k1|message))
HMAC is used for data integrity and authenticity of messages. 


#### Linux command: 
* Show logged in user - w
* Change password - passwd
* List of all open files and processes that opened them - lsof -i
* Show firewall config in Linux - cat /etc/iptables
* How to switch user - su
* What is sudo - 
* Show cpuinfo, meminfo - cat /etc/cpuinfo, cat /etc/meminfo
* Find a file in Linux  - find /home -name "search.txt"
* Search for a string in linux - grep -r -n "search_string" /home
* Show list of openports - netstat -abno
* Nohup
* Count the number of lines returned - wc -l 
* Parse string with delimiters - cut -d ":" -f1:f2

#### Windows commands:
* Show current logged in user – query user
*  Show windows system information - systeminfo
* Show list of all running processes – tasklist /SVC
* Show list of all local users in the computer – net users 
* Show info about a user – net user bob
* Find out all processes names and ports – netstat -abno
* Search for a file with name "proof.txt" – dir /S /P “proof.txt” 
* Search for a string in a file – findstr /s /c:”search_string”
* Run a program as another user – runas /noprofile /user:Administrator cmd.exe
*  Find file/folder permissions - icacls.exe
* Show list of current installed patches  = wmic qfe
* Find the name of the current domain – wmic computersystem get domain

* <b>Process Vs thread </b>
* Process:
Process means any program in execution. A process can create other child processes. Process run on their own memory hence they run on isolation. Each process start with single thread but can create multiple threads. 
* Thread: 
A thread is an entity within a process. All threads of a process share it's virtual address space and system resources. 

#### HTTP status codes: 
* Client error -4xx
* Client success -2xx
* Informational -1xx
* Redirection – 3xx
* Server error -5xx


### Authentication and Authorisation protocols 		
#### SAML
SAML SSO works by transferring the user’s identity from one place (the identity provider) to another (the service provider). This is done through an exchange of digitally signed XML documents.

Consider the following scenario: A user is logged into a system that acts as an identity provider. The user wants to log in to a remote application, such as a support or accounting application (the service provider). The following happens:
![SAML image](https://developers.onelogin.com/assets/img/pages/saml/sso-diagram.svg)
1. The user accesses the remote application using a link on an intranet, a bookmark, or similar and the application loads.
2. The application identifies the user’s origin (by application subdomain, user IP address, or similar) and redirects the user back to the identity provider, asking for authentication. This is the authentication request.
3. The user either has an existing active browser session with the identity provider or establishes one by logging into the identity provider.
4. The identity provider builds the authentication response in the form of an XML-document containing the user’s username or email address, signs it using an X.509 certificate, and posts this information to the service provider.
5. The service provider, which already knows the identity provider and has a certificate fingerprint, retrieves the authentication response and validates it using the certificate fingerprint.
6. The identity of the user is established and the user is provided with app access.

#### OpenID connect

![OpenID Connect](https://miro.medium.com/max/236/1*FdNO85lCooAVlnrEa-lxvQ.jpeg) 

![OpenID connect - Authorisation code grant](https://miro.medium.com/max/655/1*h1u_qXi3Np3kYu_eqG3hFw.jpeg) 
1. End user wants to login to your application via “Login with Google” and send the request to your application. 
2. Client application redirects the user to Google login page. 
3. This is where the user is presented with Login page or if already logged in then ask for consent.
4. User grants their consent or reject.
5. If the user grants access then the authorization server will send an authorization code to the client.
6. With the authorization code, the Client requests for an access token and ID token. ID token is a unique identifier of the end user.
7. With the access token, the application asks the resource server to ask for specific resources such as user’s contact details from Google contacts, etc.

For full OpenID connect you can visit my other blog post [here](https://medium.com/faun/threat-modeling-openid-connect-oauth-2-0-for-beginners-using-owasp-threat-dragon-part-1-b9e396fd7af9)

#### Kerberos
#### NTLM
![NTLM](https://filestore.community.support.microsoft.com/api/images/45bc59ef-a2e7-4a75-a129-8be12a01dd16?upload=true)
The following steps present an outline of NTLM noninteractive authentication. The first step provides the user's NTLM credentials and occurs only as part of the interactive authentication (logon) process.
1. (Interactive authentication only) A user accesses a client computer and provides a domain name, user name, and password. The client computes a cryptographic hash of the password and discards the actual password.
2. The client sends the user name to the server (in plaintext).
3. The server generates a 16-byte random number, called a challenge or nonce, and sends it to the client.
4. The client encrypts this challenge with the hash of the user's password and returns the result to the server. This is called the response.
5. The server sends the following three items to the domain controller:
        User name
        Challenge sent to the client
        Response received from the client
6. The domain controller uses the user name to retrieve the hash of the user's password from the Security Account Manager database. It uses this password hash to encrypt the challenge.
7. The domain controller compares the encrypted challenge it computed (in step 6) to the response computed by the client (in step 4). If they are identical, authentication is successful.

Ref: https://docs.microsoft.com/en-us/windows/win32/secauthn/microsoft-ntlm 

#### Threat Modeling 
There are five major threat modeling steps:
1. Defining security requirements. 
		a. For example, “The application shall not allow any customer to access the account information of any other customer"
2. Creating an DFD application diagram.  
3. Identifying threats. (STRIDE) 
		○ Spoofing
		○ Tampering
		○ Repudiation
		○ Information Disclosure
		○ Denial of service
		○ Elevation of privilege
4. Mitigating threats. 
5. Validating that threats have been mitigated. 

#### Google dorks: 
* How to narrow search to a site 
Specifically searches that particular site and lists all the results for that site. 	site:"www.google.com" 
* How to find specific string in URL
Searches for a URL matching one of the keywords. 	inurl:"keyword"
* How to return only certain specific file format
Searches for a particular filetype mentioned in the query. 	filetype:"pdf"
* How to return text found in body
Searches for the occurrences of keywords all at once or one at a time. 	intext:"keyword"

#### Buffer overflow: 
There are different kind of buffer overflow vulnerabilities like stack based, heap based. Stack based are the most simplistic ones. As the name suggests stack based buffer overflow occurs due to overwrite of buffer space in memory. The below C program is vulnerable to buffer overflow. The main function call a vulnerable function. The vulnerable function takes 10 character strings as input parameter. Inside the function we use a vulnerable function(strcpy) to a fixed size buffer of 10 character size. When the main function calls the vulnerable function few things happen to the stack. First the parameter of the vulnerable function  will be pushed to the stack, then the return address of the main function will be saved on the stack. Once the function finish executing, stack pointer will return to this address to continue program execution. Now if we send a parameter with more than 10 characters say 100 character, then the return address will overwrite the buffer. Strcpy will copy the extra 90 characters beyond the allocated space. Since we control the buffer we can control arbitary memory address as the return address. Then the program execution will jump to the arbitary address where we can put our shellcode. 

Vulnerable program:
```
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
```
<b> Mitigation of buffer overflow</b>:
1. Dont use vulnerable functions such as strcpy, etc.
2. Always do bound checking
3. Enabled by default ASLR -> Address space layout randomization
4. DEP -> Dynamic execution prevention 
    bypass DEP -> ROP gadget
5. Stack canaries


### Risk
#### Vulnerability
A weakness in a system or asset that makes a threat potentially more likely to occur.

#### Threat 
Any circumstance that may have a negatic impact to an asset. 

####  Risk 
Risk is combination of threat probability and loss/impact to business. 
Risk = Impact x Likelihood

#### Control 
Mechanism used to restrain, regulate or reduce vulnerabilities. Controls can be corrective, detective, preventive or deterrent. 

### NIST Cyber security framework:
1. Identify
2. Protect
3. Detect
4. Respond
5. Recover

#### Web Security related questions
##### SQL injection
Types of SQL injection
1. Inband or inline: Output directly visible
2. Blind based injection: cannot see output
3. Second order SQL injection: Injection get triggered after another function is called. 

Manual exploitation of SQL injection [here](https://github.com/tahmed11/appsec_interview/blob/master/manual_mysqli.md)
Do take the time to learn how to manually exploit SQL injection. 

##### Cross site scripting
Types of XSS
1. Reflected XSS: Requests get bounced back from the server. 
2. Stored XSS: Requests are stored and sent back from the server. 
3. Dom based XSS: XSS payload is executed as a result of modifying the DOM environment in the victim’s browser. The payload never gets sent to the server. Example: 
```
Vulnerable code: <script>document.write(“<b>current url: </b>:”+document.baseURI);</script>
Attack payload: http://example.com/test.html#<script>alert(1)</script> 
```
<b>Mitigation of DOM based XSS: </b>
* Don’t use vulnerable function for untrusted input such as eval(), element.innerHTML , element.outerHTML, document.write(), document.writeln()
* Use safer javascript functions such as: textContent or innerText:

<b>Generic mitigation against XSS: </b>
1. Do output encoding, see language specific guides. 
2. Set HTTPOnly flag so cookies are not accessible by client side JavaScript.
3. The HTTP Content-Security-Policy response header allows website administrator to control resources the user agent is allowed to load for a given page. Policies can be tailored to only allow scripts to be loaded from specific domain to avoid loading malicious scripts. 
Content-Security-Policy: default-src: ‘self’, script-src: http://example.com

Also CSP header automatically disable unsafe_inline and unsafe_eval functions which further restricts XSS. 
‘unsafe_inline’: Allow resources embedded in the page, such as inline <script> elements, <style> slements and javascripts URLs. 
‘unsafe_eval’: Allows the use of javascript eval function. 

#### Deserialization


#### Same origin policy
Same origin policy defines:
1.Each site has it’s own resources like cookie, DOM and javascript namespace
2.Each page take it’s origin from it’s URL (protocol, domain and port).
3.Script run it in the context of the origin which they are loaded. It doesn’t matter where you load it from only where it is finally executed. 
4.Many resources like media and image are passive resources. They don’t have access to objects and resources in the context they are loaded. 
Example: 
A site with origin A can:
1.Load a script from origin B, but it works in A’s context. 
2.Can load from images, CSS, videos from Site B.
3.Can load a page from origin B by iframe.
4.Cannot reach DOM of the iframe loaded from Origin B. 
#### CORS 
When a browser loads a webpage, it enforces Same origin policy which means that it only allows content to be fetched from the same origin as the web page. However in some cases a webpage may need to access assets from multiple origins. 

#### CSRF 
CSRF example:
<img src="http://192.168.0.104/xxxx/csrf_2.php?account=123-45678-90&amount=100&action=transfer" width="0" height="0" border="0">
Browser loads the following since the user is already logged in to the application. 
CSRF Mitigation:
* CSRF token
* Ask for password/2FA for sensitive operation. 
	
#### HTTP flags: 
* <b>HTTP only</b> – Cookie not accessible by client side javascript. 
* <b>Secure flag</b> – Only send cookie over HTTPS 
* <b>CSP flag:</b>
The HTTP Content-Security-Policy response header allows website administrator to control resources the user agent is allowed to load for a given page. Policies can be tailored to only allow scripts to be loaded from specific domain to avoid loading malicious scripts. 
Content-Security-Policy: default-src: ‘self’, script-src: http://example.com

* <b>HSTS flag:</b>
HTTP Strict transport security is to enforce the use of HTTPS by the user agent. 
* <b>X-Frame options</b>
X-Frame options tells the browser whether you want to allow your site to be frame or not. By preventing a browser from framing your site you can defend against <b>clickjacking</b> attacks. 
Recommended: X-Frame-Options: SameOrigin. 
