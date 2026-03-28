# Golf Stats App

A Django-based web application for tracking and analyzing golf performance.

---

## 🚀 Features (Current)

### Round Tracking

* Create golf rounds
* Enter course, tee, and date
* Navigate hole-by-hole

### Hole Entry

* Par tracking
* Approach distance (yards)
* GIR tracking
* Pin position (front / middle / back)
* Putting:

  * Multiple putts per hole
  * Distance tracking
  * Made/missed tracking

---

## 🧱 Tech Stack

* Python 3.10+
* Django 5
* SQLite (local dev)
* Bootstrap (UI)
* Poetry (dependency management)

---

## ⚙️ Setup (Windows + Poetry 2.0)

### 1. Install dependencies

```bash
poetry install
```

### 2. Activate environment (Windows)

```bash
.venv\Scripts\activate
```

### 3. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create admin user

```bash
python manage.py createsuperuser
```

### 5. Run server

```bash
python manage.py runserver
```

---

## 🌐 Access

* App: http://127.0.0.1:8000/
* Admin: http://127.0.0.1:8000/admin/

---

## 📁 Project Structure

```
apps/
  rounds/        # round + hole + putt logic
  reference/     # clubs and lookup data
config/          # Django settings
templates/       # UI templates
```

---

## 📊 Roadmap

### Next Features

* Fairway tracking (hit / miss left / right)
* Club tracking (driver, irons, etc.)
* GIR miss direction
* Up-and-down tracking
* Validation rules (putting, GIR logic)

### Future

* Historical dashboard
* Stats by club / distance / pin position
* Advanced analytics (strokes gained)
* Mobile-first UI improvements

---

## 🧠 Notes

* Built as a **personal golf analytics tool**
* Designed to evolve into a **full performance tracking system**
* Optimized for **fast entry during a round**

---

## 🧪 Development Tips

If models change:

```bash
python manage.py makemigrations
python manage.py migrate
```

If things break early on:

```bash
del db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Author

Ben Lieberman

---
