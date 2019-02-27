import wikipedia
from bs4 import BeautifulSoup
import copy

def link_branch(main_topic):
    stuff = wikipedia.WikipediaPage(main_topic)
    links = stuff.links
    print("Subtopics:")
    for i, link in enumerate(links):
        print(i +1, ": ", link)
    subtopics_list = []
    user_choice_str = ""
    while user_choice_str != "done":
        print("type in 'all' for every subtopic to be added, and done to continue generating study guide")
        user_choice_str = input("which subtopics would you like(enter topic number)?")
        try:
            if user_choice_str == "all":
                subtopics_list = copy.deepcopy(links)
            elif user_choice_str == "done":
                pass
            else:
                subtopics_list.append(links[int(user_choice_str) -1])

        except:
            print("input must be between 1 and ", str(len(links)))
    return(subtopics_list)
def language_processing(summary):

def main():
    subtopics = link_branch("voltage")
    print(subtopics)
if __name__ == '__main__':
    main()
