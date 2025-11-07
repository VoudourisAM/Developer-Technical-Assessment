#!/usr/bin/env python
# coding: utf-8

# ---
# ### Import Libraries
# ---

# In[1]:


from flask import Flask
from config import Config
from models import db
from routes.tasks import tasks_bp
from routes.visualize import visualize_bp

# ---
# ### app
# ---

# In[2]:


app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)
with app.app_context():
    db.create_all()

# Register Blueprints
app.register_blueprint(tasks_bp)
app.register_blueprint(visualize_bp)

if __name__ == "__main__":
    app.run(debug=True)






