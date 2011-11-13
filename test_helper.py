import unittest

import config
import webdavhelper

class SuiteHelper(unittest.TestCase):
    def setUp(self):
        self.Helper = webdavhelper.WebDav(config.WEBDAV_SRV_URL)

    def test_initial_instance_settings(self):
        self.assertEqual(self.Helper.host, config.WEBDAV_SRV_URL)


if __name__ == '__main__':
    unittest.main()