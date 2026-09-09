# Nmap: The Basics

> Categoria: Reconhecimento / Networking
> Plataforma: TryHackMe
> Status: ✅ Estudado / evidenciado

## Objetivo
Aprender uma base de Nmap para descobrir hosts, portas e serviços e registrar resultados de reconhecimento em laboratórios.

## Conceitos aprendidos
- descoberta de hosts
- estados de portas
- detecção de versões
- scripts NSE
- timing e saída de resultados

## Ferramentas
`nmap`, shell e anotações de evidências.

## Comandos importantes
```bash
nmap -sn 192.168.56.0/24
nmap -sV -p 22,80,443 192.168.56.10
nmap -sC -sV 192.168.56.10
nmap -oA scans/host 192.168.56.10
```

## Metodologia
Descobrir → enumerar portas → identificar serviços/versões → aprofundar no serviço exposto → registrar hipóteses.

## O que eu aprendi
O uso do Nmap já foi praticado/estudado anteriormente. Não estou declarando que completei oficialmente esta room, apenas que o conteúdo faz parte dos estudos registrados.

## Lições importantes
Nmap não substitui enumeração específica do serviço. Uma porta aberta é apenas o início da investigação.

## Referências
- https://tryhackme.com/room/nmap
- https://nmap.org/docs.html
