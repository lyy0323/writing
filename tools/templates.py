import datetime

today = datetime.date.today().strftime("%Y/%m/%d")


templates = {
    "工作日报": f"""## {today}

### 摘要

- 

### 进展

- 

### 思考

- 

### TODO

-"""
}

def help():
    print("Available templates:")
    for name, template in templates.items():
        print(f"- {name}")


def generate(template_name: str):
    if template_name not in templates:
        print(f"Template {template_name} not found")
        return
    return templates[template_name]


def generate_to_post(template_name: str, post_path: str):
    template = generate(template_name)
    with open(post_path, "a", encoding="utf-8") as f:
        f.write("\n---\n\n")
        f.write(template)


if __name__ == "__main__":
    # help()
    generate_to_post("工作日报", "../_posts/2025-06-22-工作周报2025w26.md")