import string
from ps7 import *
		
def main():
	koala = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
	trigger = TitleTrigger("koala")
	
	print trigger.evaluate(koala)	
	
main()
