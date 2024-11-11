import os
import xml.etree.ElementTree as ET

# Directory where your XML files are stored
directory = 'C:\\Users\\WhereverYouHeartdesires'

# Create the root element for the merged XML
merged_root = ET.Element("deck", name="Merged_Vocabulary")
fields = ET.SubElement(merged_root, "fields")
ET.SubElement(fields, "rich-text", name="Front", sides="11")
ET.SubElement(fields, "rich-text", name="Back", sides="01")
merged_cards = ET.SubElement(merged_root, "cards")

# Loop through each XML file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        filepath = os.path.join(directory, filename)
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        # Standardize "Avant" and "Arrière" to "Front" and "Back"
        for card in root.find("cards"):
            for field in card.findall('rich-text'):
                if field.get('name') == 'Avant':
                    field.set('name', 'Front')
                elif field.get('name') == 'Arrière':
                    field.set('name', 'Back')
            # Append standardized card to the merged XML
            merged_cards.append(card)

# Save the merged XML
output_file = os.path.join(directory, 'Merged_Vocabulary.xml')
merged_tree = ET.ElementTree(merged_root)
merged_tree.write(output_file, encoding='utf-8', xml_declaration=True)

print(f"Merged XML saved as {output_file}")
