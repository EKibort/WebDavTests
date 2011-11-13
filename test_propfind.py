'''import unittest

import config
import webdavhelper

# RFC 4918 9.1
class WebdavCommand_propfind(unittest.TestCase):
    def setUp(self):
        self.Dav = webdavhelper.WebDav(config.WEBDAV_SRV_URL)

    def test_prop1(self):
        response, content = self.Dav.propfind('/')
        #self.assertEqual();

    def test_must_empty_body_as_allprop():
        response, content = self.Dav.propfind('/',{'Depth':'0'})

    def test_must_depth_0_on_root(self):
        response, content = self.Dav.propfind('/',{'Depth':'0'})
        print response
        print content
        
    def test_must_depth_1_on_root(self):
        response, content = self.Dav.propfind('/',{'Depth':'1'})

    def test_should_depth_infinity_on_root(self):
        response, content = self.Dav.propfind('/',{'Depth':'infiniti'})

    def test_should_depth_empty_equal_to_infinity(self):
        response, content = self.Dav.propfind('/')



if __name__ == '__main__':
    unittest.main()
'''