import subprocess
import os

# Настроить репозиторий Git и параметры установки
repo_url = "https://github.com/GhostlyThunder/Test1"  # URL репозитория
install_dir = "D:/VS"  # Место установки

# Проверить, запускается ли приложение впервые
if not os.path.isfile("first_run_complete"):

    # Проверить наличие обновлений
    result = subprocess.run(['pip', 'list', '--outdated', '--user', '--find-links', repo_url], capture_output=True)
    output = result.stdout.decode('utf-8')
    if "No packages are out of date" in output:
        # Нет обновлений
        print("Нет доступных обновлений.")
    else:
        # Найдены обновления
        print("Обнаружены обновления. Установка...")

        # Установить обновления
        subprocess.run(['pip', 'install', '--upgrade', '--user', install_dir, repo_url])

    # Отметить, что первый запуск завершен
    with open("first_run_complete", "w") as f:
        f.write("True")