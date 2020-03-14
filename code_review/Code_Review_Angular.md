https://nvisium.com/blog/2019/01/10/angular-for-pentesters-part-1.html
https://www.whitehatsec.com/blog/the-security-angle-on-angular/


Check for bypass sanitization 
• bypassSecurityTrustHtml
• bypassSecurityTrustScript
• bypassSecurityTrustStyle
• bypassSecurityTrustUrl
• bypassSecurityTrustResourceUrl
From <https://angular.io/guide/security> 
• Grep -r -n "bypassSecurity" . 


Mitigate CSRF 
Angular has built-in CSRF protection mechanisms. All we have to do is adding the following lines to our AppModule:

imports: [
HttpClientModule,
HttpClientXsrfModule.withOptions({
cookieName: 'XSRF-TOKEN',
headerName: 'X-XSRF-TOKEN',
}),
],
The Angular app will then automatically intercept the XSRF-TOKEN cookie and send it back as a header, named X-XSRF-TOKEN , on every mutating request.

From <https://medium.com/@d.silvas/how-to-implement-csrf-protection-on-a-jwt-based-app-node-csurf-angular-bb90af2a9efd> 
