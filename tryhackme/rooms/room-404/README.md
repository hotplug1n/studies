# Room 404

> Categoria: CTF / Web
> Status: ✅ Concluída — evidência visual no perfil

## Objetivo
Resolver um cenário curto de laboratório baseado em investigação de serviço exposto.

## Conceitos aprendidos
- enumeração
- análise de portas/serviços
- investigação web
- raciocínio orientado a pistas

## Ferramentas
Nmap, navegador, `curl` e shell.

## Comandos importantes
```bash
nmap -sC -sV LAB_IP
curl -I http://LAB_IP/
```

## Metodologia
Mapear → observar pistas → testar hipóteses → confirmar → registrar.

## O que aprendi
Reforcei que serviços aparentemente simples podem revelar a direção da investigação.

## Documentação de apoio
https://nmap.org/docs.html · https://developer.mozilla.org/en-US/docs/Web/HTTP

## Evidência
Room concluída no perfil apresentado.