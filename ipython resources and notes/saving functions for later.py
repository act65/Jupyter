
# coding: utf-8

# In[ ]:




# In[ ]:




# In[ ]:




# In[6]:



def a():
    print('hello')
    return

def c():
    return 4

from inspect import getsource

get_ipython().magic('save -f lolz.py getsource(a)')




# In[7]:

import lolz as b

b.a()


# In[8]:

get_ipython().magic('save -a lolz.py getsource(c)')


# In[9]:

class LOL():
    def __init__(self):
        self.x = 1
        
get_ipython().magic('save -a lolz.py getsource(LOL)')

