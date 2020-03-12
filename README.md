# Application Security Interview Questions and Answers



### SAML
SAML SSO works by transferring the user’s identity from one place (the identity provider) to another (the service provider). This is done through an exchange of digitally signed XML documents.

Consider the following scenario: A user is logged into a system that acts as an identity provider. The user wants to log in to a remote application, such as a support or accounting application (the service provider). The following happens:

1. The user accesses the remote application using a link on an intranet, a bookmark, or similar and the application loads.
2. The application identifies the user’s origin (by application subdomain, user IP address, or similar) and redirects the user back to the identity provider, asking for authentication. This is the authentication request.
3. The user either has an existing active browser session with the identity provider or establishes one by logging into the identity provider.
4. The identity provider builds the authentication response in the form of an XML-document containing the user’s username or email address, signs it using an X.509 certificate, and posts this information to the service provider.
5. The service provider, which already knows the identity provider and has a certificate fingerprint, retrieves the authentication response and validates it using the certificate fingerprint.
6. The identity of the user is established and the user is provided with app access.



### Threat Modeling 
There are five major threat modeling steps:
1.  Defining security requirements. 
		a. For example, “The application shall not allow any customer to access the account information of any other customer"
2.  Creating an application diagram.  (DFD)
3.  Identifying threats. (STRIDE) 
		○ Spoofing
		○ Tampering
		○ Repudiation
		○ Information Disclosure
		○ Denial of service
		○ Elevation of privilege
4.  Mitigating threats. 
5. Validating that threats have been mitigated. 



