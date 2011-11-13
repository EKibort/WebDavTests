import httplib2

class WebDav:

    def __init__(self, host):
        self.httpcon = httplib2.Http()
        self.host = host
        self.headers = {}
	
    def _send_request(self, request_method, path, body='', extra_headers={}):
        uri = httplib2.urlparse.urljoin(self.host, path)
        allheaders = dict(self.headers, **extra_headers)
        allheaders['Content-length']=str(len(body))
        resp, content = self.httpcon.request(uri, request_method, body=body, 
                                                        headers=allheaders)
        print "Response on '%s' : %s"%(request_method, resp)
        return resp, content

    def propfind(self, path, extra_headers={}):
        return self._send_request('PROPFIND',path, extra_headers=extra_headers)

    def put(self, path, body, extra_headers={}):
        return self._send_request('PUT',path, body=body, extra_headers=extra_headers)

    def get(self, path, extra_headers={}):
        return self._send_request('GET',path, extra_headers=extra_headers)
    

        
	
