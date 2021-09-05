#!/usr/bin/env python
# coding: utf-8

# In[ ]:


txt = input("Enter your sentence: ")


# In[ ]:


txt = txt.split("_")


# In[ ]:


new_list = []
for text in txt:
    lower_txt = text.lower()
    new_list.append(lower_txt)
    # new_list.append(lower_txt)


# In[ ]:


new_sentence = ' '.join(new_list)
# new_sentence = ' '.join(new_list)

# In[ ]:


print(new_sentence)


# In[ ]:




