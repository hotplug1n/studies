# 🧪 Burp Suite

## Objetivo
Usar o Burp Suite como plataforma de inspeção e teste de aplicações web em ambientes autorizados.

## Componentes principais
- **Proxy:** interceptação e visualização de HTTP(S).
- **Repeater:** repetição e alteração manual de requisições.
- **Intruder:** automação controlada de variações de requests.
- **Target:** definição de escopo e mapa do alvo.
- **Decoder/Comparer:** apoio à análise e transformação de dados.

## Fluxo recomendado
Configurar proxy → definir escopo → navegar na aplicação → mapear endpoints → reproduzir requisições importantes → testar hipóteses → registrar resposta.

## Comandos úteis
```bash
curl -i 'http://LAB_HOST/'
curl -i -X POST 'http://LAB_HOST/login' -d 'username=test&password=test'
```

## Status pessoal
**Estudado / em andamento.** O uso e os conceitos do Burp Suite já aparecem nos estudos anteriores; conclusão oficial da room não é presumida.

## Referências
- https://portswigger.net/burp
- https://portswigger.net/web-security
