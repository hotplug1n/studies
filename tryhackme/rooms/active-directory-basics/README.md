# Active Directory Basics

> Categoria: Windows / Active Directory
> Plataforma: TryHackMe
> Status: ✅ Concluída — evidência visual no perfil

## Objetivo
Construir uma visão geral de Active Directory e seus componentes.

## Conceitos aprendidos
- domain controller
- domains, trees e forests
- usuários e grupos
- trusts e Group Policy
- autenticação e AD DS

## Ferramentas
Windows, PowerShell, Active Directory Users and Computers e lab da room.

## Comandos importantes
```powershell
whoami
Get-ADUser -Filter *
Get-ADGroup -Filter *
```

## Metodologia
Entender arquitetura → identificar objetos → compreender identidade → relacionar permissões/políticas.

## O que aprendi
Consolidei AD como uma camada central de identidade e autorização em ambientes corporativos.

## Documentação de apoio
https://tryhackme.com/room/activedirectorybasics · https://learn.microsoft.com/windows-server/identity/ad-ds/

## Evidência
Room concluída no perfil apresentado.