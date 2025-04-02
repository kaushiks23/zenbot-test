#!/usr/bin/env python
# coding: utf-8

# In[4]:


from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ZenBot test app is live!"}

@app.get("/secret")
async def get_secret():
    value = os.getenv("TEST_SECRET", "Not Set")
    return {"TEST_SECRET": value}


# In[5]:




