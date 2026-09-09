# Metasploit: Introduction

> Categoria: Exploitation
> Plataforma: TryHackMe
> Status: ✅ Estudado / evidenciado

## Objetivo
Compreender a estrutura do Metasploit Framework e o fluxo de uso de módulos em máquinas de laboratório.

## Conceitos
- `msfconsole`
- módulos de exploit, scanner e auxiliary
- opções e parâmetros
- payloads
- sessões
- `msfvenom` como ferramenta auxiliar

## Comandos importantes
```text
msfconsole
search <termo>
use <módulo>
show options
set RHOSTS <LAB_IP>
run
sessions
```

## Metodologia
Enumerar serviço → pesquisar vulnerabilidade aplicável → selecionar módulo → configurar apenas parâmetros do laboratório → executar → validar resultado → documentar.

## O que eu aprendi
Metasploit, RHOSTS/LHOST, payloads e sessões já foram estudados anteriormente em contexto de laboratório, incluindo o uso conceitual de módulos SMB.

## Lições importantes
`RHOSTS` representa o alvo do laboratório e `LHOST` normalmente identifica o endereço local usado para receber uma conexão; os valores dependem da topologia do lab.

## Referências
- https://tryhackme.com/room/metasploitintro
- https://docs.metasploit.com/
