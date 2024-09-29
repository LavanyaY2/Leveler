import streamlit as st
import spacy
import spacy.cli
import hashlib

spacy.cli.download("xx_ent_wiki_sm")
spacy.cli.download("en_core_web_sm")

nlp = spacy.load("xx_ent_wiki_sm")

def namehasher(name):
    hash_object = hashlib.md5(name.encode())  
    hash_value = hash_object.hexdigest()
    unique_id = int(hash_value, 16) % 1000000  
    return unique_id

def anonymize(name, address, contact, skills, education, experience):
    hashedname = namehasher(name)
    text = f"""
    Name = {hashedname}
    Address: {address}
    Contact: {contact}
    Education: {education}
    Skills: {skills}
    Experience: {experience}
"""
    doc = nlp(text)
    anontext = text
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE", "LOC", "DATE", "EMAIL", "PHONE", "ADDRESS"]:
            anontext = anontext.replace(ent.text, f"[{ent.label_}]")

    return anontext


def apply():
    # "confirm details"
    # "we'll anonymize identifying information before sending your application to this employer. you can select whether they receive your score for their job posting"
    # button -> confirm

    # #selectbox to choose if score will be sent as well
    if st.button("Confirm Application", key="anonymize"):
        anonymize(uname, uaddress, ucontact, uskills, ueducation, uexperience)




