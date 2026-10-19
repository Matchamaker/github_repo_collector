import csv 

def export_to_csv(repositories, filename):
    with open(filename, 'w', newline= '') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Description', 'URL', 'Language', 'Last Updated'])
        for repo in repositories:
            writer.writerow([repo['name'], repo['description'], repo['html_url'], repo['language'], repo['updated_at']])


        print(f"Data exported to {filename} successfully.")    