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

List all hotels.

### POST /api/hotels/

Create a new hotel.

The input hotel object should be in the following format:

```json
{
    "name": "Hotel Name",
    "address": "Hotel Address",
    "price": 100.0,
    "availability": true
}
```

### GET /api/reservations/

List all reservations.

### POST /api/reservations/

Create a new reservation.

The input reservation object should be in the following format:

```json
{
    "hotel": "hotel_id",
    "check_in": "2022-12-01",
    "check_out": "2022-12-10",
    "guest_list": [
        {
            "guest_name": "John Doe",
            "age": 30,
            "gender": "Male"
        },
        {
            "guest_name": "Jane Doe",
            "age": 28,
            "gender": "Female"
        }
    ]
}
```

Response

```json
{
    "confirmation_number": "reservation_id"
}
```

## Database

SQLite is used as the database for this project. The database file is located at `db.sqlite3`.

## Deployment

The project is deployed on AWS Elastic Beanstalk. The URL to access the deployed project is:

http://hotel-backend-django-dev.us-west-2.elasticbeanstalk.com/

Steps to deploy the project on AWS Elastic Beanstalk:

1. Install the Elastic Beanstalk CLI

```bash
pip install awsebcli
```

2. Initialize the Elastic Beanstalk project

```bash
eb init
```

3. Create a new environment

```bash
eb create
```

4. Deploy newly committed code

```bash
eb deploy
```

To deploy staged code

```bash
eb deploy --staged
```
