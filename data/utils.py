import csv
import json


def csv_to_json(csv_path, json_path, model_name):
    json_array = []

    #read the CSV file
    with open(csv_path, encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if "price" in row.keys():
                row['price'] = int(row['price'])
            if "age" in row.keys():
                row['age'] = int(row['age'])
            if "location_id" in row.keys():
                row['location_id'] = int(row['location_id'])
            if "category_id" in row.keys():
                row['category_id'] = int(row['category_id'])
            if "author_id" in row.keys():
                row['author_id'] = int(row['author_id'])
            if "lat" in row.keys():
                row['lat'] = float(row['lat'])
            if "lng" in row.keys():
                row['lng'] = float(row['lng'])
            if 'is_published' in row.keys():
                check_is_published(row)
            to_add = {'model': model_name, 'pk': int(row['Id'] if 'Id' in row else row['id'])}

            if 'Id' in row:
                del row['Id']
            else:
                del row['id']
            to_add['fields'] = row
            json_array.append(to_add)

    #write to the json
    with open(json_path, 'w', encoding='utf-8') as f:
        json_string = json.dumps(json_array, indent=4, ensure_ascii=False)
        f.write(json_string)


def check_is_published(row):
    if row["is_published"] == "TRUE":
        row["is_published"] = True
    if row["is_published"] == "FALSE":
        row["is_published"] = False
    return row
