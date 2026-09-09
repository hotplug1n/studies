# Blue

> Categoria: Windows / Exploitation Lab
> Status: ✅ Concluída — evidência visual no perfil

## Objetivo
Aplicar reconhecimento e exploração em uma máquina Windows de laboratório.

## Conceitos aprendidos
- enumeração de serviços
- validação de vulnerabilidades
- Metasploit
- relação entre vulnerabilidade e impacto

## Ferramentas
Nmap, Metasploit e ferramentas Windows.

## Comandos importantes
```bash
nmap -sC -sV LAB_IP
```

```text
msfconsole
search <vulnerability>
show options
set RHOSTS <LAB_IP>
run
```

## Metodologia
Enumerar → identificar serviço → pesquisar vulnerabilidade → validar no lab → registrar evidências.

## O que aprendi
Reforcei o fluxo de recon até exploração e a necessidade de confirmar versões antes de escolher um exploit.

## Documentação de apoio
https://nmap.org/docs.html · https://docs.metasploit.com/

## Evidência
Room concluída no perfil apresentado.