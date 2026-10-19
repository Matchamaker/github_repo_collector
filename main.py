from github_collector import search_requests
from CSV_exporter import export_to_csv

query = input("enter your search query: ")
filename = query.replace(" ", "_") + ".csv"

repos =search_requests(query)

export_to_csv(repos, filename)
