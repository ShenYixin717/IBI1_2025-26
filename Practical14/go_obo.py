import time
import os
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'go_obo.xml')

# DOM
import xml.dom.minidom

start_dom = time.time()
DOM = xml.dom.minidom.parse(file)
term_list = DOM.getElementsByTagName("term")

max_info_dom = {
    "molecular_function": (0, ""),
    "biological_process": (0, ""),
    "cellular_component": (0, "")
}
for term in term_list:
    go_id_node = term.getElementsByTagName("id")[0].firstChild
    go_id = go_id_node.data
    go_namespace_node = term.getElementsByTagName("namespace")[0].firstChild
    go_namespace = go_namespace_node.data if go_namespace_node else ""
    is_a_list = term.getElementsByTagName("is_a")
    is_a_count = len(is_a_list)
    if go_namespace in max_info_dom:
        if is_a_count > max_info_dom[go_namespace][0]:
            max_info_dom[go_namespace] = (is_a_count, go_id)

end_dom = time.time()
dom_time = end_dom - start_dom


# print the final conclusion
print('DOM:')
for ns, (cnt, gid) in max_info_dom.items():
    print(f"{ns}: {gid} has {cnt} elements")
print(f"DOM time: {dom_time:.4f} s")



# SAX
import xml.sax

# init the class
class Handler(xml.sax.ContentHandler):
    def __init__(self):
        self.max_info = {
            "molecular_function": (0, ""),
            "biological_process": (0, ""),
            "cellular_component": (0, "")
        }
        self.current_id = ""
        self.current_namespace = ""
        self.current_is_a_count = 0
        self.current_tag = ""
        self.in_term = False

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "term":
            self.in_term = True
            self.current_id = ""
            self.current_namespace = ""
            self.current_is_a_count = 0

    def characters(self, content):
        if self.in_term:
            if self.current_tag == "id":
                self.current_id += content.strip()
            elif self.current_tag == "namespace":
                self.current_namespace += content.strip()

    def endElement(self, tag):
        if tag == "term":
            ns = self.current_namespace
            cnt = self.current_is_a_count
            gid = self.current_id
            if ns in self.max_info:
                if cnt > self.max_info[ns][0]:
                    self.max_info[ns] = (cnt, gid)
            self.in_term = False
        elif tag == "is_a" and self.in_term:
            self.current_is_a_count += 1
        self.current_tag = ""


if __name__ == "__main__":
    start_sax = time.time()
    parser = xml.sax.make_parser()
    handler = Handler()
    parser.setContentHandler(handler)
    parser.parse(file)
    end_sax = time.time()
    sax_time = end_sax - start_sax

    print('\nSAX:')
    for ns, (cnt, gid) in handler.max_info.items():
        print(f"  {ns}:{gid} has {cnt} elements")
    print(f"SAX time: {sax_time:.4f} s")

# comparison
if dom_time > sax_time:
    print("\nConclusion: SAX is faster for large XML files.")
elif dom_time < sax_time:
    print("\nConclusion: DOM is faster for large XML files.")
else:
    print("\nConclusion: Their speed is the same.")