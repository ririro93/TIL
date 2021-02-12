# curl
> [curl tutorial](https://curl.haxx.se/docs/httpscripting.html#File_Upload_POST)

-F flag is same as --form

Back in late 1995 they defined an additional way to post data over HTTP. It is documented in the RFC 1867, why this method sometimes is referred to as RFC1867-posting.

This method is mainly designed to better support file uploads. A form that allows a user to upload a file could be written like this in HTML:
```html
<form method="POST" enctype='multipart/form-data' action="upload.cgi">
  <input type=file name=upload>
  <input type=submit name=press value="OK">
</form>
```
This clearly shows that the Content-Type about to be sent is multipart/form-data.

To post to a form like this with curl, you enter a command line like:

`curl --form upload=@localfilename --form press=OK [URL]`