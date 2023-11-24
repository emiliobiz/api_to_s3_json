import requests
import pandas as pd
import boto3
from datetime import datetime

# Make a GET request to the API
response = requests.get('https://data.kingcounty.gov/resource/f29f-zza5.json')

# Convert the response to JSON
data = response.json()

# Convert the JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Get the current datetime to use in the file name
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Write the DataFrame to a CSV file with a timestamp
csv_file = f'food_violations_{current_time}.csv'
df.to_csv(csv_file, index=False)

# Create an S3 client
s3 = boto3.client('s3')

# Replace 'my-bucket' with the name of your bucket
bucket_name = 'food-establishment-bucket'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(csv_file, bucket_name, csv_file)
