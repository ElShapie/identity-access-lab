import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('guard',Path(__file__).with_name('check_public_content.py'))
guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard)

class PublicContentTests(unittest.TestCase):
    def test_fictional_email_allowed(self):
        self.assertEqual(guard.text_issues('ingeniero@example.test'),[])

    def test_real_domain_email_rejected(self):
        self.assertTrue(guard.text_issues('person'+'@mail.com'))

    def test_github_secret_rejected(self):
        self.assertTrue(guard.text_issues('gh'+'p_'+'A'*36))

    def test_private_key_rejected(self):
        self.assertTrue(guard.text_issues('-----BEGIN '+'PRIVATE KEY-----'))

    def test_authenticated_camera_url_rejected(self):
        self.assertTrue(guard.text_issues('http'+'://user:password@camera.test/video'))

    def test_private_sheet_rejected(self):
        self.assertTrue(guard.text_issues('https://docs.google.com/'+'spreadsheets/d/'+'EXAMPLE'))

if __name__=='__main__':unittest.main()
