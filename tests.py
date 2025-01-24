import os
import unittest as ut
from main import read_file, count_words_in_str_to_dict, create_sorted_words_report

class TestMethods(ut.TestCase):

  def setUp(self):
    with open('test_files/test.txt', 'w') as f:
      f.write('Essa é uma string com exatamente nove palavras.')
    with open('test_files/test2.txt', 'w') as f:
      f.write('Teste Teste Teste Teste Teste Teste   \n . ,')

  def tearDown(self):
    os.remove('test_files/test.txt')
    os.remove('test_files/test2.txt')
    if os.path.exists('relatório.txt'):
      os.remove('relatório.txt')

  def test_existing_read_file(self):
    read_text = read_file('test_files/test.txt')
    self.assertEqual(read_text, 'Essa é uma string com exatamente nove palavras')
    read_text = read_file('test_files/test2.txt')
    self.assertEqual(read_text, 'Teste Teste Teste Teste Teste Teste')

  def test_missing_read_file(self):
    self.assertRaises(FileNotFoundError, read_file, 'não_existe.txt')

  def test_count_words_int_str_to_dict(self):
    test_dict = count_words_in_str_to_dict(read_file('test_files/test2.txt'))
    expected_dict = {
      'Teste': 6,
    }
    self.assertEqual(test_dict, expected_dict)

  def test_create_sorted_words_report(self):
    create_sorted_words_report('test2.text', count_words_in_str_to_dict(read_file('test_files/test2.txt')))
    self.assertTrue(os.path.exists('relatório.txt'))


if __name__ == '__main__':
    ut.main()