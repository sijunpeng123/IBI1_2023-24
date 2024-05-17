import xml.dom.minidom
import xml.sax
import datetime
import matplotlib.pyplot as plt

def parse_with_dom(file_path):
    start_time= datetime.datetime.now()
    
    DOMTree = xml.dom.minidom.parse(file_path)
    terms = DOMTree.getElementsByTagName('term')
    molecular_function=0
    biological_process=0
    cellular_component=0
    for term in terms:
        namespaces = term.getElementsByTagName('namespace')
        for namespace in namespaces:
            ontology = namespace.firstChild.nodeValue.strip()
            if ontology == 'molecular_function':
                molecular_function += 1
            elif ontology == 'biological_process':
                biological_process += 1
            elif ontology == 'cellular_component':
                cellular_component += 1
    end_time =datetime.datetime.now()
    time_taken = end_time - start_time
    print("Time taken (DOM):", time_taken)
    print("Molecular function (DOM):",molecular_function)
    print("Biological process (DOM):",biological_process)
    print("Cellular component (DOM):",cellular_component)
    lib={'Molecular function':molecular_function,'Biological process':biological_process,'Cellular component':cellular_component}
    import matplotlib.pyplot as plt
    ontologies = list(lib.keys())
    counts=list(lib.values())
    plt.bar(ontologies, counts, color=['blue', 'green', 'red'])
    plt.xlabel('Ontology')
    plt.ylabel('Number of Terms')
    plt.title('Number of GO Terms by Ontology (DOM)')
    plt.show()
    return
    
dom_term_count = parse_with_dom("Desktop\work\IBI\IBI1_23-24\IBI1_2023-24\practical14.go_obo.xml")


ontology_dict = {}
start_time = datetime.datetime.now()
class GOhandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ''
        self.namespace = ''

    def startElement(self, name, attrs):
        self.currentdata = name

    def endElement(self, name):
        if self.currentdata == 'namespace':
            ontology_name = self.namespace.strip()
            
            if ontology_name in ontology_dict:
                ontology_dict[ontology_name] += 1
           
            else:
                ontology_dict[ontology_name] = 1
            self.namespace=''
    def characters(self, content):
        if self.currentdata == 'namespace':
            self.namespace += content

def count_namespace_occurrences(xml_file):
    handler = GOhandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    end_time = datetime.datetime.now()
    time_taken = end_time - start_time
    print("Time taken (SAX):", time_taken)
    return ontology_dict
ontology_counts = count_namespace_occurrences("/Desktop\work\IBI\IBI1_23-24\IBI1_2023-24\practical14.go_obo.xml")

print("Namespace Occurances (SAX):", ontology_dict)
ontologies=list(ontology_dict.keys())
counts=list(ontology_dict.values())

plt.bar(ontologies,counts,color=['blue', 'green', 'red'])
plt.xlabel('Ontology')
plt.ylabel('Number of Terms')
plt.title('Number of GO Terms by Ontology (SAX)')
plt.show()

# SAX is faster than DOM
