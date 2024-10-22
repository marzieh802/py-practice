def cap_text(text):
    # return text.capitalize() #  its tests will fail
    try:
        return text.title()
    except:
        return "error!!!"
