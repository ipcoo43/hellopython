class Game:
	title = ''
	def __init__(self,tag):
		self.title = self.get_text(tag, 'a.title')
		self.comp = self.get_attr(tag, 'a.subtitle', 'title')
	
	def get_text(self, parent_tag, selector):
		tag = self.get_tag(parent_tag, selector)
 		return tag.text.strip()

	def get_attr(self, parent_tag, selector, attr_name):
		tag = self.get_tag(parent_tag, selector)
		return tag.get(attr_name).strip()

	 def get_tag(self, parent_tag, selector):
		tag = parent_tag.select(selector)
		if t==None or len(t) == 0:
			return None
		else:   
 			return tag[0]
	
	def __str__(self):
		return '{}\t{}'.format(self.title, self.comp)