## Food Violations Data Collection

This Python script collects food violations data from the King County API, converts the data into a pandas DataFrame, and then uploads the data to an Amazon S3 bucket.
How it works

1. The script starts by making a GET request to the King County API to retrieve the food violations data.

2. The response from the API is converted to JSON format.

3. The JSON data is then converted into a pandas DataFrame for easier data manipulation.

4. The DataFrame is saved as a CSV file. The filename includes the current date and time to ensure uniqueness and avoid overwriting existing files in the S3 bucket.

5. The script creates an S3 client using boto3.

6. The CSV file is uploaded to the specified S3 bucket. If the file is large, the upload process will automatically split the file into smaller parts and upload them in parallel.

## Usage

To use this script, you need to replace 'food-establishment-bucket' with the name of your S3 bucket in the bucket_name variable.
Dependencies

This script requires the following Python libraries:

- requests
- pandas
- boto3
