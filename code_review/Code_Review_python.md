### SQL injection :

Vuln code:
    # BAD -- Using string formatting   
```
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
        user = cursor.fetchone()
```
GOOD -- Using parameters
```
        cursor.execute("SELECT * FROM users WHERE username = %s", username)
        user = cursor.fetchone()
```
BAD -- Manually quoting placeholder (%s)
```
        cursor.execute("SELECT * FROM users WHERE username = '%s'", username)
        user = cursor.fetchone()
```
From <https://help.semmle.com/wiki/display/PYTHON/SQL+query+built+from+user-controlled+sources> 

Remediation:
```
	Connection = mysql.connector.connect(host,db,user,pwd)
	Cursor = connection.cursor(prepared=True)
	Sql_query_insert="Insert into Employee (id,name,…) values (%s,%s,%s)
	Insert_tuple_1=(1,"Jason",….)
	Cursor.execute(sql_query_insert,insert_tuple)
	Connection.commit()
```
### Code execution:
```
  def code_execution(request):
      if request.method == 'POST':
          first_name = base64.decodestring(request.POST.get('first_name', ''))
          #BAD -- Allow user to define code to be run.
          exec("setname('%s')" % first_name)

  def code_execution(request):
      if request.method == 'POST':
          first_name = base64.decodestring(request.POST.get('first_name', ''))
          #GOOD --Call code directly
          setname(first_name)
```
  From <https://help.semmle.com/wiki/display/PYTHON/Code+injection> 

### XXE:
Vulnerable code: 
```
  from xml.dom.pulldom import START_ELEMENT, parse
  @bottle.post('/pulldom')
  def pulldom():
      doc = parse(bottle.request.body)
      for event, node in doc:
          doc.expandNode(node)
      return(str(doc))

  From <https://www.acunetix.com/blog/web-security-zone/how-to-mitigate-xxe-vulnerabilities-in-python/> 
```
Mitigation: don’t use vulnerable XML parser and disable DTD if used. 

###  XSS prevention:
html.escape() for Python 3.2 upwards or cgi.escape() older versions of Python.

