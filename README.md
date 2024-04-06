## Running the project

To run using the local server, run the following command in the terminal:

```
python manage.py runserver
```

Then, open your browser and go to the following URL:

```
http://127.0.0.1:8000/
```

## API Endpoints

### GET /api/hotels/

List all hotels

### POST /api/hotels/

Create a new hotel

The hotel object should be in the following format:

```
{
    "name": "Hotel Name",
    "address": "Hotel Address",
    "price": 100.00,
    "availability": true
}
```

## Database

SQLite is used as the database for this project. The database file is located at `db.sqlite3`.
