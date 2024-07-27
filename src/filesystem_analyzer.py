import xml.etree.ElementTree as ET
from collections import defaultdict

def parse_filesystem_structure(xml_file):
    """Parse the filesystem structure from the XML file."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return root

def analyze_filesystem(root):
    """Analyze the filesystem structure and return relevant information."""
    structure = defaultdict(list)
    tasks = defaultdict(list)

    def traverse(element, path):
        if element.tag == 'directory':
            dir_name = element.get('name')
            new_path = f"{path}/{dir_name}" if path else dir_name
            structure[path].append(dir_name)

            for child in element:
                if child.tag == 'syncComputation':
                    for task in child.findall('task'):
                        tasks[new_path].append({
                            'name': task.get('name'),
                            'status': task.get('status')
                        })

                traverse(child, new_path)

    traverse(root, '')
    return dict(structure), dict(tasks)

def reflow_information(structure, tasks):
    """Reflow information based on the analyzed filesystem structure."""
    reflowed_info = []

    for path, directories in structure.items():
        reflowed_info.append(f"Path: {path}")
        reflowed_info.append(f"Subdirectories: {', '.join(directories)}")
        
        if path in tasks:
            reflowed_info.append("Tasks:")
            for task in tasks[path]:
                reflowed_info.append(f"  - {task['name']} (Status: {task['status']})")
        
        reflowed_info.append("")  # Add a blank line for readability

    return "\n".join(reflowed_info)

def main(xml_file):
    root = parse_filesystem_structure(xml_file)
    structure, tasks = analyze_filesystem(root)
    reflowed_info = reflow_information(structure, tasks)
    print(reflowed_info)

if __name__ == "__main__":
    main("filesystem_structure.xml")
