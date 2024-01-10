import re

def extract_links(input_html: str) -> list:
    split_input = input_html.split('\n') # Splits the string into a list separated by the newline
    pattern = re.compile(r"href\=\"(.*?)\"\>(.*?)\<")
    output = []
    for line in split_input:
        search = pattern.search(line)
        if search != None:
            res = search.group(1).split('"')[0] + ',' + search.group(2)
            output.append(res)
    return output
