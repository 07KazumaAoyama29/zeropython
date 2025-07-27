def make_car(name, model, **kwargs):
    kwargs["name"] = name
    kwargs["model"] = model
    return kwargs
print(make_car("subaru", "regacy", color = "blue", recorder = False))