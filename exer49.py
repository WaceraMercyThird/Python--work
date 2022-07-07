# Making Sentences

class ParserError(Exception):
2 pass

class Sentence(object):
2
3 def __init__(self, subject, verb, obj):
4 # remember we take ('noun','princess') tuples and convert them
5 self.subject = subject[1]
6 self.verb = verb[1]
7 self.object = obj[1]

def peek(word_list):
2 if word_list:
3 word = word_list[0]
4 return word[0]
5 else:
6 return None

def match(word_list, expecting):
2 if word_list:
3 word = word_list.pop(0)
4
5 if word[0] == expecting:
6 return word
7 else:
8 return None
9 else:
10 return None


def skip(word_list, word_type):
2 while peek(word_list) == word_type:
3 match(word_list, word_type)


def parse_verb(word_list):
2 skip(word_list, 'stop')
3
4 if peek(word_list) == 'verb':
5 return match(word_list, 'verb')
6 else:
7 raise ParserError("Expected a verb next.")


def parse_object(word_list):
2 skip(word_list, 'stop')
3 next_word = peek(word_list)
4
5 if next_word == 'noun':
6 return match(word_list, 'noun')
7 elif next_word == 'direction':
8 return match(word_list, 'direction')
9 else:
10 raise ParserError("Expected a noun or direction next.")

def parse_sentence(word_list):
2 subj = parse_subject(word_list)
3 verb = parse_verb(word_list)
4 obj = parse_object(word_list)
5
6 return Sentence(subj, verb, obj)

