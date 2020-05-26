import unittest
import pdb
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, path, handler = None):
        # Initialize the node with children as before, plus a handler
        self.path = path
        self.handler = handler
        self.children = {}

    def __repr__(self, level=0):
        ret = "  "*level+repr(self.path)+": "+str(self.handler)+"\n"
        for child in self.children.values():
            ret += child.__repr__(level+1)
        return ret

    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode(path)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_directory):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_directory)

    def insert(self, handler, path_list):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for path in path_list:
            if path not in current_node.children:
                current_node.insert(path)
            current_node = current_node.children[path]

        current_node.handler = handler


    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for path in path_list:
            children = current_node.children
            if path not in children:
                return None
            current_node = children[path]

        return current_node.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_directory):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie(root_directory)

    def __repr__(self):
        return self.route.root.__repr__()

    def add_handler(self, handler, path):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)

        self.route.insert(handler, path_list)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        try:
            path_list = self.split_path(path)
        except ValueError:
            return None
        if path_list[-1] == '':
            path_list = path_list[:-1] # Remove trailing slash
        return self.route.find(path_list)

    def split_path(self, path):
        # Splits complete path from root path and returns path sections
        path_without_root = path.split(self.route.root.path)
        if path_without_root[0] == path:
            raise ValueError("Error: Provided path doesn't match root path.")
        return path_without_root[1].split('/')


# Test cases

nd256_classroom = {}
nd256_classroom['root'] = "https://classroom.udacity.com/nanodegrees/nd256/"

nd256_classroom['dashboard'] = "https://classroom.udacity.com/nanodegrees/nd256/dashboard/overview"

nd256_classroom['syllabus'] = "https://classroom.udacity.com/nanodegrees/nd256/syllabus/core-curriculum"

nd256_classroom['introduction'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/f74fc064-524b-4ee8-8fb1-570b3c31a993"

nd256_classroom['data_structures'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/b835ca8d-4269-4ca3-b911-c8ceb9cc0aa0"

nd256_classroom['basic_algorithms'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4"

nd256_classroom['advanced_algorithms'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/94ec3f1b-f3ae-4de4-acbc-ec4b27548116"

nd256_classroom['career_services'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/a9c18090-a4e5-47e0-9387-0edbe5e70743"

nd256_classroom['introduction-jupyter-notebooks'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/f74fc064-524b-4ee8-8fb1-570b3c31a993/modules/9bbb9a6d-d848-4153-a2fc-25065ee8d42d/lessons/5b27b2cf-9a9b-4d73-bd55-899a9731c864/concepts/1d3e3599-e99a-487f-9522-2508ff6a58c8"

nd256_classroom['introduction-faq'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/f74fc064-524b-4ee8-8fb1-570b3c31a993/modules/35f1ebc2-aa55-4a3c-acd0-79e5009a71fd/lessons/2f7e83a4-b637-4df1-a795-4cbfb5d8cd93/concepts/82499d32-744d-4c12-98b2-52bd3936f4b1"

nd256_classroom['introduction-welcome'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/f74fc064-524b-4ee8-8fb1-570b3c31a993/modules/9bbb9a6d-d848-4153-a2fc-25065ee8d42d/lessons/5b27b2cf-9a9b-4d73-bd55-899a9731c864/concepts/13036b92-b510-4d06-ae36-1358dd974ad4"

nd256_classroom['basic_algorithms-project-route_trie'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/bd252a0b-e9e7-473b-bcc1-bc7e3153568b/lessons/8ec390d0-e99d-44c0-88f9-f8f9faf467fc/concepts/8a8492a5-f76d-4dcc-a07c-3e2a2ca9b3c6"


class TestTrieRouter(unittest.TestCase):
    """docstring for TestTrieRouter"""
    @classmethod
    def setUpClass(cls):
        super(TestTrieRouter, cls).setUpClass()
        cls.router = Router(nd256_classroom.pop('root'))
        for page in nd256_classroom.keys():
            cls.router.add_handler(page, nd256_classroom[page])

    def test_lookup(cls):
        print("\n##### Test case 1: lookup of existing handlers #####")
        lookup_paths = nd256_classroom.values()
        expected_handler = list(nd256_classroom.keys())
        for index, path in enumerate(lookup_paths):
            cls.run_test(path, expected_handler[index])

    def test_lookup_trailing_slash(cls):
        print("\n##### Test case 2: lookup of paths with trailing slash #####")
        lookup_paths = nd256_classroom.values()
        expected_handler = list(nd256_classroom.keys())
        for index, path in enumerate(lookup_paths):
            cls.run_test(path+'/', expected_handler[index])

    def test_invalid_lookup(cls):
        print("\n##### Test case 3: lookup of non-existing handlers #####")
        lookup_paths = ["https://www.udemy.com/", "https://classroom.udacity.com/nanodegrees/nd256/final_certificate"]
        expected_handler = [None, None]
        for index, path in enumerate(lookup_paths):
            cls.run_test(path, expected_handler[index])

    def run_test(cls, lookup_path, expected_handler):
        print("\nLookup path:")
        print(lookup_path)
        print("Expected handler: {}".format(expected_handler))
        actual_handler = cls.router.lookup(lookup_path)
        print("Returned handler: {}".format(actual_handler))
        cls.assertEqual(actual_handler, expected_handler)

'''

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
'''
