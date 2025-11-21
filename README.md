# Project _OKT

A web application for daily diary entries with music & video integration.

## 📝 Overview

Project _OKT lets users record their daily thoughts, emotions, and moments — and embed them in short video or music-like diary entries. Think of it as a digital diary + creative journal.  

Key features include:  
- Create diary entries with text  
- (Optionally) attach videos (or music) to entries  
- View entries in an indexed list  
- Expand/collapse entry content for clean UI  

## 🚀 Tech Stack

- **Backend**: Flask (or whatever framework you’re using)  
- **Frontend**: HTML, CSS, JavaScript  
- **Static files**: Stored in a `static/` directory (images, CSS, video)  
- **Templates**: Jinja / HTML templating  

## 💻 Installation & Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/JustKenTabata/Project_OKT.git
   
   cd Project_OKT

   python3 -m venv venv  
   source venv/bin/activate  
   pip install -r requirements.txt  
   flask run  
