from unittest import TestCase
from  build import Node

class TestLinkedList(TestCase):
    def test_insert_to_front(self):
        try:
            from build import LinkedList
        except ImportError:
            self.assertFalse("No function found")

        linked_list = LinkedList(None)
        linked_list.insert_to_front(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: insert_to_front on a None')
        linked_list.insert_to_front(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: insert_to_front general case')
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(linked_list.get_all_data(), ['bc', 'a', 10])

    def test_append(self):
        try:
            from build import LinkedList
        except ImportError:
            self.assertFalse("No function found")

        print('Test: append on an empty list')
        linked_list = LinkedList(None)
        linked_list.append(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: append a None')
        linked_list.append(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: append general case')
        linked_list.append('a')
        linked_list.append('bc')
        self.assertEqual(linked_list.get_all_data(), [10, 'a', 'bc'])

    def test_find(self):
        try:
            from build import LinkedList
        except ImportError:
            self.assertFalse("No function found")

        print('Test: find on an empty list')
        linked_list = LinkedList(None)
        node = linked_list.find('a')
        self.assertEqual(node, None)

        print('Test: find a None')
        head = Node(10)
        linked_list = LinkedList(head)
        node = linked_list.find(None)
        self.assertEqual(node, None)

        print('Test: find general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        node = linked_list.find('a')
        self.assertEqual(str(node), 'a')

        print('Test: find general case with no matches')
        node = linked_list.find('aaa')
        self.assertEqual(node, None)

    def test_delete(self):
        try:
            from build import LinkedList
        except ImportError:
            self.assertFalse("No function found")

        print('Test: delete on an empty list')
        linked_list = LinkedList(None)
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: delete a None')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.delete(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: delete general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), ['bc', 10])

        print('Test: delete general case with no matches')
        linked_list.delete('aa')
        self.assertEqual(linked_list.get_all_data(), ['bc', 10])

        print('Success: test_delete\n')

    def test_len(self):
        try:
            from build import LinkedList
        except ImportError:
            self.assertFalse("No function found")

        print('Test: len on an empty list')
        linked_list = LinkedList(None)
        self.assertEqual(len(linked_list), 0)

        print('Test: len general case')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(len(linked_list), 3)