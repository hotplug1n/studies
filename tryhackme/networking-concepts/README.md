# Networking Concepts

> Categoria: Networking
> Plataforma: TryHackMe
> Status: 🔎 Conteúdo pesquisado

## Objetivo
Consolidar OSI, IP, sub-redes, roteamento, TCP, UDP e portas antes de avançar para enumeração e análise de tráfego.

## Conceitos aprendidos
- OSI como modelo de referência
- camada de rede e endereçamento IP
- camada de transporte e portas
- TCP orientado a conexão vs UDP sem conexão
- roteadores encaminhando tráfego entre redes

## Ferramentas
`ip`, `ss`, `ping`, `tracepath`.

## Comandos importantes
```bash
ip addr
ip route
ss -lntup
ping -c 4 192.168.1.1
tracepath example.com
```

## Metodologia
Primeiro compreender a comunicação entre hosts; depois relacionar IP, porta, protocolo e serviço ao que aparece em uma ferramenta de recon.

## Conteúdo pesquisado
A página oficial da room cobre OSI, IP/subnets/routing, TCP/UDP/portas e conexão a uma porta TCP aberta.

## Lições importantes
Pensar em camadas ajuda a localizar a origem de um problema e a interpretar resultados de segurança.

## Referências
- https://tryhackme.com/room/networkingconcepts
