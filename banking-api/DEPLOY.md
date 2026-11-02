# Demonstração online — FinancePredict Bank

A aplicação web e a API REST são servidas **no mesmo projeto Spring Boot**, sem necessidade de outro servidor frontend.

## Teste local
1. Instale Java 17+ e Maven.
2. No terminal, execute:
   ```bash
   cd banking-api
   mvn test
   mvn spring-boot:run
   ```
3. Acesse http://localhost:8080/ .

## Publicação via Docker
O Dockerfile em `banking-api/Dockerfile` é compatível com plataformas que constroem a aplicação a partir de um repositório Git, como Render e Railway, sujeito à disponibilidade e aos limites dos planos.

Configuração sugerida:
- Repositório: `gabrielaslara-cyber/FinancePredict`
- Branch: `feature/java-spring-api`
- Root directory / contexto de build: `banking-api`
- Runtime: **Docker**
- Arquivo Dockerfile: `Dockerfile`
- Porta: a plataforma deve fornecer `PORT`; a aplicação usa `${PORT:8080}`

Depois que a hospedagem publicar uma URL HTTPS, abra o endereço raiz (`/`) para acessar o painel.

**Atenção:** aplicativo educacional sem autenticação nem persistência. Não use dados pessoais ou dinheiro real. Contas fictícias são compartilhadas no processo servidor e perdem-se em reinicializações. Não utilizar em produção como sistema financeiro.
