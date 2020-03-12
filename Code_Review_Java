### SQL injection: 

Prepared statement: it's easier to use org.springframework.jdbc.core.JdbcTemplate from the framework it's provide prepared statement by default
SqlParameterSource namedParameters = new MapSqlParameterSource().addValue("id", 1);
return namedParameterJdbcTemplate.queryForObject(
  "SELECT FIRST_NAME FROM EMPLOYEE WHERE ID = :id", namedParameters, String.class);

PreparedStatement stmt = connection.prepareStatement("SELECT * FROM users WHERE userid=? AND password=?");
stmt.setString(1, userid);
stmt.setString(2, password);
ResultSet rs = stmt.executeQuery();


SQL/ORM injection using TypeQuery:
From <https://software-security.sans.org/developer-how-to/fix-sql-injection-in-java-persistence-api-jpa> 

Vulnerable Usage
1	List results = entityManager.createQuery("Select order from Orders order where order.id = " + orderId).getResultList();
2	List results = entityManager.createNativeQuery("Select * from Books where author = " + author).getResultList();
3	int resultCode = entityManager.createNativeQuery("Delete from Cart where itemId = " + itemId).executeUpdate();

Secure Usage
1	/* positional parameter in JPQL */
2	Query jpqlQuery = entityManager.createQuery("Select order from Orders order where order.id = ?1");
3	List results = jpqlQuery.setParameter(1, "123-ADB-567-QTWYTFDL").getResultList();
1	/* named parameter in JPQL */
2	Query jpqlQuery = entityManager.createQuery("Select emp from Employees emp where emp.incentive > :incentive");
3	List results = jpqlQuery.setParameter("incentive", new Long(10000)).getResultList();
1	/* named query in JPQL - Query named "myCart" being "Select c from Cart c where c.itemId = :itemId" */
2	Query jpqlQuery = entityManager.createNamedQuery("myCart");
3	List results = jpqlQuery.setParameter("itemId", "item-id-0001").getResultList();
1	/* Native SQL */
2	Query sqlQuery = entityManager.createNativeQuery("Select * from Books where author = ?", Book.class);
3	List results = sqlQuery.setParameter(1, "Charles Dickens").getResultList();


### XSS: 

XSS spring framework: 
import org.springframework.web.util.HtmlUtils;
Encodeinput = HtmlUtils.htmlEscape(input)

For output encoding:
OWASP Java HTML Sanitizer
import org.owasp.html.Sanitizers;
import org.owasp.html.PolicyFactory;
PolicyFactory sanitizer = Sanitizers.FORMATTING.and(Sanitizers.BLOCKS);
String cleanResults = sanitizer.sanitize("<p>Hello, <b>World!</b>");

From <https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html> 

Vuln code:
 public AttackResult completed(@RequestParam String editor) {
        String unescapedString = org.jsoup.parser.Parser.unescapeEntities(editor, true);
        try {
            if (editor.isEmpty()) return trackProgress(failed().feedback("xss-mitigation-3-no-code").build());
            Document doc = Jsoup.parse(unescapedString);
            String[] lines = unescapedString.split("<html>");


### DOM Based XSS: 
Don’t use the following to accept user input: 
 element.innerHTML = "<HTML> Tags and markup";
 element.outerHTML = "<HTML> Tags and markup";
document.write("<HTML> Tags and markup");
 document.writeln("<HTML> Tags and markup");

Use safer javascript functions such as: textContent or innerText :
element.textContent = untrustedData; 
element.innerText = untrustedData; 


Generic mitiation against XSS:1. Set HTTPOnly cookie so cookie cannot be accessed by client side code
	2. Set CSP header, source to self so only javascript payload from selected site can be loaded and executed. 
		CSP header automatically disable 'unsafe_inline' and 'unsafe_eval'
		Unsafe_inline: allows resources embedded in the page such as inline <script> elements, style elements and javascript urls. 
		Unsafe_eval: allows the use of javascript eval function. 

### JSON injection:
JSON sanitiser: 
Use json-sanitizer as dependency.
 <dependency>
<groupId>com.mikesamuel</groupId>
<artifactId>json-sanitizer</artifactId>
<version>1.0</version>
</dependency>
 In Below code we are read data as UTF-8 string and then we are sanitizing the string before converting it to java object. PFA the code as well.
 
responseString = EntityUtils.toString(httpResponse.getEntity(),"UTF-8");
String wellFormedJson = com.google.json.JsonSanitizer.sanitize(responseString);
                               
O readValue = mapper.readValue(wellFormedJson, responseType);
response.setOutput(readValue);


### XXE:
Disable DTD while parsing XML. 
Different XML parser has different mechansim to disable XXE.
For example: 
Or.xml.sax.XMLReader
Reader.setFeature("http://apache.org/xml/features/…load_external_dtd",false)


XXE Attack:<?xml version><!DOCTYPE foo[<!ENTITY xxe SYSTEM "file://etc/passwd >]] 

<!ENTITY dteyybzent SYSTEM "http://hitWP5ElLuA1m.bxss.me/"> ]> &dteyybzent;


Vuln code:
 public AttackResult createNewComment(@RequestBody String commentStr) throws Exception {
        String error = "";
        try {
            Comment comment = comments.parseXml(commentStr);
            comments.addComment(comment, false);


### Deserialization: 
 
Vulnerable program: 
    @ResponseBody
    AttackResult completed(@RequestParam String token) throws IOException {
        String b64token;
        byte [] data;
        ObjectInputStream ois;
        Object o;
        long before, after;
        int delay;

        b64token = token.replace('-', '+').replace('_', '/');
        try {
            data = Base64.getDecoder().decode(b64token);
            ois = new ObjectInputStream( new ByteArrayInputStream(data) );
        } catch (Exception e) {
            return trackProgress(failed().build());
        }

        before = System.currentTimeMillis();
        try {
            o = ois.readObject();

 
	1. Don’t use readObject() 
	2. Don't use vulnerable JSON parser

Use a safer readObject method instead of readObject().
For example: data= safeReadObject(Data.class, safeClasses, 10,50, inputStream)
This method should implement return type, list of expected classes to deserialize input to max 10 objects and 50 input bytes. 
For full implementation refer to contrast security java deserialisation. 


### SSRF: 
Vulnerable code:
 protected AttackResult furBall(String url) {
        try {
                StringBuffer html = new StringBuffer();

                if (url.matches("http://ifconfig.pro")){
                    URL u = new URL(url);
                    URLConnection urlConnection = u.openConnection();
                    BufferedReader in = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
                    String inputLine;
    
### CSRF: 
IN springframework include CSRF as follows:
Form Submissions
The last step is to ensure that you include the CSRF token in all PATCH, POST, PUT, and DELETE methods. This can be done using the _csrf request attribute to obtain the current CsrfToken. An example of doing this with a JSP is shown below:
<c:url var="logoutUrl" value="/logout"/>
<form action="${logoutUrl}"
    method="post">
  <input type="submit"
    value="Log out" />
  <input type="hidden"
    name="${_csrf.parameterName}"
    value="${_csrf.token}"/>
</form>

From <https://docs.spring.io/spring-security/site/docs/3.2.0.CI-SNAPSHOT/reference/html/csrf.html
