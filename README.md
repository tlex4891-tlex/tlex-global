# tlex-global (Template)

Globální projektový template pro Claude Code na webu. Tento repozitář slouží jako **šablona** pro zakládání nových projektů.

## Jak použít jako šablonu

1. Na GitHubu klikni **Use this template** → **Create a new repository**
2. Pojmenuj nový repozitář a vytvoř ho
3. Nový projekt automaticky zdědí SessionStart hook a CLAUDE.md sync

Alternativně ručně:

```bash
# Naklonuj šablonu
git clone https://github.com/tlex4891-tlex/tlex-global.git muj-novy-projekt
cd muj-novy-projekt

# Změň remote na nový repozitář
git remote set-url origin https://github.com/tlex4891-tlex/muj-novy-projekt.git
git push -u origin main
```

## Co obsahuje

- **SessionStart hook** — při každém otevření session automaticky stáhne aktuální `CLAUDE.md` z [`claude-global-config`](https://github.com/tlex4891-tlex/claude-global-config) do `~/.claude/CLAUDE.md`
- **CLAUDE.md** — odkaz na globální konfiguraci

## Jak funguje

1. Otevřeš nový projekt (vytvořený z této šablony) v Claude Code web app
2. SessionStart hook se automaticky spustí
3. Stáhne nejnovější `CLAUDE.md` z `claude-global-config`
4. Claude ho přečte a bude pracovat podle tvých globálních instrukcí

## Úprava globálních instrukcí

Edituj `CLAUDE.md` v repozitáři [claude-global-config](https://github.com/tlex4891-tlex/claude-global-config) — změny se projeví při další session automaticky.

## Projekty vytvořené z této šablony

- [timeline](https://github.com/tlex4891-tlex/timeline) — TLEX Timeline aplikace
