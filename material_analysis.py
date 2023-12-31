# -*- coding: utf-8 -*-
"""Material_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UaPwI83x3ANgifCB3C0K9duPY1IUqC4o
"""

import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define the text data for the masks
text_data = """
101955 -masks band. The first/ forth layers are PP non-woven fabrics. The second layer is PP meltblown woven fabrics. The third layer is PP hot cotton.Tight fit, polluted air proof, adjustable nose clip, suitable for different face types.

100237 - Soft cotton material
Washable  & reusable
Comfortable & easy to wear
One size fits most. 100% Cotton.

99830 - Inner Layer - Soft mesh pattern that causes no irritation against the skin
	Outer Layer - Comfortable breathing space between 3 layers of mesh and nano filter
	3D Shape - Designed with special technology to comfortably fit against the face line
	Chin Guard - For a secure and comfortable fit
	Stopper - Convenient for adjustment

Outer - 100% polyester
Inner1 - 99% pet, 1% pvdf
Inner2 - 100% polyester

102734 - Effectively Block Droplets, Catkins, Dust and Pollen
3-Layer Filtration
Good Air Permeability 30% meltdown fabric, 70% non-woven fabric.

99829 - Inner Layer - Soft mesh pattern that causes no irritation against the skin
Outer Layer - Comfortable breathing space between 3 layers of mesh and nano filter
3D Shape - Designed with special technology to comfortably fit against the face line
Chin Guard - For a secure and comfortable fit
Stopper - Convenient for adjustment
Outer - 100% polyester
Inner1 - 99% pet, 1% pvdf
Inner2 - 100% polyester


101692 - Soft cotton material
Washable & reusable
Comfortable & easy to wear
One size fits most. 100% Cotton.

100837 - Non-woven fabric (outer layer, lining, filter), steel wire (nose bridge), nylon wire (earloop).
"""

# Process the text data using spaCy
doc = nlp(text_data)

# Analyze the text data
materials = []
features = []

for token in doc:
    # Check if the token is a noun or an adjective
    if token.pos_ in ["NOUN", "ADJ"]:
        # Check if the token is part of a noun chunk (phrase)
        if any(token in chunk for chunk in doc.noun_chunks):
            # Check if the token is in a noun chunk with specific keywords (e.g., "layer", "material", "fabric")
            if any(token.text in chunk.text for chunk in doc.noun_chunks if "layer" in chunk.text or "material" in chunk.text or "fabric" in chunk.text):
                materials.append(token.text)
            else:
                features.append(token.text)

# Print the unique materials and features
print("Materials:", set(materials))
print("Features:", set(features))

