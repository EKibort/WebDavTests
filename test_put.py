import unittest

import config
import webdavhelper

# RFC 4918 9.7
class WebdavCommand_put(unittest.TestCase):
    def setUp(self):
        self.UnexistingFile = '/test_file_5.txt'
        self.ExistingFile   = '/test_file_6.txt'
        self.Dav = webdavhelper.WebDav(config.WEBDAV_SRV_URL)

    def test_9_7_1_unexisting_file_return_201(self):
        response, content = self.Dav.put(self.UnexistingFile, body='content of test file')
        self.assertEqual(response.status, 201)

    def test_9_7_1_recreate_file_return_200(self):
        response, content = self.Dav.put(self.ExistingFile, body='new content of test file')
        self.assertEqual(response.status, 200)

    def test_9_7_1_without_an_appropriately_scoped_parent_collection_MUST_fail_409(self):
        response, content = self.Dav.put('/NotExistingPath/file.txt', body='new content of test file')
        self.assertEqual(response.status, 409)

    def test_9_7_1_with_no_content_type_server_MAY_detect_type_by_extension(self):
        self.Dav.put('/text.txt', body='content of test file')
        response, content = self.Dav.get('/text.txt')
        self.assertEqual(response['content-type'], 'text/plain')

        self.Dav.put('/text.doc', body='content of test file')
        response, content = self.Dav.get('/text.doc')
        self.assertEqual(response['content-type'], 'application/msword')

        self.Dav.put('/test.xml', body='content of test file')
        response, content = self.Dav.get('/text.xml')
        self.assertEqual(response['content-type'], 'text/html')

    def test_9_7_1_with_content_type_server_set_valid_content_type(self):
        self.Dav.put('/test2.doc', body='content of test file', extra_headers={'Content-Type':'text/plain'})
        response, content = self.Dav.get('/test2.doc')
        self.assertEqual(response['content-type'], 'text/plain')

    def test_9_7_1_can_change_content_type_during_override(self):
        self.Dav.put('/test.doc', body='content of test file', extra_headers={'Content-Type':'text/plain'})
        self.Dav.put('/test.doc', body='content of test file', extra_headers={'Content-Type':'text/html'})
        response, content = self.Dav.get('/test.doc')
        self.assertEqual(response['content-type'], 'text/html')


if __name__ == '__main__':
    unittest.main()