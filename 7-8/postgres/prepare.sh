sudo docker run -p 5433:5432 -d -e POSTGRES_PASSWORD=1234 -e POSTGRES_USER=admin -v $(pwd)/postgres-data:/var/lib/postgresql/data postgres
