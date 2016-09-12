#! /bin/bash

# This is a little CGI program
###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The MIME type of associated with the option body of the HTTP request.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.  
# HTTP_USER_AGENT:   Information about the browser/client that made requested.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. The most common methods are GET and POST.
# REQUEST_URI:       The URI of the request
# SERVER_PROTOCOL:   Currently HTTP/1.1
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address
# SERVER_PORT:       The port of the server
#      Added a content type and a blank line

echo "X-COMP-Class: Comp490"
echo "Instructor: Professor Fitzgerald"
echo "Content-type: text/html"
echo ""

if [ -n "$QUERY_STRING" ] ; then 
   cat  ./${QUERY_STRING}
fi

if [["$REQUEST_METHOD" == "POST"]]; then
  echo "Using POST method"
elif [[  "$REQUEST_METHOD" == "GET"  ]]; then
  echo "Using GET method"
fi

echo "<br>"
# parse query string variables
IFS='=&'
set -- $QUERY_STRING
echo ${1%=*} is ${2%*=}
# end of parse query string variables

echo "<br>"
echo "<html>"
echo "  <head>"
echo "    <title>This is my CGI program</title>"
echo "  </head>"
echo "	<body>"
echo "		<h1 style=\"color:orange;\">List of Shell Environment Variables:</h1>"
echo "Information: <em>$INFO</em><br />"
echo "CONTENT_TYPE:      $CONTENT_TYPE<br>"
echo "CONTENT_LENGTH:    $CONTENT_LENGTH<br>"
echo "GATEWAT_INTERFACE: $GATEWAT_INTERFACE<br>"
echo "HTTP_HOST:         $HTTP_HOST<br>"
echo "HTTP_USER_AGENT:   $HTTP_USER_AGENT<br>"
echo "QUERY_STRING:      $QUERY_STRING<br>"
echo "REQUEST_METHOD:    $REQUEST_METHOD<br>"
echo "REQUEST_URI:       $REQUEST_URI<br>"
echo "SERVER_PROTOCOL:   $SERVER_PROTOCOL<br>"
echo "SCRIPT_FILENAME:   $SCRIPT_FILENAME<br>"
echo "SCRIPT_NAME:       $SCRIPT_NAME<br>"
echo "SERVER_NAME:       $SERVER_NAME<br>"
echo "SERVER_PORT:       $SERVER_PORT<br><br>"
echo "Current time = " 
date
echo "<br>"
echo "	</body>"
echo "<html>"


# Read the body -- if it is a post
while read _post_line ; do
  echo ${_post_line} ";loop"
done 
echo $_post_line

exit 0


