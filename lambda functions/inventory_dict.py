inve_dict = [{"item":"Pen","stock":12},{"item":"Book","stock":0},{"item":"Bag","stock":5}]
result = list(filter(lambda x: x if x["stock"] > 0 else "",inve_dict))
print(result)
