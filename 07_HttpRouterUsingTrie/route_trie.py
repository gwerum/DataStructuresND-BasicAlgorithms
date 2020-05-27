import unittest
import pdb

class RouteTrieNode:
    def __init__(self, path, handler = None):
        self.path = path    # Path section: /.../.../path/.../..
        self.handler = handler 
        self.children = {}

    def __repr__(self, level=0):
        ret = "  "*level+repr(self.path)+": "+str(self.handler)+"\n"
        for child in self.children.values():
            ret += child.__repr__(level+1)
        return ret

    def insert(self, path):
        # Adds new child to node
        self.children[path] = RouteTrieNode(path)

class RouteTrie:
    # Stores all routes and handlers of the homepage
    def __init__(self, root_directory):
        # Homepage root holds main homepage URL
        self.root = RouteTrieNode(root_directory)

    def insert(self, handler, route_list):
        # Insert new handler for homepage path
        current_node = self.root

        for path in route_list:
            if path not in current_node.children:
                current_node.insert(path)
            current_node = current_node.children[path]

        current_node.handler = handler

    def find(self, route_list):
        # Returns handler for given homepage path, if existing
        current_node = self.root

        for path in route_list:
            children = current_node.children
            if path not in children:
                raise KeyError("No matching path found in Route Trie.")
            current_node = children[path]

        return current_node.handler

class Router:
    # Wrapper class for route trie and handle setter and getter
    def __init__(self, root_directory):
        # Initialize new route trie
        self.route = RouteTrie(root_directory)

    def __repr__(self):
        return self.route.root.__repr__()

    def add_handler(self, handler, homepage_path):
        # Add new handler for homepage path
        route_list = self.__split_path(homepage_path)
        self.route.insert(handler, route_list)

    def lookup(self, homepage_path):
        # Return handler from trie for given homepage path
        try:
            route_list = self.__split_path(homepage_path)
            # Remove trailing slash, if existing
            if route_list[-1] == '': 
                route_list = route_list[:-1]  
            # Get handler from route trie 
            handler = self.route.find(route_list)
            return handler

        except KeyError:
            return "No handler found."

    def __split_path(self, homepage_path):
        # Splits homepage path into route sections
        path_without_root = homepage_path.split(self.route.root.path)
        if path_without_root[0] == homepage_path:
            raise KeyError("Provided path doesn't match root path.")
        route_list = path_without_root[1].split('/')
        return route_list


# Test cases

nd256_classroom = {}
nd256_classroom['root'] = "https://classroom.udacity.com/nanodegrees/nd256/"

nd256_classroom['dashboard_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/dashboard/overview"

nd256_classroom['syllabus_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/syllabus/core-curriculum"

nd256_classroom['introduction_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/f74fc064-524b-4ee8-8fb1-570b3c31a993"

nd256_classroom['data_structures_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/b835ca8d-4269-4ca3-b911-c8ceb9cc0aa0"

nd256_classroom['basic_algorithms_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4"

nd256_classroom['advanced_algorithms_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/94ec3f1b-f3ae-4de4-acbc-ec4b27548116"

nd256_classroom['career_services_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/a9c18090-a4e5-47e0-9387-0edbe5e70743"

nd256_classroom['introduction_jupyter_notebooks_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/f74fc064-524b-4ee8-8fb1-570b3c31a993/modules/9bbb9a6d-d848-4153-a2fc-25065ee8d42d/lessons/5b27b2cf-9a9b-4d73-bd55-899a9731c864/concepts/1d3e3599-e99a-487f-9522-2508ff6a58c8"

nd256_classroom['introduction_faq_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/f74fc064-524b-4ee8-8fb1-570b3c31a993/modules/35f1ebc2-aa55-4a3c-acd0-79e5009a71fd/lessons/2f7e83a4-b637-4df1-a795-4cbfb5d8cd93/concepts/82499d32-744d-4c12-98b2-52bd3936f4b1"

nd256_classroom['introduction_welcome_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/f74fc064-524b-4ee8-8fb1-570b3c31a993/modules/9bbb9a6d-d848-4153-a2fc-25065ee8d42d/lessons/5b27b2cf-9a9b-4d73-bd55-899a9731c864/concepts/13036b92-b510-4d06-ae36-1358dd974ad4"

nd256_classroom['basic_algorithms_project_route_trie_handler()'] = "https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/bd252a0b-e9e7-473b-bcc1-bc7e3153568b/lessons/8ec390d0-e99d-44c0-88f9-f8f9faf467fc/concepts/8a8492a5-f76d-4dcc-a07c-3e2a2ca9b3c6"


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
        expected_handler = ["No handler found.", "No handler found."]
        for index, path in enumerate(lookup_paths):
            cls.run_test(path, expected_handler[index])

    def run_test(cls, lookup_path, expected_handler):
        print("\nLookup path:")
        print(lookup_path)
        print("Expected handler: {}".format(expected_handler))
        actual_handler = cls.router.lookup(lookup_path)
        print("Returned handler: {}".format(actual_handler))
        cls.assertEqual(actual_handler, expected_handler)

