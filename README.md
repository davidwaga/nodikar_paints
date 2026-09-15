# ColorCraft Paints - Django Website

A complete, responsive Django paint-company website using Bootstrap, one custom CSS file and minimal JavaScript.

## 1. Create a virtual environment

Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:
```powershell
python -m venv venv
venv\Scripts\activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create database

```bash
python manage.py makemigrations
python manage.py migrate
```

## 4. Create admin user

```bash
python manage.py createsuperuser
```

## 5. Start server

```bash
python manage.py runserver
```

Open:
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 6. Add content

Log in to Django Admin and create:
1. Product categories
2. Products
3. Blog posts

Mark products as "Featured" to show them on the home page.

## Notes

- Database is SQLite for easy development.
- Uploaded images go into `media/`.
- Replace the phone number, email, WhatsApp number and company details in `templates/includes/footer.html`.
- Change the secret key and DEBUG setting before production deployment.

## Product inventory fields

Each product now supports:
- Unique SKU
- Stock quantity
- Reorder level
- Pack size
- Color
- Cost price (UGX)
- Selling price (UGX)

The admin product list supports searching by SKU/name/color/pack size and inline editing of stock, reorder level and prices. A Low Stock column is also provided.

For an existing installation, run:
```bash
python manage.py makemigrations
python manage.py migrate
```
For this starter project, an initial `products` migration is already included.