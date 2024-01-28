import json
import xml.etree.ElementTree as ET

def convert_to_junit(json_data):
    root = ET.Element("testsuite", name="UnrealEngineTests")
    tests_count = 0
    errors_count = 0
    for test in json_data["tests"]:
        testcase = ET.SubElement(root, "testcase", classname=test["fullTestPath"], name=test["testDisplayName"])
        tests_count += 1
        for entry in test["entries"]:
            ET.SubElement(testcase, "system-out").text = entry["event"]["message"]
        if test["state"] == "Success":
            testcase.set("status", "success")
        elif test["state"] == "Warning":
            testcase.set("status", "warning")
        else:
            testcase.set("status", "failure")
        testcase.set("time", "0.0")  # UE tests reports total testing duration but not individual test duration
        errors_count += test["errors"]

    root.set("time", str(json_data["totalDuration"]))
    root.set("tests", str(tests_count))
    root.set("failures", str(json_data["failed"]))
    root.set("errors",  str(errors_count))
    root.set("skipped", "0")  # skipped tests not yet handled 

    tree = ET.ElementTree(root)
    return tree

def convert_file():
    # Open the file with UTF-8 encoding 
    with open('./Reports/index.json', 'r', encoding='utf-8-sig') as file:
        json_data = json.load(file)
    
    junit_xml_tree = convert_to_junit(json_data)
    
    with open('./Reports/tests.xml', 'wb') as xml_file:
        junit_xml_tree.write(xml_file, encoding='utf-8', xml_declaration=True)
    
    print("Conversion successful. JUnit XML file generated.")

convert_file()