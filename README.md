# FinancePredict — Ciência de Dados Financeiros

Projeto de portfólio em **Python**, **Pandas**, **scikit-learn** e **Streamlit** para comparação educacional de dois modelos de classificação aplicados a uma base pública histórica de risco de crédito.

## Objetivo
Comparar regressão logística e Random Forest, usando divisão de treino/teste estratificada e métricas ROC-AUC, PR-AUC e acurácia balanceada. O projeto demonstra tratamento de variáveis numéricas e categóricas, pipelines e comunicação de limitações.

## Executar
```bash
pip install -r requirements.txt
streamlit run app.py
```
Na primeira execução, os dados são obtidos do OpenML (`credit-g`, versão 1). É necessária conexão à internet.

## Testes
```bash
python -m pytest -q
```

## Fonte e licença dos dados
Hofmann, H. (1994). *Statlog (German Credit Data)*. UCI Machine Learning Repository. https://doi.org/10.24432/C5NC77 — CC BY 4.0. Obtidos via espelho OpenML credit-g.

## Uso responsável
Estudo exclusivamente educacional, **não adequado para decisões reais de crédito**. Dados antigos e de outro país, com risco de viés. Não fornece recomendações sobre concessão de crédito, e seu uso em produção exigiria validação e governança extensas.

## Próximas etapas
- Notebook de exploração e tratamento de dados.
- Validação cruzada e análise de calibração.
- Auditoria de vieses e estabilidade temporal em datasets apropriados.
- Testes de interface, CI e apresentação dos resultados no GitHub.

Autoria: Gabriela de Souza Lara.