def namelist(names):
    names_only = [el['name'] for el in names]

    if not names_only:
        return ""
    elif len(names_only) == 1:
        return names_only[0]
    elif len(names_only) == 2:
        return " & ".join(names_only)
    elif len(names_only) >= 3:
        last_name = names_only.pop()
        result = ", ".join(names_only) + " & " + last_name
        return result
