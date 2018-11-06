class Trie:

	#Write Trie Class Here if you choose to implement the Trie
  def __init__(self,value='',end_word=False):
    self.children=[None]*26
    self.value=value
    self.end_of_word=end_word

 # get the value
  def get_value(self):
    return self.value

  # get children
  def get_children(self):
    return self.children

  # convert a char to a key for children list
  def convert_key(self,char):
    return ord(char)-ord('a')

 #insert a new word
  def insert(self,value=''):
    start=self.children
    end_word =False
    for ind_char,char in enumerate(value):
      key=self.convert_key(char)
      if not start[key]:
        #check if is the last char of the word
        if ind_char==len(value)-1:
          end_word=True
        new_trie=Trie(char,end_word)
        start[key]=new_trie
        start=new_trie.children
      else:
        children=start[key]
        start=children.children

  #delete a word from the trie
  def delete(self,value):
    start_list=self.children
    for ind_char,char in enumerate(value):
      key=self.convert_key(char)
      if not start_list[key]:
        return
      else:
        last=start_list
        start_list=start_list[key].children
    last[key].end_of_word =False
    if last[key].children==[None]*26:
      last[key].value=''

  #find a given word
  def find(self,value):
    start_list=self.children
    for ind_char,char in enumerate(value):
      key=self.convert_key(char)
      if start_list[key]:
        start_list=start_list[key].children
      else:
        return False
    return True

  #traverse the trie forming  words
  def traverse(self,word="",list_rest=[]):
    start_list=self.children
    for trie in start_list:
      if  trie:
        if trie.end_of_word:
          if word:
            if trie.children==[None]*26:
              word+=trie.value
              list_rest.append(word)
            else:
              trie.traverse(word+trie.value,list_rest)
        else:
          trie.traverse(word+trie.value,list_rest)
       
