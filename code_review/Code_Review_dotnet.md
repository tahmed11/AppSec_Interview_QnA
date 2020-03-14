### SQL injection:
Unsafe:
String query = "SELECT account_balance FROM user_data WHERE user_name = " 
             + request.getParameter("customerName");
try {
    Statement statement = connection.createStatement( ... );
    ResultSet results = statement.executeQuery( query );
}

.NET – use parameterized queries like SqlCommand() or OleDbCommand() with bind variables
Safe: 
String query = "SELECT account_balance FROM user_data WHERE user_name = ?";
try {
  OleDbCommand command = new OleDbCommand(query, connection);
  command.Parameters.Add(new OleDbParameter("customerName", CustomerName Name.Text));
  OleDbDataReader reader = command.ExecuteReader();
  // …
} catch (OleDbException se) {
  // error handling
}



### XSS
.NET 4+
https://docs.microsoft.com/en-us/dotnet/api/system.web.security.antixss.antixssencoder?view=netframework-4.8
public class AntiXssEncoder : System.Web.Util.HttpEncoder

By default, ASP.NET applications are configured to use the AntiXssEncoder type for all output encoding.
The following example from an application-level Web.config file shows how the AntiXssEncoder type is set for an ASP.NET application:
<httpRuntime requestValidationMode="4.5" encoderType="System.Web.Security.AntiXss.AntiXssEncoder, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"/>


Recommendation:

Either update web.config file to use XSS encoder by default for all output as below or use it using individual input and output parameter using public class AntiXssEncoder : System.Web.Util.HttpEncoder 

Web.config file shows how the AntiXssEncoder type is set for an ASP.NET application:
<httpRuntime requestValidationMode="4.5" encoderType="System.Web.Security.AntiXss.AntiXssEncoder, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"/>


.NET less than 4
Anti-Cross Site Scripting Library V3.0
 1: using System; 
 2: using Microsoft.Security.Application; 
 3:  
 4: public partial class _Default : System.Web.UI.Page 
 5: { 
 6:     protected void Button1_Click(object sender, EventArgs e) 
 7:     { 
 8:     String Input = TextBox1.Text; 
 9:  
 10:     //Encode untrusted input and write output 
 11:     Response.Write(AntiXss.HtmlEncode(Input)); 
 12:     } 
 13: }

XML eXternal Entity injection (XXE)

Srf.documentdisable DTD

Most parser disable XML DTD by default. 
xmlDocument xmlDoc = new XMLDocument();
xmlDoc.XMLResolver=null //set this to disable DTD.


Deserialisation: See the section deserialisation 

### LDAP injection:
Use .NET Anti XSS 4+ for encoding LDAP Query using Microsoft.Security.Application.Encoder.LdapFilterEncode or Microsoft.Security.Application.Encoder.LdapDistinguishedNameEncode functions. 

Use: 
Encoder.LdapFilterEncode encodes input according to RFC4515 where unsafe values are converted to \XX where XX is the representation of the unsafe character

Encoder.LdapDistinguishedNameEncode encodes input according to RFC 2253 where unsafe characters are converted to #XX where XX is the representation of the unsafe character and the comma, plus, quote, slash, less than and great than signs are escaped using slash notation (\X). In addition to this a space or octothorpe (#) at the beginning of the input string is \ escaped as is a space at the end of a string.


JSON injection:Use .NET Anti XSS 4+ for encoding user input using AntiXssEncoder.HtmlEncode Method 
https://docs.microsoft.com/en-us/dotnet/api/system.web.security.antixss.antixssencoder.htmlencode?view=netframework-4.8#System_Web_Security_AntiXss_AntiXssEncoder_HtmlEncode_System_String_System_Boolean_


please perform input validation of  selectedId, if you are only expecting certain length and characters then validation should be performed accordingly.

