import os

template = """# Day {day} of My DIY AI Internship

stuff to go here

[On to Day #{next_day}!](day-{next_day}.md)
"""

def create_file(day):
    filename = f"day-{day}.md"
    content = template.format(day=day, next_day=day+1)
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Created {filename}")

# Create files from day 11 to day 90
for day in range(11, 91):
    create_file(day)

print("All files created successfully!")