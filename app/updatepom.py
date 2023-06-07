import json
import sys
import os
import xml.etree.ElementTree as ET
import pom_to_json

# Print the type of data variable
#print("Type:", type(data))
# Print the data of dictionary
#print("\nname:", data[0]['name'])
#print("\nrequirement:", data[0]['requirement'])


def update_pom(path_to_pom_in, path_to_pom_out):
  # Opening JSON file
  with open(path_to_pom_in) as json_file:
    data = json.load(json_file)

    tree = ET.parse(path_to_pom_in)

    pom = tree.getroot()

    for child in pom:
      #print(child.tag, child.attrib)
      for child2 in child.iter('dependency'):
        #print(child2.tag)
        rep_artifact = child2.find('artifactId').text
        rep_grp = child2.find('groupId').text
        rep_version = child2.find('version').text
        #print(rep_artifact)
        #print(rep_version)
        comp_rep_val = rep_grp + ':' + rep_artifact
        #print(comp_rep_val)
        for vuln_art in data:
          #print('vuln_art_name is : ', vuln_art['name'])
          if (vuln_art['name'] == comp_rep_val):
            print(rep_artifact)
            child2.find('version').text = '222222'

    tree.write(path_to_pom_out)


if __name__ == "__main__":
  # update_pom("./in/pomcopy.xml", "pomcopyout.xml")
  print("hello")
