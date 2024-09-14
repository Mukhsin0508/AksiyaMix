

def normalizer_text(obj):
    for i in obj.get_normalized_fields():
        field = getattr(obj, i)

        setattr(obj, i, " ".join(field.split()))

    return obj
