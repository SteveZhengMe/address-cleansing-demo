spaces = ' ' * 8
# Read openapi.yaml
with open('./swagger/openapi.yaml', 'r') as f:
    openapi_content = f.readlines()

parsed_content = []
# loop each line, find if the line has "'!Sub arn"
for line in openapi_content:
    if "'!Sub arn" in line:
        # If the line has "'!Sub arn", remove the first "'" and the last "'"
        line = line.replace("'", "")
    # Add 8 spaces to the beginning of each line
    line = spaces + line
    parsed_content.append(line)

# Read template_bk.yaml
with open('./template_template.yaml', 'r') as f:
    template_content = f.read()

# Replace "openapi: XXX" with the content of openapi.yaml
template_content = template_content.replace(f'{spaces}openapi: XXX', ''.join(parsed_content))

# Write the result to export.yaml
with open('./template.yaml', 'w') as f:
    f.write(template_content)