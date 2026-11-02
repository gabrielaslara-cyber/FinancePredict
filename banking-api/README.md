# FinancePredict Banking API — Java 17 + Spring Boot

API REST demonstrativa para portfólio de desenvolvimento back-end na área bancária.

## Funcionalidades
- Criar contas fictícias.
- Consultar saldo.
- Registrar depósitos e saques simulados.
- Impedir saques com saldo insuficiente.
- Consultar histórico das movimentações.
- Trabalhar com valores monetários em **BigDecimal** e validação de entrada.
- Testes unitários com JUnit 5.

## Tecnologias
**Java 17**, **Spring Boot 3.3**, **Maven**, **Bean Validation**, **JUnit 5**.

Java 17 atende a vagas que exigem Java 11 ou superior. Spring Boot 3 exige Java 17+.

## Executar localmente
Requer JDK 17+ e Maven 3.6+:
```bash
cd banking-api
mvn spring-boot:run
```

## Testar
```bash
cd banking-api
mvn test
```

## Endpoints
| Método | Rota | Corpo |
|---|---|---|
| POST | `/api/v1/accounts` | `{"holder":"Cliente de teste"}` |
| GET | `/api/v1/accounts/{id}` | — |
| POST | `/api/v1/accounts/{id}/deposits` | `{"amount":150.00}` |
| POST | `/api/v1/accounts/{id}/withdrawals` | `{"amount":40.00}` |
| GET | `/api/v1/accounts/{id}/transactions` | — |

### Exemplo
```bash
curl -X POST http://localhost:8080/api/v1/accounts -H "Content-Type: application/json" -d '{"holder":"Cliente de teste"}'
```
Copie o `id` da resposta e use nas demais rotas.

## Limitações e próximos passos
**Não é um sistema bancário real.** Todas as contas e transações são fictícias, ficam somente na memória e desaparecem ao reiniciar a API. Não há autenticação, banco de dados, auditoria imutável, controle transacional persistente ou adequação regulatória. Não conectar a contas ou dados financeiros reais.

Próximas melhorias possíveis: PostgreSQL, Spring Data JPA, autenticação, documentação OpenAPI, testes de integração e pipelines CI.

Autoria: Gabriela de Souza Lara.
