#!/usr/bin/env python
# coding: utf-8

# ---
# ### Import Libraries
# ---

# In[1]:


import os


# ---
# ### config
# ---

# In[2]:


# Παίρνει αυτόματα το path του φακέλου όπου βρίσκεται το αρχείο
BASE_DIR = os.getcwd()  # παίρνει το τρέχον working directory

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'tasks.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# In[ ]:




