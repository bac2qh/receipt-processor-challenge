# FETCH receipt process challenge 
## Language and tool used:

- Python
- Flask
- Docker
- Git
- PostMan (optional)

## Input assumptions

- date in 'YYYY-MM-DD' format
- time in 'HH:MM' 24-hour format
- price with two decimal places

## How to run 

- register and install Github, Docker 
- git clone this repository 
- `cd` to the directory on your local machine 
- `docker compose up -d` 
- use PostMan or other API clients 
  - POST raw JSON file to <localhost:8000/receipts/process>
    - server should return `{"id": id}` where id is randomly generated via python UUID module 
  - Make a GET request to <localhost:8000/receipts/{id}/points> to query the points for receipt entry previously submitted 

## Next steps: 

- Include frontend development
- Switch to production server. Currently the service is run by Flask's test server. We can switch production server like [gunicorn](https://gunicorn.org/) in the future
- Data persistence. Currently the service stores data in memory based on sessions. We can store data in NoSQL database like cassandra in the future for JSON files
- Deduplication. Currently the service could contain duplicate entries. We can implement mechanisms such as hashing to prevent taking existing receipts.