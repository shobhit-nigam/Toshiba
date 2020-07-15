from jinja2 import Template

val = int(input("enter a value:\n"))

tempa = Template("value = {{ val }}")
stra = tempa.render(val=val)

print(stra)
