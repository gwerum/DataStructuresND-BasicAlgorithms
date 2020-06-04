## Explanation for route_trie.py

### Task

The task of this exercise is to a implement a *Trie data structure* for storing all HTTPS request handlers of a homepage and its subpages. The focus is to implement the trie holding all routes (URL's) of the subpages, for the request handlers strings as dummy structures are used.

### Code explanation

Three classes have been implemented:

#### class Router(): Serves as interface class for handling requests.
1. Router()::**add_handler**(*str handler, str homepage_path*): Adds new dummy handler for given homepage path and stores it in Trie.
2. Router()::**lookup**(*str homepage_path*): Returns handler for requested homepage path, if existing.

#### class RouteTrie(): Implementation of actual Trie data structure for storing routes and handlers.
1. RouteTrie()::**insert**(*str handler, list[str] route_list*): adds new handler to Trie under given route list.
2. RouteTrie()::**find**(*list[str] route_list*): returns handler from given route list, if existing.

#### class RouteTrieNode(): Implements single node of route trie.

---

### Runtime efficiency

The methods for adding a new handler and looking up an existing handler have both the same runtime efficiency of order `O(r*c)`, where **r** is the route length (the number of sections the path is split into) and **c** is the average number of childs per Trie node. For looking up or storing a handler the Trie needs to be *walked through* section-by-section (r) and in each step the list of childs (c) needs to be searched.

The advantage of a Trie comes into play during lookup, since the lookup usually doesn't always start from the root. Considering the homepage example, one usually needs the handlers of direct neighbours (sub-pages or the parent page), which then only requires *walking* one step.

|  | Time complexity | Space complexity 
| ------------------- | --------------- | ---------------- |
| Adding a single handler to Trie | **O(r\*c)** | **O(r-s)** |
| Lookup handler from Trie | **O(r\*c)** | |

**r**: average number of split sections per path\
**s**: average number of shared sections per path\
**c**: average number of children c per Trie node

---

### Test Cases

The following three test cases have been implemented to test the Router classes:

1. **Test 1: Lookup of existing handlers**: Checks if existing handlers are correctly returned for given URL request.
2. **Test 2: Lookup with trailing slash**: Checks if existing handlers are correctly returned when URL request contains trailing slash.
3. **Test 3: Request for non-existing handlers**: Checks class behaviour for non-existing handlers.

The test cases can be executed using the following command:

```
python -m unittest route_trie.py
```