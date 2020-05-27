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

Trie data structures have the advantage of having a very efficient lookup even if large amounts of data are stored in them. This is achieved by splitting up the lookup problem into smaller sub-problems. In this exercise homepage URL's are split up into smaller string sections, which are respectively stored in dictionaries. 

So, instead of looking up the entire URL in a large dictionary, each section of the URL is looked up in a small dictionary. For small dictionaries the lookup can be performed in constant time O(1), so an URL split up into r sections can be looked up in O(r).

|  | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| Adding h handler with route size r | O(h*r) ~ **O(h)** | O(h*r) ~ **O(h)** |
| Lookup handler for given route of size r | O(r) ~ **O(1)** | |

**h**: total number of handlers stored in Trie\
**r**: average size of URL route stored in Trie

For large homepages the number of handlers **h** is much larger then the average route **r**.

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