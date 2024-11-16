import json
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

llm = GigaChat(
    credentials="ODdkYWUzMTYtZWNhYi00MjQxLWFmOWEtYjRlYjIwMjg2NDBiOjA2OTA1ZWUzLTgwMjgtNDQ4Yi05ZjEzLTg3ZDRhZDBhYjg3ZQ==",
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    verify_ssl_certs=False,
    streaming=False,
)

messages = [
    SystemMessage(
        content="Ты ИИ-помощник по методике Agile. Знаешь, что такое Scrum. Твоя задача - максимально упростить процесс ведения проекта по этой методике."
    )
]

# чтение промта для backlog
res = read_file("promt backlog.txt")

data = json.loads(read_file("start_data.json"))
text_request = (
    f"Название проекта - {data['project_name']}.\n"
    f"Краткое описание: {data['short_description']}.\n"
    f"Состав команды: {', '.join(data['team_composition'])}.\n"
    f"Стек разработки: {', '.join(data['tech_stack'])}.\n"
    f"Cрок - {data['deadline']}"
)

res += text_request
messages.append(HumanMessage(content=res))
res = llm.invoke(messages)

# запись backlog в json файл
output_lines = res.content.splitlines()
if len(output_lines) > 1:
    output_lines = output_lines[1:-1]
write_file("backlog.json", '\n'.join(output_lines) + '\n')

# чтение промта для sprint
sprint_req = read_file("promt sprint.txt")
sprint_req += "\nТекущий backlog: " + read_file("backlog.json")
messages.append(HumanMessage(content=sprint_req))
sprint_res = llm.invoke(messages)

sprint_data = {
    "count_sprints": 0,
    "sprints": []
}

current_sprint = {}

lines = sprint_res.content.strip().split('\n')
for line in lines:
    line = line.strip()
    if line.startswith("Спринт №"):
        if current_sprint:
            # Добавляем предыдущий спринт в список, если он существует
            sprint_data["sprints"].append(current_sprint)
            current_sprint = {}
        sprint_data["count_sprints"] += 1
        current_sprint["number"] = line
    elif line.startswith("Длительность спринта:"):
        current_sprint["duration"] = line.split(":")[1].strip()
    elif line.startswith("Задачи спринта:"):
        current_sprint["tasks"] = []
    elif line.startswith("-"):
        # Добавляем задачу в текущий спринт
        current_sprint["tasks"].append(line[1:].strip())

# Добавляем последний спринт, если он существует
if current_sprint:
    sprint_data["sprints"].append(current_sprint)

with open('sprint_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(sprint_data, json_file, ensure_ascii=False, indent=4)