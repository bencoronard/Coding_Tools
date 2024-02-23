import re

# Read from input.txt
with open('input.txt', 'r') as input_file:
    content = input_file.read()

# Remove newline and trailing whitespaces
content = re.sub(r'\n\s*', '', content)

# Write to output.txt
output_file_path = 'output.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(content)

# Print success message
print(f"Write successful. Output written to {output_file_path}")
