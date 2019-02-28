from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
import copy

import docx2txt

def entity_grab():
    my_document = docx2txt.process("CEE_test_study_guide.docx")
    print(my_document)
    credential_path = "AutomatedStudyGuide-dad0ce7b030d.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

    client = language.LanguageServiceClient()
    text = my_document

    document = types.Document(content = text, type = enums.Document.Type.PLAIN_TEXT)
    entities = client.analyze_entities(document).entities
    name_set = set([])
    for entity in entities:
        entity_type = enums.Entity.Type(entity.type)
        print("=" * 20)
        print("name:", entity.name)
        print("type:", entity_type.name)
        print("salience", entity.salience)
        name_set.add(entity.name)
    name_list = list(name_set)
    for i, name in enumerate(name_list):
        print(i +1, ": ", name)
    subtopics_list = []
    user_choice_str = ""
    while user_choice_str != "done" and user_choice_str != "all":
        print("type in 'all' for every subtopic to be added, and done to continue generating study guide")
        user_choice_str = input("which subtopics would you like(enter topic number)?")

        if user_choice_str == "all":
            subtopics_list = copy.deepcopy(name_list)
            break
        elif user_choice_str == "done":
            break
        else:
            try:
                subtopics_list.append(name_list[int(user_choice_str) -1])
                break
            except:
                print("input must be between 1 and ", str(len(name_list)))
        print("user string", user_choice_str)
    return subtopics_list
