import yaml

with open("example.yaml", "r") as f:
    data = yaml.safe_load(f)

print(data)