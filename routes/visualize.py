#!/usr/bin/env python
# coding: utf-8

# ---
# ### Import Libraries
# ---

# In[1]:


from flask import Blueprint, Response
import io
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

import pandas as pd
import matplotlib.pyplot as plt 

import mplcyberpunk as mplcp
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec

import seaborn as sns


# ---
# ### visualize
# ---

# In[3]:


visualize_bp = Blueprint("visualize_bp", __name__, url_prefix="/visualize")

@visualize_bp.route("/status")
def visualize_status():
    # Σύνδεση στη βάση
    engine = create_engine("sqlite:///tasks.db")
    df = pd.read_sql("SELECT * FROM task", engine)
    data = pd.DataFrame(df)
    status = data['status'].unique()
    status_counts = data["status"].value_counts()

    # Δημιουργία bar & pie plot
    plt.style.use("cyberpunk") #Background color
    pal_red = sns.color_palette("flare") #Color

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,7))

    ax1.bar(status_counts.keys()[1], status_counts.values[1], width=0.7, alpha=0.8, color=pal_red[3])
    ax1.text(x=status_counts.keys()[1], y=status_counts.values[1].sum()/1.5, s=status_counts.values[1], color='White', weight='extra bold', ha='center', fontsize=15) #Text of labels

    ax1.bar(status_counts.keys()[0], status_counts.values[0], width=0.7, alpha=0.6, color=pal_red[3])
    ax1.text(x=status_counts.keys()[0], y=status_counts.values[0].sum()/1.5, s=status_counts.values[0], color='White', weight='extra bold', ha='center', fontsize=15) #Text of labels

    ax1.bar(status_counts.keys()[2], status_counts.values[2], width=0.7, alpha=0.2, color=pal_red[3])
    ax1.text(x=status_counts.keys()[2], y=status_counts.values[2].sum()/1.5, s=status_counts.values[2], color='White', weight='extra bold', ha='center', fontsize=15) #Text of labels

    ax1.set_title("Πλήθος εργασιών ανά Status", color='White', fontsize=16)
    ax1.tick_params(axis='x', width=7, length=15, labelrotation=30, labelsize=15, bottom=True, direction="in", colors='White') #White
    ax1.tick_params(axis='y', labelsize=0) #White
    ax1.grid(False)

    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_color('White')
    ax1.spines['bottom'].set_linewidth(0.3)
    ax1.spines['left'].set_color('White')
    ax1.spines['left'].set_linewidth(0.3)


    labels = status_counts.keys()
    sizes = status_counts.values
    colors = [pal_red[3], pal_red[2], pal_red[1]]

    # Δημιουργία pie chart στο ax2
    ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'color':"white", 'fontsize':14})
    ax2.axis('equal')  # Ισοσκελές κύκλο
    ax2.set_title("Κατανομή Status", color='White', fontsize=16)

    ax2.tick_params(axis='y', labelsize=0) #White

    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.spines['top'].set_color('White')
    ax2.spines['top'].set_linewidth(0.3)
    ax2.spines['right'].set_color('White')
    ax2.spines['right'].set_linewidth(0.3)

    # Μετατροπή του γραφήματος σε PNG για αποστολή στο browser
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return Response(img.getvalue(), mimetype='image/png')


# In[ ]:




