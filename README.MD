# password-manager
Консольный менеджер паролей с шифрованием. Написан на Python.
A console password manager with encryption. Written in Python.

## Возможности
- Хранилище `vault.bin` зашифровано (Fernet), ключ получается из мастер-пароля через PBKDF2-HMAC-SHA256 (600 000 итераций) со случайной солью
- Генератор паролей на модуле `secrets` (длина от 8 до 32 символов, цифры и символы по желанию)
- Проверка мастер-пароля при первом запуске: не короче 12 символов, не из списка простых, ввод дважды
- Меню: добавить пароль, показать пароль, список сервисов, сгенерировать пароль

## Установка
pip install cryptography

## Запуск
python main.py

## Файлы
- main.py: меню и запуск
- storage.py: шифрование и хранение записей
- generator.py: генератор паролей
- checks.py: проверка мастер-пароля

## Важно
Учебный проект. Не храните в нём настоящие пароли: шифрование написано новичком и не проходило независимую проверку. Файл `vault.bin` не добавляйте в репозиторий.

## Features
- The `vault.bin` storage is encrypted (Fernet); the key is derived from the master password with PBKDF2-HMAC-SHA256 (600,000 iterations) and a random salt
- Password generator based on the `secrets` module (8 to 32 characters, digits and symbols optional)
- Master password check on first launch: at least 12 characters, not in a list of common passwords, entered twice
- Menu: add a password, show a password, list services, generate a password

## Installation
pip install cryptography

## Usage
python main.py

## Files
- main.py: menu and entry point
- storage.py: encryption and record storage
- generator.py: password generator
- checks.py: master password check

## Important
Educational project. Do not store real passwords in it: the encryption was written by a beginner and has not been independently reviewed. Do not commit the `vault.bin` file to the repository.