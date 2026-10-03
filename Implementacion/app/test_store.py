import tempfile
import unittest
from pathlib import Path
from store import Store


class PermissionsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.store = Store(Path(self.temp.name) / 'lab.sqlite')
        self.user = self.store.save({'userName': 'ingeniero@example.test', 'title': 'mantenimiento', 'active': True})

    def tearDown(self):
        self.temp.cleanup()

    def test_maintenance_cannot_administer(self):
        self.assertTrue(self.store.permitted(self.user['id'], 'mantenimiento'))
        self.assertFalse(self.store.permitted(self.user['id'], 'admin'))

    def test_demotion_removes_previous_permission(self):
        self.store.save({'title': 'auditor'}, self.user['id'])
        self.assertFalse(self.store.permitted(self.user['id'], 'mantenimiento'))
        self.assertTrue(self.store.permitted(self.user['id'], 'registros'))

    def test_deactivation_blocks_existing_user_id(self):
        self.store.save({'active': False}, self.user['id'])
        self.assertFalse(self.store.permitted(self.user['id'], 'consulta'))

    def test_string_false_is_not_truthy(self):
        self.store.save({'active': 'false'}, self.user['id'])
        self.assertFalse(self.store.permitted(self.user['id'], 'consulta'))

    def test_unknown_role_is_denied(self):
        self.store.save({'title': 'director'}, self.user['id'])
        self.assertFalse(self.store.permitted(self.user['id'], 'consulta'))

    def test_identity_cannot_be_rebound(self):
        self.assertTrue(self.store.bind_identity(self.user['id'], 'subject-a'))
        self.assertFalse(self.store.bind_identity(self.user['id'], 'subject-b'))

    def test_deletion_blocks_old_session(self):
        self.store.remove(self.user['id'])
        self.assertFalse(self.store.permitted(self.user['id'], 'consulta'))


if __name__ == '__main__':
    unittest.main()
