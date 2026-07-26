# ALK projekt Zaliczeniowy DevOps - Calculator API

Prosta aplikacja REST API napisana w języku Python (FastAPI), konteneryzowana przy użyciu platformy Docker i wdrożona na AWS ECS z wykorzystaniem Terraform (IaC) i GitHub Actions (CI/CD).

## Architektura rozwiązania

*   **Aplikacja:** Python + FastAPI (endpointy: `/health`, `/version`, `/calculate`, `/docs`).
*   **Repozytorium:** GitHub.
*   **CI/CD:** GitHub Actions (automatyczne uruchamianie testów, budowanie obrazu Docker, wrzucanie do AWS ECR i aktualizowanie usługi AWS ECS).
*   **Chmura (AWS):**
    *   **ECR (Elastic Container Registry):** Przechowywanie obrazów Docker.
    *   **ECS (Elastic Container Service - Fargate):** Bezserwerowe uruchamianie kontenerów Docker z przypisanym publicznym adresem IP.
    *   **CloudWatch:** Agregacja i przechowywanie logów aplikacji.
*   **Infrastructure as Code (IaC):** Terraform (stan zignorowany przez .gitignore, nie znajduje się w repozytorium zdalnym ze względów bezpieczeństwa).

## Instrukcja uruchomienia (lokalnie)

1. Sklonuj repozytorium.
2. Zbuduj obraz lokalnie:
   ```bash
   docker build -t alk-calculator .
   ```
3. Uruchom kontener:
   ```bash
   docker run -p 8000:8000 alk-calculator
   ```
4. Aplikacja będzie dostępna pod adresem: `http://localhost:8000/health`. Dodatkowo, FastAPI generuje interaktywną dokumentację pod adresem `http://localhost:8000/docs`.

## Wdrożenie w chmurze (Terraform)

Do obsługi projektu należy utworzyć nowego użytkownika w AWS IAM oraz wygenerować Access keys.
Wdrożenie wymaga uwierzytelnienia w AWS za pomocą powyższego użytkownika (np. poprzez zainstalowane i skonfigurowane poleceniem `aws configure` AWS CLI lokalnie).


```bash
cd terraform
terraform init
terraform apply -auto-approve
```
*Pierwsze wdrożenie utworzy repozytorium ECR oraz przygotuje ECS. Kontener może początkowo być w stanie 'pending' aż do momentu zbudowania obrazu przez GitHub Actions.*

Aby wycofać wdrożenie i zwolnić zasoby AWS wykonujemy polecenie

```bash
terraform destroy -auto-approve
```

## Konfiguracja CI/CD (GitHub Actions)

Aby zautomatyzować proces, należy dodać 2 sekrety utowrzonego wcześniej użytkownika w AWS IAM (Repository Secrets) w ustawieniach repozytorium na GitHubie (`Settings` -> `Secrets and variables` -> `Actions`):
*   `AWS_ACCESS_KEY_ID`: Twój identyfikator klucza dostępu.
*   `AWS_SECRET_ACCESS_KEY`: Twój tajny klucz.

Po dodaniu sekretów, każde zatwierdzenie kodu (commit) i wypchnięcie zmian na gałąź `main` automatycznie uruchomi pipeline.

## Link do działającej aplikacji

> [TUTAJ WPISZ PUBLICZNY ADRES IP Z AWS ECS, np. http://X.X.X.X:8000/health ]
