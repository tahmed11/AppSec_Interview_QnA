### Javascript

Check for common javascript problems: 
* eval
* DOM based XSS: document.write, document.writeln(), innerHTML , outerHTML
grep -r -n "document.write" 
grep -r -n "document.writeln()" .
grep -r -n "innerHTML" .
grep -r -n "outerHTML" . 

### React

grep -r -n "dangerouslysetinnerHTML" . 
grep -r -n "JSON.stringify" . 


### Angular 
Check for bypass sanitization
* bypassSecurityTrustHtml
* bypassSecurityTrustScript
* bypassSecurityTrustStyle
* bypassSecurityTrustUrl
* bypassSecurityTrustResourceUrl

From <https://angular.io/guide/security> 
* grep -r -n "bypassSecurity" . 

Mitigate CSRF 
Angular has built-in CSRF protection mechanisms. All we have to do is adding the following lines to our AppModule:
```
imports: [
HttpClientModule,
HttpClientXsrfModule.withOptions({
cookieName: 'XSRF-TOKEN',
headerName: 'X-XSRF-TOKEN',
}),
],
```
The Angular app will then automatically intercept the XSRF-TOKEN cookie and send it back as a header, named X-XSRF-TOKEN , on every mutating request.
From <https://medium.com/@d.silvas/how-to-implement-csrf-protection-on-a-jwt-based-app-node-csurf-angular-bb90af2a9efd> 

Other References:
https://nvisium.com/blog/2019/01/10/angular-for-pentesters-part-1.html
https://www.whitehatsec.com/blog/the-security-angle-on-angular/

