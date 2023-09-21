# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Facundo Frau
# Collaborators: -
# Time: -

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description

    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
    

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    
    def get_phrase(self):
        return self.phrase
    
    def is_phrase_in(self, text):
        text = text.lower()
        for char in string.punctuation:
            text = text.replace(char, ' ')
        while '  ' in text:
            text = text.replace('  ', ' ')
        
        phrase = self.get_phrase().lower().split(' ')
        text = text.split(' ')

        words_in_txt = all([word in text for word in phrase])
        if not words_in_txt:
            return False
        start_index = text.index(phrase[0])
        for i in range(1, len(phrase)):
            txt_index = i + start_index
            try:
                if phrase[i] != text[txt_index]:
                    return False
            except:
                return False
        return True                      

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        super().__init__(phrase)
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item Title, or False otherwise.
        """
        title = story.get_title()
        return super().is_phrase_in(title)

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        super().__init__(phrase)

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item Description, or False otherwise.
        """
        description = story.get_description()
        return super().is_phrase_in(description)

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, timestr):
        self.time = datetime.strptime(timestr, "%d %b %Y %H:%M:%S")
        self.time = self.time.replace(tzinfo=pytz.timezone("EST"))

# Problem 6
class BeforeTrigger(TimeTrigger):
    def __init__(self, timestr):
        super().__init__(timestr)

    def evaluate(self, story):
        """
        Returns True when a story is published strictly before
        the Trigger's time, or False otherwise.
        """
        pubdate = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        return pubdate.timestamp() < self.time.timestamp()


class AfterTrigger(TimeTrigger):
    def __init__(self, timestr):
        super().__init__(timestr)

    def evaluate(self, story):
        """
        Returns True when a story is published strictly after
        the Trigger's time, or False otherwise.
        """
        pubdate = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        return pubdate.timestamp() > self.time.timestamp()
    
# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, other_trigger):
        self.other_trigger = other_trigger
    
    def evaluate(self, story):
        return not self.other_trigger.evaluate(story)

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        eval_1 = self.trigger1.evaluate(story)
        eval_2 = self.trigger2.evaluate(story)
        return eval_1 and eval_2
    
# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        eval_1 = self.trigger1.evaluate(story)
        eval_2 = self.trigger2.evaluate(story)
        return eval_1 or eval_2


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    filtered = []
    for story in stories:
        triggered = any([trigger.evaluate(story) for trigger in triggerlist])
        if triggered:
            filtered.append(story)
    return filtered



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    trigger_list = []
    triggers = {}
    class_names = {'And': AndTrigger, 'Or': OrTrigger, 'Not': NotTrigger,
                   'Title': TitleTrigger, 'Description': DescriptionTrigger,
                   'After': AfterTrigger, 'Before': BeforeTrigger}
    for line in lines:
        line = line.split(',')
        if line[0] == 'ADD':
            for i in range(1, len(line)):
                trigger_name = line[i]
                trigger_list.append(triggers[trigger_name])
        else:
            trigger_type = line[1].capitalize()
            if trigger_type in ('And', 'Or'):
                trigger = class_names[trigger_type](triggers[line[2]], triggers[line[3]])
            elif trigger_type == 'Not':
                trigger = class_names[trigger_type](triggers[line[2]])
            else:
                trigger = class_names[trigger_type](line[2])
            triggers[line[0]] = trigger

    print(lines) # for now, print it so you see what it contains!
    return trigger_list



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # Uncomment for using hardcoded triggers instead of loading a txtfile
        # t1 = TitleTrigger("microsoft")
        # t2 = DescriptionTrigger("nvidia")
        # t3 = DescriptionTrigger("amd")
        # t4 = OrTrigger(t2, t3)
        # t5 = TitleTrigger("ai")
        # t6 = DescriptionTrigger("ukraine")
        # triggerlist = [t1, t4, t5, t6]

        # Problem 11
        # After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('./triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Pizzel Podcast RSS news feed
            stories.extend(process("https://pizzelpodcast.com/?format=rss"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

