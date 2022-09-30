import main_utils
import unittest
unittest.TestLoader.sortTestMethodsUsing = None


class Test(unittest.TestCase):
    def test_a_setup_class(self):
        print('\r\nCreating the lambda function...')
        main_utils.create_lambda('lambda')

    def test_b_invoke_function_and_response(self):
        print('\r\nInvoking the lambda function...')
        payload = main_utils.invoke_function('lambda')
        self.assertEqual(payload['message'], 'Hello User!')

    def test_c_teardown_class(self):
        print('\r\nDeleting the lambda function...')
        main_utils.delete_lambda('lambda')

    def test_d_secret_setup_class(self):
        print('\r\nCreating the secret...')
        main_utils.create_secret('senha', '123')

    def test_e_get_secret_setup_class(self):
        print('\r\ngetting the secret...')
        value = main_utils.get_value('senha')
        self.assertEqual(value['SecretString'], '123')

    def test_f_delete_secret_setup_class(self):
        print('\r\nDeleting the secret...')
        main_utils.delete_secret('senha')
